# src/text_analyzer/app.py

"""
Punto de entrada principal. CLI por defecto, GUI con --gui.
"""

import sys
import argparse
from pathlib import Path

from text_analyzer.interfaces.cli import run_cli
from text_analyzer.interfaces.gui import run_gui


def main():
    parser = argparse.ArgumentParser(description="🚀 Analizador de Texto Profesional")
    parser.add_argument("--gui", action="store_true", help="Ejecutar interfaz gráfica")
    
    args = parser.parse_args()
    
    if args.gui:
        from text_analyzer.interfaces.gui import run_gui
        run_gui()
    else:
        from text_analyzer.interfaces.cli import run_cli
        run_cli()


if __name__ == "__main__":
    main()
