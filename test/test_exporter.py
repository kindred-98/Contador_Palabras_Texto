# tests/test_exporter.py

import json
import csv
from pathlib import Path
import pytest

from src.text_analyzer.io.exporter import export_txt, export_json, export_csv

# ===============================
# Fixture de datos de prueba
# ===============================
@pytest.fixture
def sample_data():
    return {
        "texto_original": "Hola mundo",
        "num_palabras": 2,
        "num_caracteres": 10,
        "top_palabras": [("hola", 1), ("mundo", 1)]
    }

# ===============================
# Test export TXT
# ===============================
def test_export_txt(tmp_path, sample_data):
    # Sobrescribimos generate_filename para que use tmp_path
    from src.text_analyzer.io import exporter
    original_gen = exporter.generate_filename
    exporter.generate_filename = lambda prefix, ext: str(tmp_path / f"{prefix}.{ext}")

    try:
        result_file = export_txt(sample_data)
        assert Path(result_file).exists()
        content = Path(result_file).read_text(encoding="utf-8")
        assert "Hola mundo" in content
        assert "num_palabras" not in content
    finally:
        exporter.generate_filename = original_gen

# ===============================
# Test export JSON
# ===============================
def test_export_json(tmp_path, sample_data):
    from src.text_analyzer.io import exporter
    original_gen = exporter.generate_filename
    exporter.generate_filename = lambda prefix, ext: str(tmp_path / f"{prefix}.{ext}")

    try:
        result_file = export_json(sample_data)
        assert Path(result_file).exists()

        with open(result_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert data["texto_original"] == sample_data["texto_original"]
        assert data["num_palabras"] == sample_data["num_palabras"]

        expected_top = [list(x) for x in sample_data["top_palabras"]]
        assert data["top_palabras"] == expected_top
    finally:
        exporter.generate_filename = original_gen

# ===============================
# Test export CSV
# ===============================
def test_export_csv(tmp_path, sample_data):
    from src.text_analyzer.io import exporter
    original_gen = exporter.generate_filename
    exporter.generate_filename = lambda prefix, ext: str(tmp_path / f"{prefix}.{ext}")

    try:
        result_file = export_csv(sample_data)
        assert Path(result_file).exists()

        with open(result_file, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)

        # Verificamos que alguna fila tenga texto_original
        assert any(sample_data["texto_original"] in row.get("texto_original", "") for row in rows)
    finally:
        exporter.generate_filename = original_gen