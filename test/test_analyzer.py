# tests/test_analyzer.py
import pytest
from collections import Counter
from pathlib import Path

from text_analyzer.core.models import (
    AnalysisConfig,
    AnalysisResult
)

from text_analyzer.core.utils import (
    normalize_text,
    extract_words,
    count_sentences,
    count_paragraphs,
    count_characters
)

from text_analyzer.core.analyzer import analyze_text


class TestUtils:
    """Tests unitarios para funciones de utilidades puras."""

    def test_normalize_text_basic(self):
        """Texto simple: strip, lower, normalización de saltos."""
        text = "  Hola Mundo!\n\tCon\r\nlíneas   múltiples  "
        config = AnalysisConfig(case_sensitive=False)

        result = normalize_text(text, config)

        assert result == "hola mundo! con líneas múltiples"

    def test_normalize_text_case_sensitive(self):
        """Si case_sensitive=True, no hace lower()."""
        text = "Hola Mundo"
        config = AnalysisConfig(case_sensitive=True)

        result = normalize_text(text, config)

        assert result == "Hola Mundo"

    def test_normalize_text_empty(self):
        """Texto vacío se normaliza a cadena vacía."""
        result = normalize_text("", AnalysisConfig())

        assert result == ""

    def test_extract_words_real_text(self):
        """Extrae palabras reales, ignora puntuación básica."""

        text = "Hola, mundo! Este es un test. ¿Cuántas palabras?"
        config = AnalysisConfig(min_word_length=3)

        words = extract_words(text, config)

        expected = ["hola", "mundo", "este", "test", "cuántas", "palabras"]

        assert words == expected
        assert len(words) == 6

    def test_extract_words_short_words(self):
        """Ignora palabras menores a min_word_length."""

        text = "a yo tu no"
        config = AnalysisConfig(min_word_length=3)

        words = extract_words(text, config)

        assert words == []

    def test_count_sentences_real(self):
        """Cuenta oraciones reales con diferentes terminaciones."""

        text = """Esto es una oración.
        Esta acaba en ?.
        ¡Esta en exclamación!
        Pero esta no termina."""

        count = count_sentences(text)

        assert count == 4

    def test_count_sentences_abbreviations(self):
        """No cuenta puntos de abreviaturas como fin de oración."""

        text = "Dr. Pérez va al Sr. López. Fin."

        count = count_sentences(text)

        assert count == 2

    def test_count_paragraphs_real(self):
        """Cuenta párrafos reales separados por líneas vacías."""

        text = """Primer párrafo con dos líneas.

        Segundo párrafo.

        Tercer párrafo con
        línea continua."""

        count = count_paragraphs(text)

        assert count == 3

    def test_count_characters(self):
        """Cuenta caracteres totales y sin espacios."""

        text = "Hola mundo  con   espacios"

        total, no_spaces = count_characters(text)

        assert total == 26
        assert no_spaces == 20


class TestAnalyzer:

    TEXT_PARRAFO_UNICO = """
    Python es un lenguaje de programación interpretado, de alto nivel y general propósito.
    Su diseño filosofía enfatiza la legibilidad del código y su sintaxis permite a los programadores expresar conceptos en pocas líneas de código.
    """

    TEXT_MULTIPLE = """
    Este es el primer párrafo.
    Termina aquí.

    Este es el segundo párrafo con dos oraciones.
    Esta es la segunda oración.

    Tercer párrafo: ¡Hola mundo!
    """

    def test_analyze_text_parrafo_unico(self):

        config = AnalysisConfig(top_n=5, min_word_length=2)

        result = analyze_text(self.TEXT_PARRAFO_UNICO, config)

        assert isinstance(result, AnalysisResult)
        assert result.num_words > 20
        assert result.num_sentences >= 2
        assert result.num_paragraphs == 1
        assert len(result.most_common_words) == 5
        assert result.word_frequencies["python"] > 0

    def test_analyze_text_multiple_paragraphs(self):

        config = AnalysisConfig()

        result = analyze_text(self.TEXT_MULTIPLE, config)

        assert result.num_paragraphs == 3
        assert result.num_sentences >= 5
        assert "este" in [word for word, _ in result.most_common_words]

    def test_analyze_text_empty_raises_error(self):

        with pytest.raises(ValueError, match="texto vacío"):
            analyze_text("")

    def test_analyze_text_only_spaces(self):

        text = "   \n\t  "

        result = analyze_text(text, AnalysisConfig())

        assert result.num_words == 0
        assert len(result.errors) > 0

    def test_config_top_n(self):

        config = AnalysisConfig(top_n=3)

        result = analyze_text("uno dos tres cuatro cinco", config)

        assert len(result.most_common_words) == 3
        assert result.most_common_words[0][0] == "uno"


class TestRealWorldCases:

    @pytest.fixture
    def lorum_ipsum(self):

        return """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.
        """

    def test_lorum_ipsum(self, lorum_ipsum):

        result = analyze_text(lorum_ipsum)

        assert result.num_sentences == 3
        assert result.num_paragraphs == 1
        assert "dolor" in result.word_frequencies

    def test_spanish_text(self):

        text = """
        El rápido zorro marrón saltó sobre el perro perezoso.
        ¡Qué tan rápido corrió el zorro veloz!
        """

        result = analyze_text(text)

        assert "zorro" in result.word_frequencies
        assert result.word_frequencies["zorro"] == 2
        assert result.num_sentences == 2


def test_config_min_word_length():

    text = "a yo tu de en el la los"

    config = AnalysisConfig(min_word_length=4)

    result = analyze_text(text, config)

    assert result.num_words == 0


def test_analyze_with_different_configs():

    text = "Hola Hola mundo Mundo"

    config1 = AnalysisConfig(case_sensitive=False, top_n=2)

    result1 = analyze_text(text, config1)

    assert result1.most_common_words[0][0] == "hola"

    config2 = AnalysisConfig(case_sensitive=True, top_n=2)

    result2 = analyze_text(text, config2)

    assert result2.most_common_words[0][0] == "Hola"