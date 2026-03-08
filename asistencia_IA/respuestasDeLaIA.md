# RESPUESTA DEL PRIMER PROMPT.

Te resumo: tu tarea es hacer un programa de terminal en Python que analice un texto (escrito por teclado o leído de un .txt) y muestre estadísticas: palabras, caracteres, oraciones, párrafos y palabras más frecuentes, además de usar Git mientras lo desarrollas.

Te propongo una estructura de proyecto sencilla; si quieres luego te escribo el código paso a paso:

## Funcionalidades mínimas

1) Pedir al usuario si quiere:

- Escribir el texto en la terminal.
- Cargar un archivo .txt (por ejemplo pidiéndole la ruta).

2) Calcular:

+ Número de caracteres: len(texto).
- Número de palabras: len(texto.split()).
- Número de oraciones: contar ., ?, ! (por ejemplo con split o recorriendo el texto).
- Número de párrafos: contar separaciones por líneas en blanco (texto.split("\n\n")).
- Frecuencia de palabras: usando collections.Counter sobre texto.split() y sacar las más frecuentes.
- Mostrar un informe en pantalla.
- Preguntar si el usuario quiere guardar el informe en un archivo .txt y, si dice que sí, escribirlo con open("informe.txt", "w", encoding="utf-8").

3) Posible organización del código
* main():
- Muestra un pequeño menú.
- Obtiene el texto (input o archivo).
- Llama a una función analizar_texto(texto).

