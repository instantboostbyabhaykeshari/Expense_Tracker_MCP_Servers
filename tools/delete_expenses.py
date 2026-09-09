from database import get_connection

def delete_expenses(expense_id: int) -> dict:
    conn = get_connection()
    
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """ DELETE FROM expenses
                    WHERE id = %s
                    RETURNING id
                """,
                (expense_id,)
            )   
            deleted = cursor.fetchone()
            
        conn.commit()  
                
        if deleted:
            return {
                "success": True,
                "messages": "Expense deleted successfully!"
            }   
                
        return {
            "success": False,
            "message": "Expense not found"
        }
    finally:
        conn.close()