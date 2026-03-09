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

from text_analyzer.storage.history_manager import (
    get_text_analysis,
    save_text_analysis,
)

def analyze_text(text: str, config: AnalysisConfig | None = None) -> AnalysisResult:
    """
    Función principal: texto -> AnalysisResult completo.
    
    1. Validar texto no vacío
    2. Revisar si el análisis existe en historial
    3. Normalizar texto
    4. Calcular métricas
    5. Guardar resultado en historial
    """

    if config is None:
        config = AnalysisConfig()

    raw_text = text
    if not raw_text:
        raise ValueError("No se puede analizar texto vacío")

    # ===============================
    # FASE 2 — CONSULTAR HISTORIAL
    # ===============================
    cached = get_text_analysis(raw_text)

    if cached:
        return AnalysisResult(
            raw_text=cached["raw_text"],
            normalized_text=cached["normalized_text"],
            num_characters=cached["num_characters"],
            num_characters_no_spaces=cached["num_characters_no_spaces"],
            num_words=cached["num_words"],
            num_sentences=cached["num_sentences"],
            num_paragraphs=cached["num_paragraphs"],
            word_frequencies=Counter(cached["word_frequencies"]),
            most_common_words=cached["most_common_words"],
            config=config,
            errors=cached["errors"],
        )

    # ===============================
    # ANALISIS NORMAL
    # ===============================

    normalized_text = normalize_text(text, config)

    total_chars, chars_no_spaces = count_characters(text)
    words = extract_words(normalized_text, config)

    word_frequencies = Counter(words)
    most_common_words = word_frequencies.most_common(config.top_n)

    num_sentences = count_sentences(text)
    num_paragraphs = count_paragraphs(text)

    errors = []
    if not words:
        errors.append("No se encontraron palabras válidas (todas < min_word_length)")

    result = AnalysisResult(
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

    # ===============================
    # GUARDAR EN HISTORIAL
    # ===============================

    serializable_result = {
        "raw_text": result.raw_text,
        "normalized_text": result.normalized_text,
        "num_characters": result.num_characters,
        "num_characters_no_spaces": result.num_characters_no_spaces,
        "num_words": result.num_words,
        "num_sentences": result.num_sentences,
        "num_paragraphs": result.num_paragraphs,
        "word_frequencies": dict(result.word_frequencies),
        "most_common_words": result.most_common_words,
        "errors": result.errors
    }

    save_text_analysis(raw_text, serializable_result)

    return result


def get_top_words_analysis(result: AnalysisResult, n: int = 5) -> List[Tuple[str, int]]:
    """
    Extrae las N palabras más frecuentes del resultado.
    
    Convenience function para mostrar resúmenes rápidos.
    """
    return result.word_frequencies.most_common(n)