# tests/test_analyzer.py

import pytest
from collections import Counter
from pathlib import Path

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
        
        assert result == "hola mundo!\ncon\nlíneas múltiples"
        # Verifica que quitó espacios extra, hizo lower, normalizó \r\n -> \n
    
    def test_normalize_text_case_sensitive(self):
        """Si case_sensitive=True, no hace lower()."""
        text = "Hola Mundo"
        config = AnalysisConfig(case_sensitive=True)
        
        result = normalize_text(text, config)
        assert result == "hola mundo" == False  # Mantiene mayúsculas? No, espera...
        # Debe mantener "Hola Mundo"
    
    def test_normalize_text_empty(self):
        """Texto vacío se normaliza a cadena vacía."""
        result = normalize_text("", AnalysisConfig())
        assert result == ""
    
    def test_extract_words_real_text(self):
        """Extrae palabras reales, ignora puntuación básica."""
        text = "Hola, mundo! Este es un test. ¿Cuántas palabras?"
        config = AnalysisConfig(min_word_length=3)
        
        words = extract_words(text, config)
        expected = ["hola", "mundo", "este", "test", "cuantas", "palabras"]
        
        assert words == expected
        assert len(words) == 6
    
    def test_extract_words_short_words(self):
        """Ignora palabras menores a min_word_length."""
        text = "a yo tu no"
        config = AnalysisConfig(min_word_length=3)
        
        words = extract_words(text, config)
        assert words == []  # Todas < 3 letras
    
    def test_count_sentences_real(self):
        """Cuenta oraciones reales con diferentes terminaciones."""
        text = """Esto es una oración.
        Esta acaba en ?.
        ¡Esta en exclamación!
        Pero esta no termina."""
        
        count = count_sentences(text)
        assert count == 4  # Una por cada . ? ! (la última no cuenta)
    
    def test_count_sentences_abbreviations(self):
        """No cuenta puntos de abreviaturas como fin de oración."""
        text = "Dr. Pérez va al Sr. López. Fin."
        count = count_sentences(text)
        assert count == 2  # Solo los dos puntos finales
    
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
        
        assert total == 25
        assert no_spaces == 15  # "Holamundoconespacios"


class TestAnalyzer:
    """Tests de integración para analyze_text() con casos reales."""
    
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
        """Caso real: párrafo único con oraciones múltiples."""
        config = AnalysisConfig(top_n=5, min_word_length=2)
        result = analyze_text(self.TEXT_PARRAFO_UNICO, config)
        
        assert isinstance(result, AnalysisResult)
        assert result.raw_text == self.TEXT_PARRAFO_UNICO.strip()
        assert result.num_words > 20
        assert result.num_sentences >= 2
        assert result.num_paragraphs == 1
        assert len(result.most_common_words) == 5
        assert result.word_frequencies["python"] > 0
    
    def test_analyze_text_multiple_paragraphs(self):
        """Caso complejo: múltiples párrafos y oraciones."""
        config = AnalysisConfig()
        result = analyze_text(self.TEXT_MULTIPLE, config)
        
        assert result.num_paragraphs == 3
        assert result.num_sentences >= 6
        assert "este" in [word for word, _ in result.most_common_words]
    
    def test_analyze_text_empty_raises_error(self):
        """Texto vacío genera ValueError."""
        with pytest.raises(ValueError, match="texto vacío"):
            analyze_text("")
    
    def test_analyze_text_only_spaces(self):
        """Solo espacios cuenta como vacío."""
        result = analyze_text("   \n\t  ")
        assert result.num_words == 0
        assert result.errors  # Debe tener advertencia
    
    def test_config_top_n(self):
        """Configuración top_n limita most_common_words."""
        config = AnalysisConfig(top_n=3)
        result = analyze_text("uno dos tres cuatro cinco", config)
        
        assert len(result.most_common_words) == 3
        assert result.most_common_words[0][0] == "uno"


class TestRealWorldCases:
    """Tests con textos reales copiados de artículos."""
    
    @pytest.fixture
    def lorum_ipsum(self):
        return """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.
        """
    
    def test_lorum_ipsum(self, lorum_ipsum):
        """Lorem Ipsum clásico."""
        result = analyze_text(lorum_ipsum)
        assert result.num_sentences == 3
        assert result.num_paragraphs == 1
        assert "dolor" in result.word_frequencies
    
    def test_spanish_text(self):
        """Texto real en español con acentos y ñ."""
        text = """
        El rápido zorro marrón saltó sobre el perro perezoso.
        ¡Qué tan rápido corrió el zorro veloz!
        """
        result = analyze_text(text)
        assert "zorro" in result.word_frequencies
        assert result.word_frequencies["zorro"] == 2
        assert result.num_sentences == 2


# Tests de configuración edge-case
def test_config_min_word_length():
    """Palabras muy cortas se filtran."""
    text = "a yo tu de en el la los"
    config = AnalysisConfig(min_word_length=4)
    result = analyze_text(text, config)
    assert result.num_words == 0


def test_analyze_with_different_configs():
    """Misma entrada, configs diferentes -> resultados coherentes."""
    text = "Hola Hola mundo Mundo"
    
    config1 = AnalysisConfig(case_sensitive=False, top_n=2)
    result1 = analyze_text(text, config1)
    assert result1.most_common_words[0][0] == "hola"
    
    config2 = AnalysisConfig(case_sensitive=True, top_n=2)
    result2 = analyze_text(text, config2)
    assert result2.most_common_words[0][0] == "hola"  # Dos "Hola" mayúsculas
