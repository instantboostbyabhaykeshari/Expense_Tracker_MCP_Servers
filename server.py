from fastmcp import FastMCP
from datetime import date

from database import initialize_database
from tools.add_expenses import add_expenses

mcp = FastMCP("Expense Tracker MCP Server")

@mcp.tool()
def add_expense_tool(amount: float, category: str, sub_category: str, description: str, expense_date: date) -> dict:
    """Add a new expense in the database."""
    return add_expenses(amount, category, sub_category, description, expense_date)



if __name__ == "__main__":
    try:
        initialize_database()
        mcp.run()
    except Exception as exc:
        print(f"omething Error in mcp: {exc}")
        raise