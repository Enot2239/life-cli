import typer
from rich import print
from rich.table import Table
from datetime import date
from app.config import get_db_connection

app = typer.Typer(help="Track your daily habits")

# Initialize database table for habits
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            name TEXT,
            day TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.command()
def track(name: str):
    """Mark a habit as done for today"""
    today = str(date.today())
    conn = get_db_connection()
    conn.execute("INSERT INTO habits (name, day) VALUES (?, ?)", (name, today))
    conn.commit()
    conn.close()
    print(f"[green]Tracked:[/green] {name} on {today}")

@app.command()
def history(name: str):
    """Show history for a habit"""
    conn = get_db_connection()
    cursor = conn.execute("SELECT day FROM habits WHERE name = ? ORDER BY day", (name,))
    days = [row[0] for row in cursor]

    if not days:
        print(f"[yellow]No history found for habit '{name}'[/yellow]")
        return

    table = Table(title=f"History for '{name}'")
    table.add_column("Date")
    for day in days:
        table.add_row(day)

    print(table)

@app.command()
def list():
    """List all habits tracked"""
    conn = get_db_connection()
    cursor = conn.execute("SELECT DISTINCT name FROM habits")
    habits = [row[0] for row in cursor]

    if not habits:
        print("[yellow]No habits tracked yet[/yellow]")
        return

    table = Table(title="Tracked Habits")
    for habit in habits:
        table.add_row(habit)

    print(table)

init_db()
