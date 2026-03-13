# tests/test_gui.py

import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path

from src.text_analyzer.interfaces.gui import TextAnalyzerGUI


# ===============================
# Fixture para la GUI
# ===============================

@pytest.fixture
def app():
    gui = TextAnalyzerGUI()
    yield gui
    gui.destroy()


# ===============================
# Pruebas de Text Input y Análisis
# ===============================

def test_analizar_texto_basic(app):
    # Insertamos texto simulado
    app.text_input.insert("1.0", "Hola mundo")
    
    # Patch a analyze_text y format_analysis
    with patch("src.text_analyzer.interfaces.gui.analyze_text") as mock_analyze, \
         patch("src.text_analyzer.interfaces.gui.format_analysis", return_value="RESULTADO FORMATEADO") as mock_format:
        mock_analyze.return_value = {"dummy": True}
        app.analizar_texto()
    
    content = app.result_box.get("1.0", "end")
    assert "RESULTADO FORMATEADO" in content
    mock_analyze.assert_called_once_with("Hola mundo")
    mock_format.assert_called_once()


def test_analizar_texto_empty(app):
    app.text_input.delete("1.0", "end")  # aseguramos que está vacío
    # No debe levantar error
    app.analizar_texto()
    content = app.result_box.get("1.0", "end")
    assert content == ""


def test_analizar_palabra_basic(app):
    app.text_input.insert("1.0", "Python es genial")
    
    with patch("src.text_analyzer.interfaces.gui.analyze_single_word") as mock_word:
        mock_word.return_value = {
            "word": "Python",
            "syllables": ["Py", "thon"],
            "syllable_count": 2,
            "has_tilde": False,
            "stress_type": "Aguda"
        }
        app.analizar_palabra()
    
    content = app.result_box.get("1.0", "end")
    assert "Python" in content
    assert "Sílabas: Py-thon" in content


def test_analizar_palabra_empty(app):
    app.text_input.delete("1.0", "end")
    # Debe mostrar advertencia pero no levantar error
    app.analizar_palabra()
    content = app.result_box.get("1.0", "end")
    assert content == ""


# ===============================
# Test Cargar archivo
# ===============================

def test_cargar_archivo(monkeypatch, app, tmp_path):
    # Creamos archivo de prueba
    file_path = tmp_path / "test.txt"
    file_path.write_text("Contenido de prueba")

    # Patch de filedialog.askopenfilename
    monkeypatch.setattr(
        "src.text_analyzer.interfaces.gui.filedialog.askopenfilename",
        lambda **kwargs: str(file_path)
    )

    app.cargar_archivo()
    content = app.text_input.get("1.0", "end")
    assert "Contenido de prueba" in content


# ===============================
# Test Exportar
# ===============================

def test_exportar(monkeypatch, app, tmp_path):
    app.result_box.insert("1.0", "Texto a exportar")

    save_file = tmp_path / "export.txt"

    monkeypatch.setattr(
        "src.text_analyzer.interfaces.gui.filedialog.asksaveasfilename",
        lambda **kwargs: str(save_file)
    )

    app.exportar()
    # Verificamos que el archivo se creó y contiene el texto
    assert save_file.exists()
    content = save_file.read_text()
    assert content == "Texto a exportar"


# ===============================
# Test botón salir no rompe
# ===============================

def test_salir_button(monkeypatch, app):
    # Patch sys.exit para no cerrar realmente
    monkeypatch.setattr("sys.exit", lambda: "exit_called")
    result = app.protocol("WM_DELETE_WINDOW")()
    assert result == "exit_called"