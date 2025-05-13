import string
import secrets
import typer
from rich import print

app = typer.Typer(help="Secure password generator")

@app.command()
def generate(
    length: int = typer.Option(
        12,
        "--length",
        "-l",
        help="Length of the password",
        min=4,
        max=128
    ),
    symbols: bool = typer.Option(
        True,
        "--symbols/--no-symbols",
        "-s/--no-s",
        help="Include special characters"
    ),
):
    """
    Generate a secure password with optional symbols and custom length.
    """
    chars = string.ascii_letters + string.digits
    if symbols:
        chars += string.punctuation

    password = ''.join(secrets.choice(chars) for _ in range(length))
    print(f"[bold green]Generated password:[/bold green] {password}")
