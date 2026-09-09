import os
from database import get_connection


def test_connection():
    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT version();")
            result = cursor.fetchone()
        print("PostgreSQL connected")
        print(result)
    finally:
        conn.close()


if __name__ == "__main__":
    try:
        test_connection()
    except Exception as exc:
        print(f"Database connection failed: {exc}")
        print("Check DB_HOST, DB_PORT, DB_NAME, DB_USER, and DB_PASSWORD in your environment or .env file.")
        raise