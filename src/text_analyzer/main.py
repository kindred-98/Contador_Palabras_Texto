# ==============================
# Analizador de Texto – Fase 1 PRO+ 
# ==============================

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.progress import track
from rich.bar import Bar
from collections import Counter
import time

console = Console()
historial = []

# Función para mostrar menú interactivo
def mostrar_menu():
    console.print(Panel("[bold cyan]📂 MENÚ DEL ANALIZADOR DE TEXTO[/bold cyan]",
                        subtitle="Selecciona una opción", expand=False))
    console.print("[green]1) Analizar texto completo[/green] 📄")
    console.print("[yellow]2) Analizar palabra específica[/yellow] 🔍")
    console.print("[magenta]3) Ver historial de análisis[/magenta] 📜")
    console.print("[blue]4) Exportar resultados[/blue] 💾")
    console.print("[red]5) Salir[/red] ❌")
    opcion = Prompt.ask("Ingresa el número de la opción")
    return opcion

# Función para analizar texto completo
def analizar_texto():
    texto = Prompt.ask("\nIngresa el texto a analizar 📄")

    # Barra de progreso simulando análisis
    console.print("\n[bold green]Analizando texto...[/bold green]")
    for _ in track(range(50), description="Procesando..."):
        time.sleep(0.01)

    palabras = texto.split()
    num_palabras = len(palabras)
    num_caracteres = len(texto)
    contador_palabras = Counter(palabras)
    palabra_mas_comun = contador_palabras.most_common(1)[0]

    # Mostrar estadísticas generales
    analisis = f"[bold green]Total palabras:[/bold green] {num_palabras} | " \
               f"[bold green]Total caracteres:[/bold green] {num_caracteres} | " \
               f"[bold yellow]Palabra más frecuente:[/bold yellow] '{palabra_mas_comun[0]}' ({palabra_mas_comun[1]} veces)"
    console.print(Panel(analisis, title="✅ Estadísticas Generales", expand=False))
    
    # Mostrar tabla de las palabras más frecuentes
    table = Table(title="📊 Palabras más frecuentes", show_lines=True)
    table.add_column("Palabra", style="cyan", no_wrap=True)
    table.add_column("Frecuencia", style="magenta")
    table.add_column("Visual", style="green")

    top_palabras = contador_palabras.most_common(10)
    max_freq = top_palabras[0][1] if top_palabras else 1
    for palabra, freq in top_palabras:
        bar = "█" * int((freq / max_freq) * 20)
        table.add_row(palabra, str(freq), bar)
    console.print(table)

    guardar_historial(analisis)
    return texto

# Función para analizar palabra específica
def analizar_palabra(texto):
    if not texto:
        console.print("[red]Primero debes analizar un texto completo.[/red]")
        return

    palabra = Prompt.ask("Ingresa la palabra a analizar 🔍").lower()
    palabras_lista = texto.lower().split()
    contador = palabras_lista.count(palabra)
    posiciones = [i+1 for i, p in enumerate(palabras_lista) if p == palabra]

    analisis = f"[bold yellow]Palabra:[/bold yellow] '{palabra}' | " \
               f"[bold cyan]Veces encontrada:[/bold cyan] {contador} | " \
               f"[bold magenta]Posiciones:[/bold magenta] {posiciones}"
    console.print(Panel(analisis, title="🔎 Resultado Palabra", expand=False))
    guardar_historial(analisis)

# Función para guardar historial
def guardar_historial(analisis):
    historial.append(analisis)

# Función para ver historial
def ver_historial():
    if historial:
        console.print(Panel("[bold magenta]📜 HISTORIAL DE ANÁLISIS[/bold magenta]", expand=False))
        table = Table(show_header=True, header_style="bold blue")
        table.add_column("N°")
        table.add_column("Resultado")
        for i, h in enumerate(historial, 1):
            table.add_row(str(i), h)
        console.print(table)
    else:
        console.print("[red]No hay historial disponible.[/red]")

# Función para exportar resultados
def exportar_resultados():
    if not historial:
        console.print("[red]No hay resultados para exportar.[/red]")
        return

    nombre_archivo = Prompt.ask("Nombre del archivo a exportar (ej. resultados.txt) 💾")
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        for h in historial:
            f.write(f"{h}\n")
    console.print(f"[bold blue]Resultados exportados a {nombre_archivo}[/bold blue] 💾")

# ===== Loop principal =====
def main():
    texto = ""
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            texto = analizar_texto()
        elif opcion == "2":
            analizar_palabra(texto)
        elif opcion == "3":
            ver_historial()
        elif opcion == "4":
            exportar_resultados()
        elif opcion == "5":
            console.print("[bold red]¡Hasta luego![/bold red] 👋")
            break
        else:
            console.print("[red]Opción inválida. Intenta nuevamente.[/red]")

if __name__ == "__main__":
    main()