# import cowsay

# cowsay.cow("Hello world!") # type: ignore
# cowsay.dragon("I'm a dragon!") # type: ignore
# cowsay.tux("Look where it brings you. Back to me.") # type: ignore

# from art import *

# tprint("Hello!")

from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Список студентів")
table.add_column("Ім'я", style="cyan")
table.add_column("Проєкт", style="magenta")

table.add_row("Андрій", "Чат-бот")
table.add_row("Марія", "Гра на Python")

console.print(table)