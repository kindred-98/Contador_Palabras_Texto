<div align="center">

<!-- ANIMATED HEADER BANNER -->
<img src="IMG/banner.gif" alt="Contador de Palabras MDL" width="100%" />

# 📊 Contador de Palabra MDL

**Herramienta de análisis lingüístico de textos desarrollada en Python**  
*Arquitectura limpia · CLI + GUI · Testing automatizado · Exportación multi-formato*

---

<!-- BADGES -->
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Tests](https://img.shields.io/badge/Tests-48%20passed-2ea44f?style=for-the-badge&logo=pytest&logoColor=white)](tests/)
[![Coverage](https://img.shields.io/badge/Coverage-88%25-brightgreen?style=for-the-badge&logo=codecov&logoColor=white)](tests/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)]()
[![Code Style](https://img.shields.io/badge/Code%20Style-Clean%20Architecture-blueviolet?style=for-the-badge)]()

</div>

---

## 📌 Índice

- [Descripción](#-descripción)
- [Demo](#-demo)
- [Características](#-características)
- [Arquitectura](#-arquitectura-del-proyecto)
- [Instalación](#-instalación)
- [Uso](#️-uso)
- [Ejemplo de análisis](#-ejemplo-de-análisis)
- [Exportación de resultados](#-exportación-de-resultados)
- [Testing](#-testing)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Tecnologías](#-tecnologías)
- [Comparativa de interfaces](#-comparativa-de-interfaces)
- [Changelog](#-changelog)
- [Autor](#-autor)
- [Licencia](#-licencia)

---

## 📖 Descripción

**Contador de Palabra MDL** es una herramienta desarrollada en Python que permite analizar textos de forma completa, obteniendo estadísticas lingüísticas detalladas y exportando los resultados en múltiples formatos.

El proyecto fue construido con foco en:

- 🏗️ **Arquitectura limpia** — separación clara por capas (`core`, `interfaces`, `io`, `storage`, `errors`)
- 🧪 **Testing robusto** — 48 tests automatizados con ~88% de cobertura
- 🖥️ **Doble interfaz** — CLI interactiva con Rich + GUI con Tkinter
- 📤 **Exportación flexible** — JSON, CSV y TXT
- 🔎 **Análisis lingüístico real** — frecuencia, estadísticas de texto y análisis por palabra

---

## 🎬 Demo

> 📸 Las capturas y GIFs del proyecto se encuentran en la carpeta `IMG/`

| CLI en acción | Interfaz GUI |
|:---:|:---:|
| ![!\[CLI\](IMG/1-Usar_CLI.png)](https://github.com/kindred-98/Contador_Palabras_Texto/blob/0019289c7f7ff51d971d84128f3d767bdcca5569/asistencia_IA/IMG/1-Usar_CLI.png) | ![!\[GUI\](IMG/GUI_Actualizado.png)](https://github.com/kindred-98/Contador_Palabras_Texto/blob/0ee6a3defc958166d8b49bc397b37093f4f3f018/asistencia_IA/IMG/GUI_Actualizado.png)|

| Pantalla de inicio |
|:---:|
| ![!\[Inicio\](IMG/0-Interfaz_De_Inicio.png)](https://github.com/kindred-98/Contador_Palabras_Texto/blob/0019289c7f7ff51d971d84128f3d767bdcca5569/asistencia_IA/IMG/0-Interfaz_De_Inicio.png) |

---

## 🚀 Características

| Funcionalidad | Descripción | Estado |
|---|---|:---:|
| Conteo de palabras | Total de palabras, caracteres, oraciones y párrafos | ✅ |
| Palabras frecuentes | Top palabras con visualización de barra | ✅ |
| Análisis lingüístico | Análisis individual por palabra | ✅ |
| Historial de análisis | Persistencia local en JSON | ✅ |
| Exportación TXT | Resultados en texto plano | ✅ |
| Exportación JSON | Datos estructurados | ✅ |
| Exportación CSV | Compatible con Excel / hojas de cálculo | ✅ |
| Interfaz CLI | Navegación interactiva con Rich | ✅ |
| Interfaz GUI | Ventana gráfica con Tkinter | ✅ |
| Sistema de logs | Registro de eventos y errores | ✅ |
| Manejo de errores | Excepciones personalizadas | ✅ |
| Tests automatizados | Suite con pytest + cobertura | ✅ |

---

## 🧠 Arquitectura del proyecto

```
┌─────────────────────────────────────────────────────────────────┐
│                     Contador de Palabra MDL                     │
│                                                                 │
│  ┌───────────────┐          ┌───────────────────────────────┐  │
│  │  Interfaces   │          │            Core               │  │
│  │               │◄────────►│                               │  │
│  │  CLI (Rich)   │          │  analyzer.py   → estadísticas │  │
│  │  GUI (Tk)     │          │  linguistic.py → por palabra  │  │
│  │               │          │  models.py     → estructuras  │  │
│  └───────────────┘          └───────────────────────────────┘  │
│          │                                  │                   │
│          ▼                                  ▼                   │
│  ┌───────────────┐          ┌───────────────────────────────┐  │
│  │      IO       │          │           Storage             │  │
│  │               │          │                               │  │
│  │  exporter     │          │  history_manager.py           │  │
│  │  file_loader  │          │  history.json                 │  │
│  │  input_handler│          │                               │  │
│  └───────────────┘          └───────────────────────────────┘  │
│                                                                 │
│  ┌──────────────────────────────┐   ┌──────────────────────┐  │
│  │           Errors             │   │        Logging       │  │
│  │  custom_exceptions.py        │   │  logger.py           │  │
│  │  error_handler.py            │   │                      │  │
│  └──────────────────────────────┘   └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📦 Instalación

### Requisitos previos

- Python 3.10 o superior
- pip

### Pasos

**1. Clonar el repositorio:**

```bash
git clone https://github.com/TU_USUARIO/Contador_Palabras_Texto.git
cd Contador_Palabras_Texto
```

**2. Crear entorno virtual:**

```bash
python -m venv .venv
```

**3. Activar entorno:**

```bash
# Windows
.venv\Scripts\activate

# Linux / Mac
source .venv/bin/activate
```

**4. Instalar dependencias:**

```bash
pip install -r requirements.txt
```

---

## ▶️ Uso

### Interfaz CLI

```bash
python -m src.text_analyzer.interfaces.cli
```

### Interfaz GUI

```bash
python -m src.text_analyzer.interfaces.gui
```

### Desde VS Code

Abre `src/main.py` y pulsa el botón **▷ Run** (esquina superior derecha).

O con atajo de teclado: `F5`

---

## 💡 Ejemplo de análisis

**Entrada:**

```
Python es increíble. Python es potente. Python es divertido.
```

**Salida:**

```
┌────────────────────────────────────┐
│         Resultados del análisis    │
├──────────────────┬─────────────────┤
│ Total palabras   │       9         │
│ Total caracteres │      55         │
│ Oraciones        │       3         │
│ Párrafos         │       1         │
│ Palabra líder    │ Python (x3)     │
└──────────────────┴─────────────────┘
```

**Tabla de frecuencia:**

```
Python    ████████████████████  3
es        █████████████         3
increíble ████                  1
potente   ████                  1
divertido ████                  1
```

---

## 💾 Exportación de resultados

Los análisis se exportan automáticamente a:

```
src/exportacionesDel_Usuario/
```

Con nombre de archivo basado en timestamp:

```
analysis_20260315_183000.json
analysis_20260315_183000.csv
analysis_20260315_183000.txt
```

### Ejemplo de salida JSON

```json
{
  "timestamp": "2026-03-15T18:30:00",
  "total_words": 9,
  "total_characters": 55,
  "sentences": 3,
  "paragraphs": 1,
  "top_words": [
    { "word": "Python", "count": 3 },
    { "word": "es", "count": 3 }
  ]
}
```

---

## 🧪 Testing

El proyecto incluye una suite completa de tests automatizados con **pytest**.

**Ejecutar todos los tests:**

```bash
pytest
```

**Con reporte de cobertura:**

```bash
pytest --cov
```

**Con reporte HTML:**

```bash
pytest --cov --cov-report=html
```

**Resultados actuales:**

```
==================== test session starts ====================

tests/test_analyzer.py      ..........   PASSED
tests/test_cli.py           ..........   PASSED
tests/test_exporter.py      ..........   PASSED
tests/test_file_loader.py   ..........   PASSED
tests/test_gui.py           ..........   PASSED

============== 48 passed in 1.23s ==============

---------- coverage: 88% ----------
```

---

## 📂 Estructura del proyecto

```
Contador_Palabras_Texto/
│
├── src/
│   ├── text_analyzer/
│   │   ├── core/
│   │   │   ├── analyzer.py          # Lógica principal de análisis
│   │   │   ├── linguistic.py        # Análisis lingüístico por palabra
│   │   │   └── models.py            # Modelos de datos
│   │   │
│   │   ├── interfaces/
│   │   │   ├── cli.py               # Interfaz de línea de comandos
│   │   │   ├── gui.py               # Interfaz gráfica (Tkinter)
│   │   │   └── gui_formatter.py     # Formateador para GUI
│   │   │
│   │   ├── io/
│   │   │   ├── exporter.py          # Exportación JSON / CSV / TXT
│   │   │   ├── file_loader.py       # Carga de archivos externos
│   │   │   └── input_handler.py     # Gestión de entradas del usuario
│   │   │
│   │   ├── storage/
│   │   │   ├── history_manager.py   # Gestión del historial
│   │   │   └── history.json         # Historial persistente
│   │   │
│   │   ├── errors/
│   │   │   ├── custom_exceptions.py # Excepciones personalizadas
│   │   │   └── error_handler.py     # Manejador centralizado de errores
│   │   │
│   │   └── login/
│   │       └── logger.py            # Sistema de logs
│   │
│   └── exportacionesDel_Usuario/    # Resultados exportados por el usuario
│
├── tests/
│   ├── test_analyzer.py
│   ├── test_cli.py
│   ├── test_exporter.py
│   ├── test_file_loader.py
│   └── test_gui.py
│
├── IMG/                             # Capturas, GIFs y diagrama de arquitectura
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🔁 Comparativa de interfaces

| Característica | CLI | GUI |
|---|:---:|:---:|
| Análisis de texto | ✅ | ✅ |
| Tabla de frecuencia | ✅ | ✅ |
| Historial de análisis | ✅ | ✅ |
| Exportación de resultados | ✅ | ✅ |
| Coloreado / formato visual | ✅ Rich | ✅ Tkinter |
| Sin dependencia de ventana | ✅ | ❌ |
| Apto para scripts / automatización | ✅ | ❌ |
| Experiencia visual amigable | ⚠️ | ✅ |

---

## 🛠 Tecnologías

| Tecnología | Uso |
|---|---|
| [Python 3.10+](https://python.org) | Lenguaje principal |
| [Rich](https://github.com/Textualize/rich) | Formato y color en CLI |
| [Tkinter](https://docs.python.org/3/library/tkinter.html) | Interfaz gráfica |
| [Pytest](https://pytest.org) | Framework de testing |
| [Pytest-cov](https://github.com/pytest-dev/pytest-cov) | Cobertura de tests |

---

## 📋 Changelog

### v1.0.0 — 2026-03-15
- 🎉 Release inicial del proyecto
- ✅ Análisis completo de texto (palabras, caracteres, oraciones, párrafos)
- ✅ Tabla de frecuencia con visualización en barra
- ✅ Análisis lingüístico de palabras individuales
- ✅ Historial de análisis persistente
- ✅ Exportación a JSON, CSV y TXT
- ✅ Interfaz CLI interactiva con Rich
- ✅ Interfaz GUI con Tkinter
- ✅ Suite de 48 tests automatizados (~88% cobertura)
- ✅ Sistema de logs y manejo de errores personalizado

---

## 👨‍💻 Autor

<div align="center">

**MDL**

*Proyecto educativo enfocado en arquitectura limpia, testing automatizado y separación por capas en Python.*

[![GitHub](https://img.shields.io/badge/GitHub-@TU_USUARIO-181717?style=for-the-badge&logo=github)](https://github.com/kindred-98/Contador_Palabras_Texto.git)

</div>

---

## 📜 Licencia

Este proyecto está bajo licencia **MIT**.  
Consulta el archivo [LICENSE](LICENSE) para más información.

---

<div align="center">

*Hecho con 🐍 Python y arquitectura limpia*

⭐ Si este proyecto te resulta útil, considera dejarle una estrella en GitHub

</div>
