# src/text_analyzer/core/analyzer.py

"""
Motor principal del análisis de texto. Orquesta utils para devolver AnalysisResult.
No conoce de archivos, CLI, GUI - solo texto puro -> resultados.
"""

from collections import Counter
from typing import List, Tuple

from .models import AnalysisResult, AnalysisConfig
from .utils import (
    normalize_text,
    extract_words,
    count_sentences,
    count_paragraphs,
    count_characters
)


def analyze_text(text: str, config: AnalysisConfig | None = None) -> AnalysisResult:
    """
    Función principal: texto -> AnalysisResult completo.
    
    1. Validar texto no vacío
    2. Normalizar texto
    3. Calcular todas las métricas usando utils
    4. Construir Counter de palabras
    5. Generar top palabras
    6. Crear y devolver AnalysisResult
    """
    if config is None:
        config = AnalysisConfig()
    
    # Validar texto no vacío
    raw_text_stripped = text.strip()
    if not raw_text_stripped:
        raise ValueError("No se puede analizar texto vacío")
    
    # 1. Normalizar texto
    normalized_text = normalize_text(text, config)
    
    # 2. Calcular métricas básicas
    total_chars, chars_no_spaces = count_characters(text)
    words = extract_words(normalized_text, config)
    
    # 3. Counter para frecuencias de palabras
    word_frequencies = Counter(words)
    
    # 4. Top palabras según config
    most_common_words = word_frequencies.most_common(config.top_n)
    
    # 5. Métricas de estructura
    num_sentences = count_sentences(text)
    num_paragraphs = count_paragraphs(text)
    
    # 6. Detectar advertencias
    errors = []
    if not words:
        errors.append("No se encontraron palabras válidas (todas < min_word_length)")
    
    # 7. Crear resultado inmutable
    return AnalysisResult(
        raw_text=text,
        normalized_text=normalized_text,
        num_characters=total_chars,
        num_characters_no_spaces=chars_no_spaces,
        num_words=len(words),
        num_sentences=num_sentences,
        num_paragraphs=num_paragraphs,
        word_frequencies=word_frequencies,
        most_common_words=most_common_words,
        config=config,
        errors=errors
    )


def get_top_words_analysis(result: AnalysisResult, n: int = 5) -> List[Tuple[str, int]]:
    """
    Extrae las N palabras más frecuentes del resultado.
    
    Convenience function para mostrar resúmenes rápidos.
    """
    return result.word_frequencies.most_common(n)
