import typer
from app import tasks, passwords, habits

app = typer.Typer(help="life-cli — your daily command-line productivity assistant")

# Register subcommands
app.add_typer(tasks.app, name="task", help="Task manager")
app.add_typer(passwords.app, name="pass", help="Password generator")
app.add_typer(habits.app, name="habit", help="Habit tracker")

if __name__ == "__main__":
    app()
