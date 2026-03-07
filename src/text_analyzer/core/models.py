# src/text_analyzer/core/models.py

from __future__ import annotations

from dataclasses import dataclass
from collections import Counter
from typing import Optional


@dataclass(frozen=True)
class AnalysisConfig:
    """
    Configuración del análisis de texto.

    - min_word_length: longitud mínima de palabra para entrar en el conteo.
    - top_n: número de palabras más frecuentes que se devolverán en 'most_common_words'.
    - case_sensitive: si True, distingue mayúsculas/minúsculas en el conteo.
    """
    min_word_length: int = 1
    top_n: int = 10
    case_sensitive: bool = False


@dataclass(frozen=True)
class AnalysisResult:
    """
    Resultado detallado del análisis de un texto.

    Este modelo es inmutable para facilitar el testeo y evitar efectos laterales.
    No contiene lógica, solo datos calculados por el analizador.
    """
    # Texto
    raw_text: str                      # Texto original tal como lo introdujo el usuario
    normalized_text: str               # Texto normalizado (lower, limpieza, etc.)

    # Métricas básicas
    num_characters: int                # Total de caracteres del texto original
    num_characters_no_spaces: int      # Total de caracteres excluyendo espacios (opcional, pero útil)
    num_words: int                     # Total de palabras detectadas
    num_sentences: int                 # Total de oraciones detectadas
    num_paragraphs: int                # Total de párrafos detectados

    # Frecuencias
    word_frequencies: Counter[str]     # Frecuencia de todas las palabras (según reglas de análisis)
    most_common_words: list[tuple[str, int]]  # Lista de (palabra, frecuencia) limitada por config.top_n

    # Metadatos
    config: AnalysisConfig             # Configuración usada para generar este resultado
    errors: list[str]                  # Advertencias o errores no fatales encontrados durante el análisis


@dataclass(frozen=True)
class FileAnalysisContext:
    """
    Contexto de análisis cuando el origen es un archivo.

    Separa claramente el 'qué' (AnalysisResult) del 'de dónde' (archivo, ruta).
    Esto es útil para informes y logs.
    """
    file_path: str                     # Ruta al archivo analizado
    encoding: str                      # Codificación usada para leer el archivo
    result: AnalysisResult             # Resultado del análisis del contenido del archivo
    read_error: Optional[str] = None   # Mensaje de error si hubo problemas al leer (None si fue bien)