* analizar_texto(texto):
- Devuelve un diccionario con las estadísticas: `{"caracteres": ..., "palabras": ..., "oraciones": ..., "parrafos": ..., "frecuencias": Counter(...)}.[web:2][web:1]

* mostrar_informe(stats):
- Imprime los datos en formato legible.

* guardar_informe(stats, nombre_archivo):
Genera un texto de informe y lo guarda.

* Git (muy básico)
- git init en la carpeta del proyecto.
Cada vez que completes un paso importante:
- git add .
- git commit -m "mensaje descriptivo"

Si me dices en qué punto estás (¿ya has hecho algo de código? ¿quieres que empecemos desde cero?), te escribo el esqueleto completo del programa y lo vamos mejorando.


# RESPUESTA DEL SEGUNDO PROMPT

# 1. Objetivo del proyecto
Desarrollar una herramienta de análisis de texto que funcione por línea de comandos y que pueda tener una GUI sencilla reutilizando la misma lógica interna.
La aplicación debe: leer texto desde terminal o archivo .txt, calcular estadísticas (caracteres, palabras, oraciones, párrafos, palabras más frecuentes), mostrar un informe y permitir guardarlo.
​
# 2. Estructura de carpetas y ficheros
Basada en buenas prácticas de proyectos Python: separar lógica, interfaces (CLI/GUI), tests y documentación.

´´´

text_analyzer/
├── .gitignore
├── README.md
├── pyproject.toml (opcional, si quieres ir “pro”)
├── src/
│   └── text_analyzer/
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── models.py          # Tipos de datos, dataclasses p.ej. para resultados
│       │   ├── analyzer.py        # Lógica de análisis del texto
│       │   └── utils.py           # Funciones auxiliares (limpieza texto, validaciones)
│       ├── io/
│       │   ├── __init__.py
│       │   ├── file_loader.py     # Lectura/escritura de archivos .txt, manejo de errores
│       │   └── input_handler.py   # Entrada desde terminal, validaciones de usuario
│       ├── interfaces/
│       │   ├── __init__.py
│       │   ├── cli.py             # Interfaz de línea de comandos
│       │   └── gui.py             # Interfaz gráfica (mínima, opcional)
│       └── app.py                 # Punto de entrada común, orquesta CLI/GUI
├── tests/
│   ├── __init__.py
│   ├── test_analyzer.py           # Tests de la lógica de análisis
│   ├── test_file_loader.py        # Tests de IO (mocks, casos de error)
│   └── test_cli.py                # Tests básicos de CLI (ej., con argparse y salidas)
└── asistencia_ia/
    ├── prompts.md                 # Prompts usados con la IA
    ├── decisiones.md              # Cambios de diseño motivados por la IA
    └── incidencias.md             # Errores detectados, propuestas de la IA y correcciones
´´´ 

Esta estructura sigue la idea de src/ para el código, tests/ separados y archivos de configuración en la raíz.

# 3. Roles y responsabilidades por módulo

## 3.1. core (lógica de negocio)

### models.py:
- Definir un modelo de datos para el resultado del análisis (por ejemplo, una estructura con campos: palabras, caracteres, etc.).
​- Centralizar tipos y constantes (por ejemplo delimitadores de oraciones).

### analyzer.py:
- Funciones puras que reciben un texto y devuelven el modelo de resultados.
- Contiene la lógica de conteo (palabras, oraciones, párrafos, frecuencias) sin ninguna interacción con usuario ni consola.

### utils.py:
- Normalización de texto, limpieza, helpers para separar párrafos, etc.
- Validaciones “bajas” (por ejemplo comprobar si el texto está vacío).

## 3.2. io (entrada/salida de datos)

### file_loader.py:
- Funciones para leer archivos .txt con manejo de errores: archivo no encontrado, problemas de codificación, ruta inválida.
- Función para guardar el informe (texto) en un archivo.

### input_handler.py:
- Lectura de texto desde terminal (multi‑línea si lo quieres).
- Validación de opciones de menú, reintentos cuando el usuario mete algo incorrecto.

## 3.3. interfaces (presentación)

### cli.py:
- Implementa la experiencia de terminal: menú inicial, selección de “texto manual / archivo”, mostrar informe y preguntar si se guarda.
- Usa solo funciones de core e io; no implementa lógica de análisis propia, solo coordina.

### gui.py:
- Interfaz gráfica mínima (por ejemplo con tkinter): caja de texto, botón “Analizar”, visualización de resultados.
- Igual que la CLI, solo llama a la lógica de core, separando totalmente GUI y negocio.

### app.py:
- Punto de entrada que decide si ejecutar la CLI o la GUI, por ejemplo con un parámetro (--gui o similar).
- Contiene la función main(), que es la que se ejecuta desde terminal.

# 4. Planificación paso a paso para hoy
Pensado para que llegues a una versión completa pero sencilla antes de entregar.

### Fase 1 – Setup del proyecto y Git
Crear carpeta text_analyzer y estructura de subcarpetas vacías según el esquema.

1. Inicializar repositorio: git init.
2. Crear .gitignore con entradas básicas:
3. __pycache__/, .pytest_cache/, .venv/ o env/, archivos temporales (*.pyc, etc.).
​4. Crear README.md inicial con: descripción corta del proyecto, requisitos mínimos, instrucciones básicas para ejecutar la CLI.
5. Primer commit: estructura inicial + README + .gitignore.

### Fase 2 – Diseño de lógica de análisis (sin código, solo definición)
1. Especificar en asistencia_ia/decisiones.md cómo vas a contar:
- Qué consideras palabra (separar por espacios, manejo de puntuación).
- Qué consideras oración (puntos, signos de interrogación/exclamación).
- Qué consideras párrafo (separación por líneas en blanco).
2. Definir en models.py en papel (o comentario) el modelo de resultados: campos obligatorios que la app siempre mostrará.
3. Definir en analyzer.py qué funciones necesitas (nombre, parámetros, valor de retorno) en forma de firma/comentarios, no código.

### Fase 3 – Lógica central y tests
1. Escribir primero los tests de la lógica de análisis en tests/test_analyzer.py:
- Caso de texto simple con una oración.
- Caso con varias oraciones y párrafos.
- Caso de texto vacío.
- Verificar que las palabras más frecuentes se calculan correctamente.
2. Implementar luego las funciones en analyzer.py y utils.py hasta que los tests pasen.
3. Commit: “Implement core analyzer with tests”.

### Fase 4 – Entrada/salida (IO) y validaciones
1. Tests para file_loader.py:
- Leer archivo válido.
- Archivo no existente.
- Archivo vacío.
2. Implementar lectura con manejo de excepciones (capturar errores y devolver mensajes claros o excepciones controladas).
3. Implementar función de guardado de informe con comportamiento predecible frente a rutas inválidas.
4. Tests para input_handler.py si te da tiempo (al menos validar que las opciones del menú son correctas).
5. Commit: “Add IO layer with error handling and tests”.

### Fase 5 – Interfaz de línea de comandos (CLI)
1. Diseñar el flujo de interacción en un pequeño esquema:
- Mostrar menú.
- Preguntar origen del texto.
- Obtener texto.
- Llamar a analyzer.
- Mostrar informe.
- Preguntar si se guarda y ejecutar guardado.
2. Implementar la CLI en interfaces/cli.py, reutilizando solo funciones de core e io.
3. Crear app.py con un main() que llame a la CLI por defecto.
4. Commit: “Add CLI interface”.

### Fase 6 – GUI mínima (si tienes tiempo)
1. Diseñar una GUI muy básica en interfaces/gui.py: un textarea, un botón “Analizar”, zona de resultados.
2. Conectar los eventos para que usen las funciones de core.
3. Ampliar app.py para que acepte, por ejemplo, un argumento de línea de comandos que active la GUI.
4. Commit: “Add minimal GUI”.

### Fase 7 – Documentación y pulido final
1. Completar README.md con:
- Descripción detallada.
- Cómo instalar dependencias.
- Cómo ejecutar la app en modo CLI y GUI.
- Cómo ejecutar los tests.
2. Poner en asistencia_ia/prompts.md los prompts más relevantes usados con la IA, y en incidencias.md los errores que hayas corregido con ayuda de la IA (esto muestra bien el proceso).
3. Último commit: “Finalize documentation and clean up”.

# 5. Estrategia de validación y manejo de errores
1. Validaciones:
- No permitir continuar si el texto está vacío.
- Validar opciones de menú y repetir la pregunta en caso de entrada inválida.
- Limitar tamaño máximo del texto si lo crees necesario para evitar cuelgues.

2. Manejo de errores:

- Para archivos: capturar excepciones comunes y mostrar mensajes comprensibles (sin stacktrace al usuario).
- Separar errores “recuperables” (por ejemplo ruta incorrecta) de errores internos (bug de código).

3. Tests:
- Cubrir la lógica pura con tests unitarios.
- Testear escenarios de error en IO (archivo inexistente, etc.).

6. Flujo de trabajo con Git
- Commits pequeños y descriptivos al finalizar cada fase o sub‑tarea.
- Mensajes de commit claros: “Add analyzer tests for empty text”, “Refactor CLI menu handling”, etc.
- Etiquetas opcionales (tags) si quieres marcar una versión “entregable”.

Si quieres, el siguiente paso es que elijamos exactamente los nombres de funciones/clases en cada módulo y sus firmas, y luego ya pasamos a escribir el código siguiendo esta planificación.

# RESPUESTA DEL TERCER PROMPT 3
Buena pregunta: en realidad no hay ninguna razón para meter interfaces dentro de una carpeta llamada “errores”; fue solo un malentendido de nombres, no una buena práctica.

La idea “senior” es exactamente la que dices: todas las capas principales (core, io, interfaces) al mismo nivel dentro del paquete de src, cada una como un sub‑paquete bien separado. Quedaría así:

text_analyzer/
├── .gitignore
├── README.md
├── src/
│   └── text_analyzer/
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── models.py
│       │   ├── analyzer.py
│       │   └── utils.py
│       ├── io/
│       │   ├── __init__.py
│       │   ├── file_loader.py
│       │   └── input_handler.py
│       ├── interfaces/        # Aquí, al mismo nivel
│       │   ├── __init__.py
│       │   ├── cli.py
│       │   └── gui.py
│       └── app.py
├── tests/
│   ├── __init__.py
│   ├── test_analyzer.py
│   ├── test_file_loader.py
│   └── test_cli.py
└── asistencia_ia/
    ├── prompts.md
    ├── decisiones.md
    └── incidencias.md

- Esto respeta las recomendaciones de separar capas: lógica de dominio (core), acceso a datos/archivos (io) e interfaces de usuario (CLI/GUI) cada una en su paquete propio, dentro del paquete principal text_analyzer alojado en src/.

- Si quieres, en el siguiente mensaje definimos nombres concretos de funciones/métodos en cada módulo (solo diseño, sin código aún) para que tengas el plan totalmente cerrado antes de picar nada.

# PREGUNTAS DEL EJERCICIO

1) ¿Cómo capturo varias líneas de texto en Python hasta que el usuario pulse Enter dos veces? 

Una forma típica con input() es ir leyendo línea a línea y parar cuando el usuario introduce una línea vacía, y considerar “Enter dos veces seguidas” como “dos líneas vacías seguidas”. En pseudocódigo:

- Crear una lista lineas.
- Llevar un contador de líneas vacías seguidas.
### En un bucle:
- Leer con input().
- Si la línea está vacía:
- Incrementar el contador de vacías.
- Si ya es 2 → salir del bucle.

### Si la línea NO está vacía:
- Reiniciar el contador de vacías a 0.
- Añadir la línea a la lista
- Al final, unir las líneas con "\n".join(lineas) para obtener un solo texto.
 importante: input() solo lee una línea cada vez, así que para “multilínea” simulas el final mirando cuándo el usuario deja la línea en blanco (una o dos veces seguidas, según tus reglas).


2) ¿Cuál es la diferencia entre input() y sys.stdin.read() para capturar texto largo?

Conceptualmente:

### input():
- Lee una sola línea cada vez (hasta que el usuario pulse Enter).
- Devuelve un str.
- Es ideal para entradas interactivas paso a paso: menús, preguntas - - cortas, o multilínea simulada con un bucle.
Normalmente se usa junto con print() para hacer diálogos con el usuario.

### sys.stdin.read():
- Lee todo lo que haya en la entrada estándar de golpe (hasta EOF: fin de archivo).
- También devuelve un str, pero puede contener muchas líneas, incluso texto pegado desde un archivo.

### Es más útil cuando:
- Rediriges un archivo: python script.py < archivo.txt.
- O quieres que el usuario pegue un bloque grande y señales fin con Ctrl+D (Linux/macOS) o Ctrl+Z (Windows).
- No está pensado para interacción paso a paso, sino para “leer entrada en bloque”.

 Para tu proyecto de analizador de texto:
- Si quieres un modo interactivo “usuario escribe en consola y termina con Enter dos veces”, lo razonable es usar un bucle con input() como en el punto 1.

- Si quisieras soportar también “leer todo un bloque que se le pasa por redirección”, podrías ofrecer un modo avanzado con sys.stdin.read() que se traga todo el texto de golpe.

# RESPUESTA DEL QUINTO PROMPT
Resumen de lo que hicimos, fue creacion de funciones de core.
Texto crudo ─┐
             ├─> normalize_text() ──> normalized_text
             ├─> count_characters() ─> num_chars, num_chars_no_spaces  
             ├─> extract_words() ────> lista_palabras ──\
             │                                           ├─> Counter ──> word_frequencies
             │                                           │               └─> most_common_words  
             ├─> count_sentences() ──> num_sentences     │
             └─> count_paragraphs() ──> num_paragraphs ──┘

↓ Todos los datos ──> analyze_text() ──> AnalysisResult (inmutable)

# RESPUESTA DEL SEXTO PROMPT

cd text_analyzer
pytest tests/test_analyzer.py -v
- O con cobertura:
- pytest --cov=src/text_analyzer tests/ -v

Cobertura que garantiza estos tests:
✅ Utils individuales: cada función probada aislada
✅ Casos reales: Lorem Ipsum, español con acentos, párrafos reales
✅ Edge cases: vacío, solo espacios, configs diferentes
✅ Configuración: min_word_length, top_n, case_sensitive
✅ Regex: abreviaturas, puntuación compleja
✅ Counter: frecuencias correctas

# RESPUESTA DEL SEPTIMO PROMPT
Estado del proyecto 🎉
✅ models.py
✅ utils.py + tests
✅ analyzer.py + Counter
✅ file_loader.py + open()
✅ input_handler.py + input()
⏳ interfaces/cli.py (próximo)