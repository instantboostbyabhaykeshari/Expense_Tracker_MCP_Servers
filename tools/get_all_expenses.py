from database import get_connection

def get_all_expenses() -> list:
    conn = get_connection()
    
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """SELECT id, amount, category, sub_category, description, expense_date, created_at from expenses;"""
            )
                
            rows = cursor.fetchall()
        
            return [
                {
                    "id": row[0],
                    "amount": float(row[1]),
                    "category": row[2],
                    "sub_category": row[3],
                    "description": row[4],
                    "expense_date": str(row[5]),
                    "created_at": str(row[6])
                }
                for row in rows
            ]
                
    finally:
        conn.close()