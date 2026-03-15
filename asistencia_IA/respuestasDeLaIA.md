# 🤖 Respuestas de la IA — Text Analyzer (Proyecto 2)

Registro de las respuestas más relevantes obtenidas durante el desarrollo, organizadas por fase.

---

## 🟦 Fase 0 — Planificación y base del proyecto

### Respuesta al Prompt 1 — Descripción del ejercicio

La IA resumió la tarea y propuso una estructura básica de funciones:

- `main()` — menú, obtención del texto y llamada al análisis
- `analizar_texto(texto)` — devuelve diccionario con estadísticas
- `mostrar_informe(stats)` — imprime los datos en formato legible
- `guardar_informe(stats, nombre_archivo)` — genera y guarda el informe

También propuso el flujo básico de Git: `init`, commits por cada paso y mensajes descriptivos.

---

### Respuesta al Prompt 2 — Planificación profesional

La IA propuso la siguiente estructura modular:

```
text_analyzer/
├── .gitignore
├── README.md
├── src/
│   └── text_analyzer/
│       ├── core/
│       │   ├── models.py        # Tipos de datos y resultados
│       │   ├── analyzer.py      # Lógica de análisis pura
│       │   └── utils.py         # Normalización, helpers, validaciones
│       ├── io/
│       │   ├── file_loader.py   # Lectura/escritura de archivos .txt
│       │   └── input_handler.py # Entrada desde terminal y validaciones
│       ├── interfaces/
│       │   ├── cli.py           # Interfaz de línea de comandos
│       │   └── gui.py           # Interfaz gráfica (opcional)
│       └── app.py               # Punto de entrada común CLI/GUI
├── tests/
│   ├── test_analyzer.py
│   ├── test_file_loader.py
│   └── test_cli.py
└── asistencia_ia/
    ├── prompts.md
    ├── decisiones.md
    └── incidencias.md
```

**Responsabilidades por capa:**

- `core` — lógica de negocio pura, sin interacción con usuario ni consola
- `io` — acceso a archivos y entrada de datos con manejo de errores
- `interfaces` — presentación: CLI y GUI coordinan pero no implementan lógica
- `app.py` — orquesta CLI/GUI según argumento (`--gui` o similar)

---

### Respuesta al Prompt 3 — Corrección de estructura

> *"No hay ninguna razón para meter `interfaces` dentro de una carpeta llamada `errores`. Fue un malentendido de nombres, no una buena práctica."*

La corrección fue exactamente la propuesta: `interfaces` al mismo nivel que `core` e `io` dentro de `src/text_analyzer/`.

---

### Preguntas técnicas durante el desarrollo

**¿Cómo capturo varias líneas de texto hasta que el usuario pulse Enter dos veces?**

La solución es un bucle con `input()` que lleva un contador de líneas vacías consecutivas. Al llegar a dos líneas vacías seguidas, se rompe el bucle y se une todo con `"\n".join(lineas)`. `input()` solo lee una línea a la vez — la multilínea se simula detectando cuándo el usuario deja la línea en blanco.

**¿Cuál es la diferencia entre `input()` y `sys.stdin.read()`?**

| | `input()` | `sys.stdin.read()` |
|---|---|---|
| Lee | Una línea a la vez | Todo el bloque de golpe |
| Ideal para | Interacción paso a paso, menús | Texto pegado o redirigido desde archivo |
| Fin de entrada | Enter (línea vacía) | EOF (`Ctrl+D` / `Ctrl+Z`) |

Para este proyecto se usó `input()` en bucle para el modo interactivo.

---

### Respuesta al Prompt 5 — Conexión models + utils

El flujo de datos implementado quedó así:

```
Texto crudo ─┐
             ├─> normalize_text()    ──> normalized_text
             ├─> count_characters()  ──> num_chars, num_chars_no_spaces
             ├─> extract_words()     ──> lista_palabras ──┐
             │                                            ├─> Counter ──> word_frequencies
             ├─> count_sentences()   ──> num_sentences    │             └─> most_common_words
             └─> count_paragraphs()  ──> num_paragraphs ──┘

↓ Todos los datos ──> analyze_text() ──> AnalysisResult (inmutable)
```

---

### Respuesta al Prompt 6 — Tests

Cobertura garantizada por los tests generados:

- Utils individuales: cada función probada de forma aislada
- Casos reales: Lorem Ipsum, español con acentos, párrafos reales
- Edge cases: texto vacío, solo espacios, configuraciones distintas
- Configuración: `min_word_length`, `top_n`, `case_sensitive`
- Regex: abreviaturas, puntuación compleja
- Counter: verificación de frecuencias correctas

