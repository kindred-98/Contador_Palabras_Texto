# src/main.py

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from text_analyzer.interfaces.cli import historial, run_cli
from text_analyzer.interfaces.gui import run_gui
from text_analyzer.core.models import AnalysisResult

console = Console()


def resumen_historial(h):
    """
    Convierte un item del historial en texto legible.
    - Si es string → lo devuelve tal cual
    - Si es AnalysisResult → devuelve primeras 60 caracteres del texto analizado
    """
    if isinstance(h, AnalysisResult):
        t = h.raw_text.strip().replace("\n", " ")
        return t[:60] + ("..." if len(t) > 60 else "")
    return str(h)


def mostrar_menu_principal():
    # Panel principal con título
    console.print(Panel("[bold cyan]🚀 TEXT ANALYZER PRO+[/bold cyan]", subtitle="Selecciona una opción", expand=False))

    # Opciones con iconos y colores
    console.print("[green]1) Usar en Terminal (CLI) 📂[/green]")
    console.print("[magenta]2) Abrir Interfaz Gráfica (GUI) 🖥️[/magenta]")
    console.print("[yellow]3) Ver historial rápido 📜[/yellow]")
    console.print("[red]4) Salir ❌[/red]")


def mostrar_historial_rapido():
    """Muestra los últimos 5 análisis del historial."""
    table = Table(title="📜 Historial rápido", show_lines=True)
    table.add_column("N°", style="cyan", no_wrap=True)
    table.add_column("Último análisis", style="magenta")

    if historial:
        for i, h in enumerate(historial[-5:], 1):  # últimos 5 análisis
            table.add_row(str(i), resumen_historial(h))
    else:
        table.add_row("-", "No hay análisis previos")

    console.print(table)


def main():
    while True:
        mostrar_menu_principal()
        opcion = Prompt.ask("\nElige una opción", choices=["1", "2", "3", "4"], default="1")

        if opcion == "1":
            run_cli()
        elif opcion == "2":
            run_gui()
        elif opcion == "3":
            mostrar_historial_rapido()
        elif opcion == "4":
            console.print("\n[bold red]👋 ¡Hasta luego![/bold red]")
            break


if __name__ == "__main__":
    main()