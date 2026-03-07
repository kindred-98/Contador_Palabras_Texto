# src/text_analyzer/interfaces/cli.py

"""
Interfaz de línea de comandos interactiva.
Orquesta input_handler, analyzer y file_loader sin lógica de negocio.
"""

import sys
from pathlib import Path
from typing import Dict

from ..core.models import AnalysisConfig, AnalysisResult, FileAnalysisContext
from ..core.analyzer import analyze_text
from ..io.file_loader import read_text_file, write_text_file, analyze_file
from ..io.input_handler import (
    prompt_menu_option, 
    capture_multiline_text, 
    prompt_file_path, 
    prompt_save_report,
    prompt_config
)


def format_analysis_report(result: AnalysisResult) -> str:
    """Genera informe legible para mostrar/guardar."""
    lines = [f"📊 ANÁLISIS DE TEXTO - {len(result.raw_text)} caracteres"]
    lines.append("=" * 60)
    
    lines.extend([
        f"📈 CARACTERES: {result.num_characters:,} (sin espacios: {result.num_characters_no_spaces:,})",
        f"📝 PALABRAS: {result.num_words:,}",
        f"📜 ORACIONES: {result.num_sentences:,}",
        f"📑 PÁRRAFOS: {result.num_paragraphs:,}",
    ])
    
    if result.errors:
        lines.append(f"⚠️  ADVERTENCIAS: {', '.join(result.errors)}")
    
    lines.append("\n🏆 TOP {0} PALABRAS MÁS FRECUENTES:".format(len(result.most_common_words)))
    lines.append("-" * 40)
    for i, (word, count) in enumerate(result.most_common_words, 1):
        lines.append(f"  {i:2d}. {word:<15} → {count:3d} veces")
    
    return "\n".join(lines)


def run_cli() -> None:
    """Flujo principal de la CLI interactiva."""
    print("🚀 ANALIZADOR DE TEXTO PROFESIONAL")
    print("=====================================")
    
    # 1. Configuración opcional
    config = prompt_config()
    
    # 2. Menú de entrada
    options: Dict[str, str] = {
        "1": "Texto manual (multilínea)",
        "2": "Archivo .txt"
    }
    choice = prompt_menu_option(options)
    
    text_or_path: str = ""
    result: AnalysisResult | None = None
    
    if choice == "1":
        # Texto manual
        text_or_path = capture_multiline_text()
        result = analyze_text(text_or_path, config)
        
    else:  # "2"
        # Archivo
        file_path = prompt_file_path()
        file_context = analyze_file(file_path, config)
        
        if file_context.read_error:
            print(f"❌ ERROR: {file_context.read_error}")
            sys.exit(1)
        
        result = file_context.result  # type: ignore
    
    # 3. Mostrar resultados
    assert result is not None
    report = format_analysis_report(result)
    print("\n" + report)
    
    # 4. Guardar opcional
    save, path = prompt_save_report("analisis_resultado.txt")
    if save:
        try:
            write_text_file(path, report)
            print(f"💾 Informe guardado en: {Path(path).absolute()}")
        except Exception as e:
            print(f"❌ Error guardando: {e}")


if __name__ == "__main__":
    run_cli()
