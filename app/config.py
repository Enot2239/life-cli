from pathlib import Path
import sqlite3

# Path to local SQLite database
DB_PATH = Path.home() / ".life_cli.db"

# Get database connection
def get_db_connection():
    return sqlite3.connect(DB_PATH)
