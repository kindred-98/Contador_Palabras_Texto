from collections import Counter
from text_analyzer.core.linguistic import analyze_word_linguistics
from .models import AnalysisResult, AnalysisConfig
from .utils import normalize_text, extract_words, count_sentences, count_paragraphs, count_characters
from text_analyzer.storage.history_manager import get_text_analysis, save_text_analysis, get_word_analysis, save_word_analysis

def analyze_text(text: str, config: AnalysisConfig | None = None) -> AnalysisResult:
    if config is None:
        config = AnalysisConfig()

    if not text:
        raise ValueError("No se puede analizar texto vacío")

    cached = get_text_analysis(text)
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

    save_text_analysis(text, {
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
    })

    return result

def analyze_single_word(word: str):
    if not word:
        raise ValueError("La palabra no puede estar vacía")

    cached = get_word_analysis(word)
    if cached:
        return cached

    linguistic = analyze_word_linguistics(word)
    result = {
        "word": linguistic.word,
        "syllables": linguistic.syllables,
        "syllable_count": linguistic.syllable_count,
        "has_tilde": linguistic.has_tilde,
        "stress_type": linguistic.stress_type
    }

    save_word_analysis(word, result)
    return result