# tests/test_file_loader.py

import pytest
from pathlib import Path
from src.text_analyzer.io.file_loader import (
    read_text_file,
    write_text_file,
    analyze_file,
    FileReadError,
    FileWriteError
)
from src.text_analyzer.core.models import AnalysisConfig

# ===============================
# Test read_text_file
# ===============================

def test_read_text_file_success(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("Hola mundo", encoding="utf-8")

    content = read_text_file(str(file_path))
    assert content == "Hola mundo"

def test_read_text_file_not_found(tmp_path):
    file_path = tmp_path / "no_existe.txt"
    with pytest.raises(FileReadError, match="Archivo no encontrado"):
        read_text_file(str(file_path))

def test_read_text_file_wrong_extension(tmp_path):
    file_path = tmp_path / "archivo.md"
    file_path.write_text("Contenido")
    with pytest.raises(FileReadError, match="Solo se permiten archivos"):
        read_text_file(str(file_path))

def test_read_text_file_unicode_error(tmp_path, monkeypatch):
    file_path = tmp_path / "test.txt"
    file_path.write_bytes(b"\xff\xfe\xff")  # bytes inválidos para utf-8

    # Debe intentar varios encodings y finalmente fallar
    with pytest.raises(FileReadError, match="No se pudo leer"):
        read_text_file(str(file_path))

# ===============================
# Test write_text_file
# ===============================

def test_write_text_file_success(tmp_path):
    file_path = tmp_path / "salida.txt"
    write_text_file(str(file_path), "Hola mundo")
    assert file_path.exists()
    assert file_path.read_text() == "Hola mundo"

def test_write_text_file_permission_error(tmp_path, monkeypatch):
    file_path = tmp_path / "salida.txt"

    def fake_open(*args, **kwargs):
        raise PermissionError("Simulado")

    monkeypatch.setattr("builtins.open", fake_open)

    with pytest.raises(FileWriteError, match="Error escribiendo"):
        write_text_file(str(file_path), "Contenido")

# ===============================
# Test analyze_file
# ===============================

def test_analyze_file_success(tmp_path):
    file_path = tmp_path / "texto.txt"
    file_path.write_text("Hola mundo")

    context = analyze_file(str(file_path), AnalysisConfig(top_n=1))
    assert context.result is not None
    assert context.read_error is None
    assert context.file_path.endswith("texto.txt")

def test_analyze_file_read_error(tmp_path):
    file_path = tmp_path / "no_existe.txt"

    context = analyze_file(str(file_path))
    assert context.result is None
    assert "Archivo no encontrado" in context.read_error