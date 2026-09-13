from fastmcp import FastMCP
from datetime import date

from database import initialize_database
from tools.add_expenses import add_expenses
from tools.get_all_expenses import get_all_expenses
from tools.delete_expenses import delete_expenses

mcp = FastMCP("Expense Tracker MCP Server")

@mcp.tool()
def add_expense_tool(amount: float, category: str, sub_category: str, description: str, expense_date: date) -> dict:
    """Add a new expense in the database."""
    return add_expenses(amount, category, sub_category, description, expense_date)


@mcp.tool()
def get_all_expense() -> list:
    """Fetch all expenses from the database."""
    return get_all_expenses()

@mcp.tool()
def delete_expense(expense_id: int) -> dict:
    """Delete expense with respect with expense id from the database."""
    return delete_expenses(expense_id)


def main() -> None:
    try:
        initialize_database()
        mcp.run()
    except Exception as exc:
        print(f"Something Error in mcp server or in tools: {exc}")
        raise


if __name__ == "__main__":
    main()