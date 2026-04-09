import random
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()
history = []  # Список для збереження історії раундів
round_number = 1
options = ["Камінь", "Ножиці", "Папір"]

def show_menu():
    menu_text = "[cyan]1.[/cyan] Почати гру\n[cyan]2.[/cyan] Історія ігор\n[cyan]3.[/cyan] Вихід"
    panel = Panel(menu_text, title="[bold magenta]Головне меню[/bold magenta]", expand=False)
    console.print(panel)

def play_round():
    global round_number
    # Prompt.ask з choices гарантує, що юзер введе тільки правильне слово
    player_choice = Prompt.ask("\n[bold yellow]Ваш вибір[/bold yellow]", choices=options)
    computer_choice = random.choice(options)
    
    console.print(f"Комп'ютер обрав: [bold cyan]{computer_choice}[/bold cyan]")
    
    # Логіка гри
    if player_choice == computer_choice:
        result = "Нічия"
        color = "yellow"
    elif (player_choice == "Камінь" and computer_choice == "Ножиці") or \
         (player_choice == "Ножиці" and computer_choice == "Папір") or \
         (player_choice == "Папір" and computer_choice == "Камінь"):
        result = "Перемога"
        color = "green"
    else:
        result = "Поразка"
        color = "red"
        
    console.print(f"[{color}][bold]Результат: {result}![/bold][/{color}]\n")
    
    # Зберігаємо в історію
    history.append({
        "round": str(round_number),
        "player": player_choice,
        "computer": computer_choice,
        "result": f"[{color}]{result}[/{color}]" # Зберігаємо одразу з кольоровим тегом
    })
    round_number += 1

def show_history():
    if not history:
        console.print("[yellow]Історія порожня. Зіграйте хоча б один раунд![/yellow]\n")
        return

    table = Table(title="[bold magenta]Історія матчів[/bold magenta]")
    table.add_column("Раунд", justify="center", style="cyan")
    table.add_column("Гравець", justify="center")
    table.add_column("Комп'ютер", justify="center")
    table.add_column("Результат", justify="center")

    for match in history:
        table.add_row(match["round"], match["player"], match["computer"], match["result"])

    console.print(table)
    console.print()

# Головний цикл програми
console.print("[bold green]Вітаємо в Аркаді![/bold green] 🎮")
while True:
    show_menu()
    choice = Prompt.ask("Оберіть дію", choices=["1", "2", "3"])
    
    if choice == "1":
        play_round()
    elif choice == "2":
        show_history()
    elif choice == "3":
        console.print("[bold magenta]Дякуємо за гру! Бувай![/bold magenta] 👋")
        break