Para ejecutar:
```bash
pytest tests/test_analyzer.py -v
pytest --cov=src/text_analyzer tests/ -v
```

---

### Respuesta al Prompt 7 — Estado tras file_loader e input_handler

```
✅ models.py
✅ utils.py + tests
✅ analyzer.py + Counter
✅ file_loader.py + open()
✅ input_handler.py + input()
⏳ interfaces/cli.py  ← siguiente paso
```

---

## 🟨 Fase 1 — CLI profesional con Rich

Lo implementado en esta fase:

- Menú interactivo con 5 opciones: Analizar texto, Analizar palabra, Ver historial, Exportar resultados, Salir
- Análisis de palabras individuales con conteo de ocurrencias y posiciones
- Historial de análisis en tabla con Rich
- Exportación de resultados a `.txt`
- Visualización con paneles, tablas, colores, emojis y barra de progreso simulada
- Tabla de frecuencia de palabras con barra visual

---

## 🟩 Fase 2 — Historial y persistencia

Lo implementado y acordado:

- `resumen_historial(h)` para convertir cualquier entrada del historial (string o `AnalysisResult`) en texto legible — esto resolvió el `TypeError` al mezclar tipos en el menú
- Historial rápido como opción 3 del menú: muestra los últimos 5 análisis en tabla Rich
- Historial compartido entre CLI y GUI — cualquier análisis de GUI aparece en la CLI

**Estado final de la Fase 2:**

| Elemento | Estado |
|---|:---:|
| `history_manager` | ✅ |
| Persistencia JSON | ✅ |
| Consulta historial | ✅ |
| Caché antes de analizar | ✅ |
| Reconstrucción de objetos | ✅ |
| Arquitectura limpia | ✅ |

---

## 🟪 Fase 3 — Análisis lingüístico

La IA generó el código y señaló exactamente qué cambiar en `analyzer.py` y `cli.py`.

**Output en terminal tras la fase:**

```
🔎 Resultado Palabra
────────────────────────────────
Palabra:           programación
Veces encontrada:  2
Posiciones:        [4, 9]

🧠 Análisis Lingüístico
────────────────────────────────
Palabra            programación
Sílabas            pro-gra-ma-ción
Número de sílabas  4
Tiene tilde        Sí
Tipo de palabra    aguda
```

**Mejoras propuestas por la IA (no aplicadas — se siguió el roadmap):**

1. Detección automática de idioma
2. Análisis de legibilidad (índice Flesch)
3. Análisis de n-gramas (bigramas y trigramas)

---

## 🟥 Fase 4 — Exportación de resultados

### Objetivo

Permitir guardar y compartir los análisis en formatos estándar: `TXT`, `JSON` y `CSV`.

### Módulo creado

```
src/text_analyzer/io/
└── exporter.py
    ├── export_txt()
    ├── export_json()
    ├── export_csv()
    └── generate_filename()   # timestamp automático → analysis_20260312_113455.csv
```

### Incidencias durante el diseño

**Problema 1:** el historial exportaba strings (`"Total palabras: 20 | Total caracteres: 120"`), datos no estructurados e imposibles de procesar en Excel o pandas.
**Solución:** guardar el resultado como estructura de datos y exportarlo como dict.

**Problema 2:** la CLI no tenía referencia al último análisis realizado.
**Solución:** variable `ultimo_resultado` que almacena el último análisis y lo pasa al exportador.

### Estructura de salida

**CSV:**
```
metric,value
num_caracteres,120
num_palabras,20

top_palabras,frecuencia
python,5
codigo,3
programacion,2
```

**JSON:**
```json
{
  "texto_original": "Python es un lenguaje...",
  "num_palabras": 20,
  "num_caracteres": 120,
  "top_palabras": [["python", 5], ["codigo", 3]]
}
```

### Decisiones de diseño acordadas

- **Separación de responsabilidades** — exportación como módulo independiente en `io/`, no dentro del CLI
- **Datos estructurados** en lugar de strings — propuesta del usuario que mejoró significativamente el diseño
- **Timestamp automático** en nombres de archivo para evitar sobrescrituras

### Estado final de la Fase 4

La aplicación incluye: CLI con Rich, GUI, análisis de texto, análisis lingüístico, historial, persistencia JSON, exportación a TXT/JSON/CSV, timestamps automáticos y arquitectura limpia por capas.

---

## ⬛ Fase 5

Documentada bajo imagen por práctica de distintos estilos de trabajo con IA.

![alt text](https://github.com/kindred-98/Contador_Palabras_Texto/blob/0ee6a3defc958166d8b49bc397b37093f4f3f018/asistencia_IA/IMG/Documentacion_FASE5.png)