import typer
from rich import print
from rich.table import Table
from app.config import get_db_connection

app = typer.Typer(help="Manage your personal tasks")

# Initialize database table for tasks
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            done BOOLEAN
        )
    """)
    conn.commit()
    conn.close()

@app.command()
def add(title: str):
    """Add a new task"""
    conn = get_db_connection()
    conn.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", (title, False))
    conn.commit()
    conn.close()
    print(f"[green]Task added:[/green] {title}")

@app.command()
def list():
    """List all tasks"""
    conn = get_db_connection()
    cursor = conn.execute("SELECT id, title, done FROM tasks")
    table = Table(title="Your Tasks")
    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Status")

    for row in cursor:
        status = "✅" if row[2] else "❌"
        table.add_row(str(row[0]), row[1], status)

    print(table)

@app.command()
def done(task_id: int):
    """Mark task as completed"""
    conn = get_db_connection()
    conn.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    print(f"[cyan]Task {task_id} marked as done[/cyan]")

@app.command()
def delete(task_id: int):
    """Delete a task"""
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    print(f"[red]Task {task_id} deleted[/red]")

init_db()
