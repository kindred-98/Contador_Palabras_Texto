# tests/test_gui.py

import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
import sys

from src.text_analyzer.interfaces.gui import TextAnalyzerGUI
pytestmark = pytest.mark.skip(reason="GUI tests desactivados en entorno CI")

# ===============================
# Mockear CustomTkinter y filedialog para entorno headless
# ===============================
@pytest.fixture(autouse=True)
def mock_ctk(monkeypatch):
    import customtkinter as ctk
    import tkinter.filedialog as fd

    # Mockear clases de GUI
    for cls_name in ["CTk", "CTkTextbox", "CTkLabel", "CTkFrame", "CTkButton"]:
        monkeypatch.setattr(ctk, cls_name, MagicMock())

    # Mockear diálogos de archivos
    monkeypatch.setattr(fd, "askopenfilename", lambda **kwargs: "")
    monkeypatch.setattr(fd, "asksaveasfilename", lambda **kwargs: "")

    # Mockear métodos de widgets que se usan en tests
    mock_textbox = ctk.CTkTextbox.return_value
    mock_textbox.get.return_value = ""
    mock_textbox.insert.return_value = None
    mock_textbox.delete.return_value = None


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
    app.text_input.get.return_value = "Hola mundo"

    with patch("src.text_analyzer.interfaces.gui.analyze_text") as mock_analyze, \
         patch("src.text_analyzer.interfaces.gui.format_analysis", return_value="RESULTADO FORMATEADO") as mock_format:
        mock_analyze.return_value = {"dummy": True}
        app.analizar_texto()

    app.result_box.insert.assert_called_once_with("1.0", "RESULTADO FORMATEADO")
    mock_analyze.assert_called_once_with("Hola mundo")
    mock_format.assert_called_once()


def test_analizar_texto_empty(app):
    app.text_input.get.return_value = "\n"
    app.analizar_texto()
    app.result_box.delete.assert_called_once()


def test_analizar_palabra_basic(app):
    app.text_input.get.return_value = "Python es genial"

    with patch("src.text_analyzer.interfaces.gui.analyze_single_word") as mock_word:
        mock_word.return_value = {
            "word": "Python",
            "syllables": ["Py", "thon"],
            "syllable_count": 2,
            "has_tilde": False,
            "stress_type": "Aguda"
        }
        app.analizar_palabra()

    inserted_text = "\n".join([
        "🧠 ANÁLISIS LINGÜÍSTICO\n",
        "Palabra: Python",
        "Sílabas: Py-thon",
        "Número de sílabas: 2",
        "Tiene tilde: No",
        "Tipo de palabra: Aguda"
    ])
    app.result_box.insert.assert_called_once_with("1.0", inserted_text)


def test_analizar_palabra_empty(app):
    app.text_input.get.return_value = "\n"
    app.analizar_palabra()
    app.result_box.delete.assert_called_once()


# ===============================
# Test Cargar archivo
# ===============================
def test_cargar_archivo(monkeypatch, app, tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("Contenido de prueba")

    monkeypatch.setattr(
        "src.text_analyzer.interfaces.gui.filedialog.askopenfilename",
        lambda **kwargs: str(file_path)
    )

    app.cargar_archivo()
    app.text_input.delete.assert_called()
    app.text_input.insert.assert_called_once_with("1.0", "Contenido de prueba")


# ===============================
# Test Exportar
# ===============================
def test_exportar(monkeypatch, app, tmp_path):
    save_file = tmp_path / "export.txt"

    monkeypatch.setattr(
        "src.text_analyzer.interfaces.gui.filedialog.asksaveasfilename",
        lambda **kwargs: str(save_file)
    )

    app.result_box.get.return_value = "Texto a exportar"
    app.exportar()

    # El archivo debería existir y contener el texto
    assert save_file.exists()
    content = save_file.read_text().strip()
    assert content == "Texto a exportar"


# ===============================
# Test botón salir no rompe
# ===============================
def test_salir_button(monkeypatch, app):
    called = {}

    def fake_exit():
        called["exit"] = True
        return None

    monkeypatch.setattr(sys, "exit", fake_exit)

    # Llamamos al handler de cerrar ventana
    app.exit_handler()

    assert called.get("exit") is True

    