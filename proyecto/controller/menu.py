from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

from controller.function import ingest_data
from controller.reports import generar_reporte

def menu(app):
    console = Console()

    while True:
        menu_text = Text()
        menu_text.append("\n[bold cyan]Proyecto de Libros[/bold cyan]\n", style="underline bold")
        menu_text.append("[1] 🟢 Ingestar Data\n", style="green")
        menu_text.append("[2] 📈 Generar Reporte\n", style="blue")
        menu_text.append("[3] ❌ Salir\n", style="red")

        console.print(Panel(menu_text, title="[bold magenta]Menú Principal[/bold magenta]", expand=False, border_style="yellow"))

        opcion = Prompt.ask("[bold yellow]Selecciona una opción[/bold yellow]", choices=["1", "2", "3"], default="3")

        if opcion == "1":
            ingest_data(app)
        elif opcion == "2":
            generar_reporte(app)
        elif opcion == "3":
            break
