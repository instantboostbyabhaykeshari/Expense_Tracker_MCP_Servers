from datetime import date
from database import get_connection


def add_expenses(amount: float, category: str, sub_category: str, description: str, expense_date: date) -> dict:
    conn = get_connection()
    
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """ INSERT INTO expenses (amount, category, sub_category, description, expense_date)
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING id
                """,    
                (amount, category, sub_category, description, expense_date)
            )
            
            expense_id = cursor.fetchone()[0]
                
        conn.commit()
        
        return {
            "success": True,
            "id": expense_id,
            "messages": "Expense added successfully!"
        }
        
    finally:
        conn.close()
    