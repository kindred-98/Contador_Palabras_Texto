# src/text_analyzer/interfaces/cli.py

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.progress import track

from collections import Counter
import time

from text_analyzer.core.analyzer import analyze_single_word, analyze_text, AnalysisResult, AnalysisConfig
from text_analyzer.io.exporter import export_json, export_csv, export_txt
from text_analyzer.login.logger import setup_logger
from text_analyzer.errors.error_handler import handle_error

logger = setup_logger()
console = Console()
historial = []

# ===============================
# Almacena el último resultado como AnalysisResult real
# ===============================
ultimo_resultado: AnalysisResult | None = None

# ===============================
# MENÚ
# ===============================
def mostrar_menu():
    console.print(Panel("[bold cyan]📂 MENÚ DEL ANALIZADOR DE TEXTO[/bold cyan]", subtitle="Selecciona una opción", expand=False))
    console.print("[green]1) Analizar texto completo[/green] 📄")
    console.print("[yellow]2) Analizar palabra específica[/yellow] 🔍")
    console.print("[magenta]3) Ver historial de análisis[/magenta] 📜")
    console.print("[blue]4) Exportar resultados[/blue] 💾")
    console.print("[red]5) Salir[/red] ❌")
    return Prompt.ask("Ingresa el número de la opción")

# ===============================
# ANALIZAR TEXTO
# ===============================
def analizar_texto():
    global ultimo_resultado

    logger.info("CLI: usuario inició análisis de texto")
    texto = Prompt.ask("\nIngresa el texto a analizar 📄")

    if not texto.strip():
        logger.warning("CLI: texto ingresado vacío")
        console.print("[red]Texto vacío. Intenta de nuevo.[/red]")
        return ""

    console.print("\n[bold green]Analizando texto...[/bold green]")
    for _ in track(range(50), description="Procesando..."):
        time.sleep(0.01)

    # ===============================
    # ANALISIS REAL
    # ===============================
    config = AnalysisConfig(case_sensitive=False, min_word_length=2, top_n=10)
    result = analyze_text(texto, config=config)
    ultimo_resultado = result  # Guardamos el AnalysisResult

    # ===============================
    # Mostrar resumen con Rich
    # ===============================
    analisis_panel = (
        f"[bold green]Total palabras:[/bold green] {result.num_words} | "
        f"[bold green]Total caracteres:[/bold green] {result.num_characters} | "
        f"[bold yellow]Palabra más frecuente:[/bold yellow] "
        f"'{result.most_common_words[0][0]}' ({result.most_common_words[0][1]} veces)" if result.most_common_words else ""
    )
    console.print(Panel(analisis_panel, title="✅ Estadísticas Generales", expand=False))

    # Tabla de palabras más frecuentes
    table = Table(title="📊 Palabras más frecuentes", show_lines=True)
    table.add_column("Palabra", style="cyan", no_wrap=True)
    table.add_column("Frecuencia", style="magenta")
    table.add_column("Visual", style="green")

    max_freq = result.most_common_words[0][1] if result.most_common_words else 1
    for palabra, freq in result.most_common_words:
        bar = "█" * int((freq / max_freq) * 20)
        table.add_row(palabra, str(freq), bar)

    console.print(table)

    guardar_historial(analisis_panel)
    logger.info("CLI: análisis de texto completado")
    return texto

# ===============================
# ANALIZAR PALABRA
# ===============================
def analizar_palabra(texto):
    if not texto:
        logger.warning("CLI: intento de analizar palabra sin texto previo")
        console.print("[red]Primero debes analizar un texto completo.[/red]")
        return

    palabra = Prompt.ask("Ingresa la palabra a analizar 🔍").lower()
    logger.info(f"CLI: análisis de palabra '{palabra}'")
    palabras_lista = texto.lower().split()
    contador = palabras_lista.count(palabra)
    posiciones = [i + 1 for i, p in enumerate(palabras_lista) if p == palabra]
    linguistic = analyze_single_word(palabra)

    analisis = (
        f"[bold yellow]Palabra:[/bold yellow] '{palabra}' | "
        f"[bold cyan]Veces encontrada:[/bold cyan] {contador} | "
        f"[bold magenta]Posiciones:[/bold magenta] {posiciones}"
    )
    console.print(Panel(analisis, title="🔎 Resultado Palabra", expand=False))

    # Tabla de análisis lingüístico
    table = Table(title="🧠 Análisis Lingüístico", show_lines=True)
    table.add_column("Propiedad", style="cyan")
    table.add_column("Valor", style="green")
    table.add_row("Palabra", linguistic["word"])
    table.add_row("Sílabas", "-".join(linguistic["syllables"]))
    table.add_row("Número de sílabas", str(linguistic["syllable_count"]))
    table.add_row("Tiene tilde", "Sí" if linguistic["has_tilde"] else "No")
    table.add_row("Tipo de palabra", linguistic["stress_type"])
    console.print(table)

    guardar_historial(analisis)
    logger.info(f"CLI: análisis de palabra '{palabra}' completado")

# ===============================
# HISTORIAL
# ===============================
def guardar_historial(analisis):
    historial.append(analisis)

def ver_historial():
    logger.info("CLI: usuario consultó historial")
    if historial:
        console.print(Panel("[bold magenta]📜 HISTORIAL DE ANÁLISIS[/bold magenta]", expand=False))
        table = Table(show_header=True, header_style="bold blue")
        table.add_column("N°")
        table.add_column("Resultado")
        for i, h in enumerate(historial, 1):
            table.add_row(str(i), h)
        console.print(table)
    else:
        logger.warning("CLI: historial consultado pero está vacío")
        console.print("[red]No hay historial disponible.[/red]")

# ===============================
# EXPORTAR RESULTADOS
# ===============================
def exportar_resultados():
    if not ultimo_resultado:
        logger.warning("CLI: intento de exportar sin análisis previo")
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
        logger.warning("CLI: formato de exportación inválido")
        console.print("[red]Formato inválido[/red]")
        return

    logger.info(f"CLI: resultados exportados a {filename}")
    console.print(f"[green]Archivo exportado:[/green] {filename}")

# ===============================
# RUN CLI
# ===============================
def run_cli():
    texto = ""
    logger.info("CLI iniciado")
    while True:
        try:
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
                logger.info("CLI finalizado por el usuario")
                console.print("[bold red]¡Hasta luego![/bold red] 👋")
                break
            else:
                console.print("[red]Opción inválida.[/red]")
        except Exception as e:
            handle_error(e)