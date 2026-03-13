# tests/test_cli.py

import pytest
from unittest.mock import patch

from src.text_analyzer.interfaces.cli import (
    guardar_historial,
    ver_historial,
    exportar_resultados,
    format_analysis_report
)

# ===============================
# Test historial
# ===============================

def test_guardar_historial_adds_item():
    # Inicializamos lista vacía
    historial = []

    # Patch para reemplazar lista interna del módulo
    with patch("text_analyzer.interfaces.cli.historial", historial):
        guardar_historial("resultado 1")
        guardar_historial("resultado 2")

    assert len(historial) == 2
    assert historial[0] == "resultado 1"
    assert historial[1] == "resultado 2"

def test_ver_historial_no_items(capsys):
    # Lista vacía
    with patch("text_analyzer.interfaces.cli.historial", []):
        ver_historial()

    captured = capsys.readouterr()
    assert "No hay historial disponible" in captured.out


def test_ver_historial_with_items(capsys):
    items = ["resultado A", "resultado B"]

    with patch("text_analyzer.interfaces.cli.historial", items):
        ver_historial()

    captured = capsys.readouterr()
    assert "resultado A" in captured.out
    assert "resultado B" in captured.out


# ===============================
# Test format_analysis_report
# ===============================

def test_format_analysis_report_basic():
    result = "Texto de prueba"
    assert format_analysis_report(result) == "Texto de prueba"


# ===============================
# Test exportar resultados
# ===============================

def test_exportar_results_no_last_result(capsys):
    # Sin resultado previo
    with patch("text_analyzer.interfaces.cli.ultimo_resultado", None):
        exportar_resultados()

    captured = capsys.readouterr()
    assert "Primero debes analizar un texto" in captured.out


def test_exportar_results_invalid_option(monkeypatch, tmp_path, capsys):
    # Creamos resultado simulado
    result = {"texto_original": "hola"}

    # Patch ultimo_resultado
    with patch("text_analyzer.interfaces.cli.ultimo_resultado", result):
        # Simulamos opción inválida
        monkeypatch.setattr(
            "text_analyzer.interfaces.cli.Prompt.ask",
            lambda *args, **kwargs: "9"
        )
        exportar_resultados()

    captured = capsys.readouterr()
    assert "Formato inválido" in captured.out


def test_exportar_results_txt(monkeypatch, tmp_path):
    result = {"texto_original": "hola"}

    with patch("text_analyzer.interfaces.cli.ultimo_resultado", result):
        # Forzamos export TXT
        monkeypatch.setattr(
            "text_analyzer.interfaces.cli.Prompt.ask",
            lambda *args, **kwargs: "1"
        )
        filename = None
        # Interceptamos la función export_txt
        from src.text_analyzer.io.exporter import export_txt

        def fake_export_txt(data):
            nonlocal filename
            filename = tmp_path / "export.txt"
            filename.write_text(data["texto_original"])
            return str(filename)

        monkeypatch.setattr(
            "text_analyzer.interfaces.cli.export_txt",
            fake_export_txt
        )

        exportar_resultados()

        # Validamos que se haya creado archivo
        assert filename.exists()
        content = filename.read_text()
        assert content == "hola"


# ===============================
# Test CLI completo simulado
# ===============================

def test_full_cli_flow(monkeypatch, capsys):
    # Lista de inputs simulados
    inputs = iter([
        "1",            # Analizar texto
        "Hola mundo",   # Texto
        "2",            # Analizar palabra
        "Hola",         # Palabra
        "3",            # Ver historial
        "5"             # Salir
    ])

    monkeypatch.setattr(
        "text_analyzer.interfaces.cli.Prompt.ask",
        lambda *args, **kwargs: next(inputs)
    )

    # Ejecutamos CLI hasta salir
    from src.text_analyzer.interfaces.cli import run_cli
    run_cli()

    captured = capsys.readouterr()
    assert "Analizando texto" in captured.out
    assert "Hola" in captured.out
    assert "📜 HISTORIAL" in captured.out
    assert "¡Hasta luego!" in captured.out