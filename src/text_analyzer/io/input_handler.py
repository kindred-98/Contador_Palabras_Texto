# src/text_analyzer/io/input_handler.py

"""
Manejo de entrada interactiva del usuario en terminal.
Usa input(), strip(), lower() y validaciones robustas.
"""

from typing import Dict, List
import sys

from ..core.models import AnalysisConfig


def prompt_menu_option(options: Dict[str, str]) -> str:
    """
    Muestra menú numerado y valida opción del usuario.
    
    Args:
        options: {"1": "Texto manual", "2": "Archivo .txt"}
        
    Returns:
        Clave válida del diccionario options
    """
    while True:
        print("\n" + "="*50)
        print("SELECCIONE MODO DE ENTRADA:")
        for key, desc in options.items():
            print(f"  {key}) {desc}")
        print("="*50)
        
        choice = input("Opción (ej: 1): ").strip().lower()
        
        if choice in options:
            return choice
        print("❌ Opción inválida. Intente de nuevo.")


def capture_multiline_text() -> str:
    """
    Captura texto multilínea hasta que usuario presiona Enter DOS VECES.
    
    Usa input() en bucle + lógica de líneas vacías consecutivas.
    """
    print("\n📝 Escriba su texto (Enter dos veces para finalizar):")
    print("(Puede pegar texto multilínea)")
    
    lines: List[str] = []
    empty_lines_count = 0
    
    while True:
        try:
            line = input()
        except KeyboardInterrupt:
            print("\n\n⚠️  Operación cancelada por usuario.")
            sys.exit(0)
        
        line_stripped = line.strip()
        
        if not line_stripped:  # Línea vacía
            empty_lines_count += 1
            if empty_lines_count >= 2:
                break
        else:
            lines.append(line)
            empty_lines_count = 0
    
    return "\n".join(lines)


def prompt_file_path() -> str:
    """Pide ruta de archivo con validación básica."""
    while True:
        path = input("\n📁 Ruta del archivo .txt: ").strip()
        if path:
            return path
        print("❌ La ruta no puede estar vacía.")


def prompt_save_report(result_path: str = "analisis_resultado.txt") -> tuple[bool, str]:
    """
    Pregunta si guardar informe y en qué ruta.
    
    Returns:
        (guardar: bool, ruta: str)
    """
    choice = input(f"\n💾 ¿Guardar informe en '{result_path}'? (s/n): ").strip().lower()
    if choice in ["s", "si", "y", "yes"]:
        custom_path = input("📁 Ruta personalizada (Enter para usar default): ").strip()
        return True, custom_path if custom_path else result_path
    return False, ""


def prompt_config() -> AnalysisConfig:
    """Configuración interactiva simple del análisis."""
    print("\n⚙️  CONFIGURACIÓN (Enter para defaults):")
    top_n = input("Top palabras a mostrar (10): ").strip()
    min_len = input("Longitud mínima palabra (1): ").strip()
    
    try:
        top_n_int = int(top_n) if top_n else 10
        min_len_int = int(min_len) if min_len else 1
    except ValueError:
        print("⚠️  Usando valores por defecto.")
        top_n_int, min_len_int = 10, 1
    
    return AnalysisConfig(
        min_word_length=min_len_int,
        top_n=top_n_int,
        case_sensitive=False  # Por simplicidad, siempre False en modo interactivo
    )
