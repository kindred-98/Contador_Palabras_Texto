#!/usr/bin/env python3
"""
Punto de entrada principal.
"""

import argparse
import sys
from pathlib import Path

# Añadir raíz del proyecto para imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.text_analyzer.app import main

if __name__ == "__main__":
    main()
