# src/text_analyzer/storage/history_manager.py
import json
from pathlib import Path
from typing import Optional, Any

HISTORY_FILE = Path(__file__).parent / "history.json"

def _read_history() -> dict:
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def _write_history(data: dict) -> None:
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# --- Texto completo ---
def get_text_analysis(text: str) -> Optional[dict]:
    data = _read_history()
    return data.get("texts", {}).get(text)

def save_text_analysis(text: str, result: dict) -> None:
    data = _read_history()
    if "texts" not in data:
        data["texts"] = {}
    data["texts"][text] = result
    _write_history(data)

# --- Palabra individual ---
def get_word_analysis(word: str) -> Optional[dict]:
    data = _read_history()
    return data.get("words", {}).get(word)

def save_word_analysis(word: str, result: dict) -> None:
    data = _read_history()
    if "words" not in data:
        data["words"] = {}
    data["words"][word] = result
    _write_history(data)