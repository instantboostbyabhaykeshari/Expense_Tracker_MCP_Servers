import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    );
    

def initialize_database():
    conn = get_connection()
    
    try:
        with conn.cursor() as cursor:
            with open("db/schema.sql", "r") as file:
                schema = file.read()
                
            cursor.execute(schema)
        conn.commit()       
        print("Database initialized successfully!")
        
    finally:
        conn.close()