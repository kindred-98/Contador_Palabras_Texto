# tests/test_exporter.py

import json
import csv
from pathlib import Path

import pytest

from src.text_analyzer.io.exporter import export_txt, export_json, export_csv


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
    filename = tmp_path / "output.txt"

    result_file = export_txt(sample_data)

    # Verificamos que se creó un archivo
    assert Path(result_file).exists()

    # Comprobamos contenido
    content = Path(result_file).read_text()
    assert "Hola mundo" in content
    assert "num_palabras" not in content  # TXT solo incluye texto original


# ===============================
# Test export JSON
# ===============================

def test_export_json(tmp_path, sample_data):
    filename = tmp_path / "output.json"

    result_file = export_json(sample_data)

    assert Path(result_file).exists()

    with open(result_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Validamos que los datos coinciden
    assert data["texto_original"] == sample_data["texto_original"]
    assert data["num_palabras"] == sample_data["num_palabras"]
    assert data["top_palabras"] == sample_data["top_palabras"]


# ===============================
# Test export CSV
# ===============================

def test_export_csv(tmp_path, sample_data):
    filename = tmp_path / "output.csv"

    result_file = export_csv(sample_data)

    assert Path(result_file).exists()

    with open(result_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    # CSV debería tener 1 fila con las claves principales (texto_original)
    # Si tu CSV está formateado de otra forma, ajusta esta verificación
    assert any(sample_data["texto_original"] in row["texto_original"] for row in rows)