from rich.console import Console
from text_analyzer.login.logger import setup_logger

console = Console()
logger = setup_logger()


def handle_error(error: Exception):

    """
    Maneja todos los errores de la aplicación
    """

    logger.exception(f"Error detectado: {error}")

    console.print(
        f"[bold red]❌ Error:[/bold red] {str(error)}"
    )