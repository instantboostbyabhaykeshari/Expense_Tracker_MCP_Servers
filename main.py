import random
from fastmcp import FastMCP
import psycopg

mcp = FastMCP(name="Dice Roller")

@mcp.tool
def roll_dice(n_dice: int) -> list[int]:
    """Roll `n_dice` 6-sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers a and b."""
    return a+b

@mcp.tool
def subtract(a: int, b: int) -> int:
    """Subtract two numbers a and b."""
    return a-b

if __name__ == "__main__":
    mcp.run()