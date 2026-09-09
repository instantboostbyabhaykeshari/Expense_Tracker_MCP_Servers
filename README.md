# Expense Tracker MCP

An **MCP (Model Context Protocol) server** that allows AI assistants such as Claude Desktop to manage expenses using natural language.

The server provides tools to **add, view, and delete expenses**, with PostgreSQL handling persistent storage.

## Features

- Add expenses with amount, category, sub-category, description, and date
- View all stored expenses
- Delete expenses by ID
- PostgreSQL database integration
- Modular MCP tool architecture
- Automatic database schema initialization
- Claude Desktop integration

## Tech Stack

- **Python**
- **FastMCP / MCP**
- **PostgreSQL**
- **Psycopg 3**
- **uv**
- **python-dotenv**
- **Claude Desktop**

## Project Structure

```text
MCP Servers/
│
├── db/
│   └── schema.sql
│
├── tools/
│   ├── add_expenses.py
│   ├── delete_expenses.py
│   └── get_all_expenses.py
│
├── .env
├── database.py
├── server.py
└── README.md