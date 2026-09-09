from datetime import date
from typing import Optional
from database import get_connection


def add_expenses(amount: float, category: str, sub_category: str, description: str, expense_date: Optional[date] = None):
    conn = get_connection()
    
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """ INSERT INTO expenses (amount, category, sub_category, description, expense_date)
                    VALUES (%s, %s, %s, %s, %s)
                """
                    
                (amount, category, sub_category, description, expense_date)
            )
                
        conn.commit()
    finally:
        conn.close()
        
    print("Your all expense added successfully!")
    