# 🗒️ Devlog 

Registro del proceso de desarrollo: prompts utilizados, decisiones tomadas y evolución del proyecto fase a fase.

---

## 🟦 Fase 0 — Planificación y base del proyecto

### Descripción del ejercicio

Desarrollar un analizador de texto interactivo en terminal que permita introducir texto directamente o cargarlo desde un `.txt`, obteniendo estadísticas detalladas: palabras, caracteres, oraciones, párrafos y palabras más frecuentes. Con control de versiones en Git y asistencia de IA para generar código a analizar, comprender y modificar.

---

### Prompts utilizados

**Prompt 1 — Definición del ejercicio**
Se entregó la descripción del proyecto tal como estaba planteada en la tarea.

**Prompt 2 — Planificación antes de código**
> *"No he hecho nada, tengo que comenzar de cero pero quiero primero hacer una planificación paso a paso. Quiero estructura modularizada repartiendo responsabilidades, tests, validaciones, manejo de errores y que pueda correr en terminal o GUI. Quiero `.gitignore`, `README` y una carpeta `asistencia_ia` donde guardar los prompts usados y los fallos encontrados. No quiero código aún — quiero una planificación y estructura profesional como la haría un senior."*

**Prompt 3 — Corrección de estructura**
> *"¿Por qué en la estructura me pone la carpeta `interfaces` dentro de la carpeta `errores`? ¿Por qué no dejarla en `src` a la altura de las demás carpetas?"*

La IA había cometido un error de diseño. Se corrigió.

**Prompt 4 — Models**
> *"Comencemos con el models. Créame los models como un senior para el contador de palabras."*

**Prompt 5 — Conexión models + utils**
> *"Ahora quiero conectar los models con los utils y fírmame las funciones que devolverán estos modelos."*

**Prompt 6 — Tests**
> *"Quiero que me generes los tests como un senior con casos de prueba reales."*

**Prompt 7 — file_loader e input_handler**
> *"Créame el código de `file_loader` e `input_handler`."*

**Prompt 8 — Resolución de errores en tests**

Primero se intentó resolver los errores de tests de forma independiente, leyendo los mensajes de la terminal y aplicando el método prueba-error. Luego se recurrió a la IA con preguntas directas sobre cada error puntual: qué era, dónde estaba y por qué ocurría. Todo quedó documentado en el archivo de incidencias.

**Prompt 9 — Roadmap de evolución**

Tras tener la base funcionando, el output era este:

```
📊 ANÁLISIS DE TEXTO - 29 caracteres
=======================================
📈 CARACTERES: 29 (sin espacios: 24)
📝 PALABRAS:   5
📜 ORACIONES:  1
📑 PÁRRAFOS:   1

🏆 TOP 5 PALABRAS MÁS FRECUENTES:
----------------------------------------
1. kindred → 1 veces
2. yasuo   → 1 veces
3. son     → 1 veces
4. unos    → 1 veces
5. mmgv    → 1 veces
```

Funcionaba, pero se quería más. Se le pidió a la IA que pensara como un senior y propusiera un roadmap de evolución, considerando:

- Solo corría en terminal, sin modo de selección CLI / GUI
- La interfaz no era suficientemente legible ni interactiva
- No había análisis lingüístico por palabra (sílabas, tipo de acento, etc.)
- No había historial persistente para evitar recalcular palabras ya analizadas

El roadmap también se solicitó en formato visual.

---

## 🟨 Fase 1 — CLI profesional con Rich

Mejora de la experiencia en terminal con la librería Rich: interfaz visual, menú interactivo y navegación clara. Se usaron prompts adicionales para la exportación de resultados y la creación del script `main.py`.

---

## 🟩 Fase 2 — Historial y persistencia

- Implementación del historial persistente en JSON/SQLite con consulta desde CLI.
- Se detectó que al analizar una palabra desde GUI, el historial rompía el menú principal. Se investigó, se preguntó a la IA la causa y se corrigió.
- Se especificó el diseño exacto deseado para la pantalla de inicio de la CLI y se añadió un historial rápido visible al entrar.

---

## 🟪 Fase 3 — Análisis lingüístico

Se solicitó implementar análisis lingüístico por palabra:

- División en sílabas
- Tipo de palabra: aguda, grave, esdrújula, sobresdrújula
- Detección de tilde y número de sílabas
- Guardado del análisis lingüístico en historial

El nuevo módulo se creó fuera de `analyzer.py` para no mezclar responsabilidades.

---

## 🟥 Fase 4

Se usó el mismo prompt de la fase directamente: se pegó el enunciado completo de la Fase 4 y se pidió implementarlo tal cual.

---

## ⬛ Fase 5

> Documentada de forma diferente como práctica de distintos estilos de trabajo con IA.

![!\[Imagen Fase 5\](ChatGPT%20Image%2013%20mar%202026%2C%2001_34_00.png)](https://github.com/kindred-98/Contador_Palabras_Texto/blob/0ee6a3defc958166d8b49bc397b37093f4f3f018/asistencia_IA/IMG/Documentacion_FASE5.png)
