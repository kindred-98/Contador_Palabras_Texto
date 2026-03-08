# src/text_analyzer/core/utils.py

"""
Utilidades de procesamiento de texto puro. Funciones sin estado, puras.

Cada función tiene un propósito único y recibe/salida datos simples.
Usan: strip(), lower(), replace(), re, split() según los objetivos del proyecto.
"""

from typing import List
import re
from collections import Counter

from .models import AnalysisConfig



def normalize_text(text: str, config: AnalysisConfig) -> str:
    """
    Normaliza el texto según la configuración.

    Reglas:
    - Normaliza saltos de línea (\r\n, \r -> \n)
    - Convierte saltos de línea y tabs a espacios
    - Colapsa whitespace múltiple en un solo espacio
    - lower() si no es case_sensitive
    - strip() final
    """

    if not text:
        return ""

    # Normalizar saltos de línea
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")

    # Convertir saltos de línea y tabs en espacios
    normalized = normalized.replace("\n", " ").replace("\t", " ")

    # Colapsar cualquier whitespace múltiple en un solo espacio
    normalized = re.sub(r"\s+", " ", normalized)

    # Aplicar lower si corresponde
    if not config.case_sensitive:
        normalized = normalized.lower()

    return normalized.strip()


def extract_words(text: str, config: AnalysisConfig) -> List[str]:
    """
    Extrae palabras del texto, aplicando filtros de longitud mínima.
    
    Usa re.findall() con patrón de palabras + split() alternativo.
    Filtra palabras por config.min_word_length.
    """
    if not text:
        return []
    
    # Extraer palabras usando regex (alfanumérico + apóstrofes)
    words = re.findall(r"\b[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]{2,}\b", text)
    
    # Filtrar por longitud mínima
    words = [word for word in words if len(word) >= config.min_word_length]
    
    # lower() solo si no es case_sensitive
    if not config.case_sensitive:
        words = [word.lower() for word in words]
    
    return words


def count_sentences(text: str) -> int:
    """
    Cuenta oraciones usando regex para detectar . ? !
    
    Patrón robusto que evita contar puntos de abreviaturas comunes.
    """
    if not text or not text.strip():
        return 0
    
    # Patrón para detectar finales de oración, evitando abreviaturas comunes
    sentence_pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s'
    sentences = re.split(sentence_pattern, text)
    
    # Contar solo oraciones no vacías
    return len([s for s in sentences if s.strip()])


def count_paragraphs(text: str) -> int:
    """
    Cuenta párrafos como bloques separados por 2+ saltos de línea.
    
    Usa split("\n\n") + limpieza con strip().
    """
    if not text or not text.strip():
        return 0
    
    # Normalizar saltos de línea primero
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    
    # Dividir por párrafos (2+ líneas vacías)
    paragraphs = re.split(r'\n\s*\n', normalized)
    
    # Contar solo párrafos no vacíos
    return len([p for p in paragraphs if p.strip()])


def count_characters(text: str) -> tuple[int, int]:
    """
    Cuenta caracteres totales y sin espacios.
    
    Usa len(text) y len(re.sub(r'\s+', '', text)).
    """
    total_chars = len(text)
    chars_no_spaces = len(re.sub(r'\s+', '', text))
    return total_chars, chars_no_spaces
