from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.progress import track

from collections import Counter
import time

from text_analyzer.core.analyzer import analyze_single_word
from text_analyzer.io.exporter import export_json, export_csv, export_txt

console = Console()

historial = []

# NUEVO
ultimo_resultado = None


# ===============================
# MENÚ
# ===============================

def mostrar_menu():

    console.print(
        Panel(
            "[bold cyan]📂 MENÚ DEL ANALIZADOR DE TEXTO[/bold cyan]",
            subtitle="Selecciona una opción",
            expand=False
        )
    )

    console.print("[green]1) Analizar texto completo[/green] 📄")
    console.print("[yellow]2) Analizar palabra específica[/yellow] 🔍")
    console.print("[magenta]3) Ver historial de análisis[/magenta] 📜")
    console.print("[blue]4) Exportar resultados[/blue] 💾")
    console.print("[red]5) Salir[/red] ❌")

    opcion = Prompt.ask("Ingresa el número de la opción")

    return opcion


# ===============================
# ANALIZAR TEXTO
# ===============================

def analizar_texto():

    global ultimo_resultado

    texto = Prompt.ask("\nIngresa el texto a analizar 📄")

    console.print("\n[bold green]Analizando texto...[/bold green]")

    for _ in track(range(50), description="Procesando..."):
        time.sleep(0.01)

    palabras = texto.split()

    num_palabras = len(palabras)

    num_caracteres = len(texto)

    contador_palabras = Counter(palabras)

    palabra_mas_comun = contador_palabras.most_common(1)[0]

    analisis = (
        f"[bold green]Total palabras:[/bold green] {num_palabras} | "
        f"[bold green]Total caracteres:[/bold green] {num_caracteres} | "
        f"[bold yellow]Palabra más frecuente:[/bold yellow] "
        f"'{palabra_mas_comun[0]}' ({palabra_mas_comun[1]} veces)"
    )

    console.print(
        Panel(
            analisis,
            title="✅ Estadísticas Generales",
            expand=False
        )
    )

    table = Table(
        title="📊 Palabras más frecuentes",
        show_lines=True
    )

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

    # ===============================
    # GUARDAR RESULTADO ESTRUCTURADO
    # ===============================

    ultimo_resultado = {
        "texto_original": texto,
        "num_palabras": num_palabras,
        "num_caracteres": num_caracteres,
        "top_palabras": top_palabras
    }

    return texto


# ===============================
# ANALIZAR PALABRA
# ===============================

def analizar_palabra(texto):

    if not texto:

        console.print("[red]Primero debes analizar un texto completo.[/red]")

        return

    palabra = Prompt.ask("Ingresa la palabra a analizar 🔍").lower()

    palabras_lista = texto.lower().split()

    contador = palabras_lista.count(palabra)

    posiciones = [
        i + 1
        for i, p in enumerate(palabras_lista)
        if p == palabra
    ]

    # ANALISIS LINGÜÍSTICO

    linguistic = analyze_single_word(palabra)

    analisis = (
        f"[bold yellow]Palabra:[/bold yellow] '{palabra}' | "
        f"[bold cyan]Veces encontrada:[/bold cyan] {contador} | "
        f"[bold magenta]Posiciones:[/bold magenta] {posiciones}"
    )

    console.print(
        Panel(
            analisis,
            title="🔎 Resultado Palabra",
            expand=False
        )
    )

    table = Table(
        title="🧠 Análisis Lingüístico",
        show_lines=True
    )

    table.add_column("Propiedad", style="cyan")
    table.add_column("Valor", style="green")

    table.add_row("Palabra", linguistic["word"])
    table.add_row("Sílabas", "-".join(linguistic["syllables"]))
    table.add_row("Número de sílabas", str(linguistic["syllable_count"]))
    table.add_row("Tiene tilde", "Sí" if linguistic["has_tilde"] else "No")
    table.add_row("Tipo de palabra", linguistic["stress_type"])

    console.print(table)

    guardar_historial(analisis)


# ===============================
# HISTORIAL
# ===============================

def guardar_historial(analisis):

    historial.append(analisis)


def ver_historial():

    if historial:

        console.print(
            Panel(
                "[bold magenta]📜 HISTORIAL DE ANÁLISIS[/bold magenta]",
                expand=False
            )
        )

        table = Table(
            show_header=True,
            header_style="bold blue"
        )

        table.add_column("N°")

        table.add_column("Resultado")

        for i, h in enumerate(historial, 1):

            table.add_row(str(i), h)

        console.print(table)

    else:

        console.print("[red]No hay historial disponible.[/red]")


# ===============================
# EXPORTAR RESULTADOS
# ===============================

def exportar_resultados():

    if not ultimo_resultado:

        console.print("[red]Primero debes analizar un texto.[/red]")

        return

    console.print("\n[bold cyan]Formato de exportación[/bold cyan]")

    console.print("1) TXT")
    console.print("2) JSON")
    console.print("3) CSV")

    opcion = Prompt.ask("Selecciona formato")

    if opcion == "1":

        filename = export_txt(ultimo_resultado)

    elif opcion == "2":

        filename = export_json(ultimo_resultado)

    elif opcion == "3":

        filename = export_csv(ultimo_resultado)

    else:

        console.print("[red]Formato inválido[/red]")

        return

    console.print(f"[green]Archivo exportado:[/green] {filename}")


# ===============================
# RUN CLI
# ===============================

def run_cli():

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


# ===============================
# GUI SUPPORT
# ===============================

def format_analysis_report(result: str) -> str:
    return result