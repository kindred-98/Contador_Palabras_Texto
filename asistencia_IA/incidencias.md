# FASE 0

1. La IA me ha dado la primera estructra del proyecto con una carpeta
llamada errores que dentro tenia la interfaz del proyecto.
Eso es una mala practica laboral.
Por lo tanto la e cuestionado y me ha dado otra que si tiene buena 
practica.

Nota: No todo lo que brilla es oro. 

2. Cada pregunta son texto explicativos muy a fondo en perplexity.
aveces te explica cosas demas y te sobre carga de infomacion.

3. tenemos problemas con los import.

4. problemas con los dos test. test_count_characters y test_normalize_text_basic.

# Resolución de Problemas en Tests (Pytest)

## 1. Contexto

Durante el desarrollo del **Analizador de Texto Profesional**, se implementaron **tests automatizados con pytest** para verificar el correcto funcionamiento de las funciones principales del sistema.

Los tests cubren:

* normalización de texto
* extracción de palabras
* conteo de oraciones
* conteo de párrafos
* conteo de caracteres
* análisis completo de texto

Durante la ejecución inicial de los tests se detectaron varios errores que impidieron que la suite de pruebas se ejecutara correctamente.

---

# 2. Preguntas realizadas durante la depuración

Durante la resolución del problema se plantearon las siguientes dudas técnicas:

### 2.1 Organización del proyecto

**Pregunta**

> ¿`text_analyzer` es una carpeta donde todo va dentro o `text_analyzer` y `src` son independientes?

**Conclusión**

Se confirmó que:

```
text_analyzer/ (raíz del proyecto)
│
├── src/
│   └── text_analyzer/
│
├── tests/
└── asistencia_ia/
```

* `src/` contiene el **código fuente**
* `tests/` contiene los **tests**
* `asistencia_ia/` contiene documentación sobre uso de IA

Esta estructura es común en proyectos profesionales de Python.

---

### 2.2 Error durante ejecución de pytest

**Pregunta**

> ¿Por qué pytest muestra `ERROR collecting test/test_analyzer.py`?

**Causa**

Un `assert` estaba ejecutándose **fuera de la función de test** debido a una mala indentación.

Pytest ejecuta el código del archivo al importarlo, lo que provocó un error durante la colección de tests.

---

### 2.3 Diferencia entre resultado esperado y resultado obtenido

**Pregunta**

> ¿Por qué falla el test `test_normalize_text_basic`?

Pytest mostraba:

```
AssertionError: assert 'hola mundo! \tcon líneas   múltiples'
               == 'hola mundo! con líneas múltiples'
```

El problema era que la función `normalize_text()` no estaba:

* eliminando `\t`
* eliminando saltos de línea
* colapsando espacios múltiples

---

# 3. Errores detectados en los tests

Durante la depuración se identificaron los siguientes problemas.

---

## Error 1 — Indentación incorrecta en el test

Código problemático:

```
def test_normalize_text_basic(self):

 """Texto simple"""

text = "..."
config = ...
```

El contenido del test estaba **fuera de la función**.

Esto generó:

```
ERROR collecting test/test_analyzer.py
```

---

## Error 2 — Normalización incompleta del texto

La función original `normalize_text()` hacía:

* `strip()`
* `replace("\r\n", "\n")`
* `lower()`

Pero **no manejaba correctamente**:

* tabs (`\t`)
* múltiples espacios
* saltos de línea convertidos en espacios

Esto generaba resultados como:

```
hola mundo!         con líneas   múltiples
```

Cuando el test esperaba:

```
hola mundo! con líneas múltiples
```

---

## Error 3 — Advertencia de Python sobre secuencias de escape

Pytest mostró la advertencia:

```
SyntaxWarning: "\s" is an invalid escape sequence
```

Esto ocurre cuando se usa `\s` dentro de una cadena normal.

La solución es usar **raw strings**:

```
r"\s+"
```

---

# 4. Solución implementada

Se corrigió la función `normalize_text()` aplicando una normalización completa de espacios.

Implementación final:

```
def normalize_text(text: str, config: AnalysisConfig) -> str:

    if not text:
        return ""

    normalized = text.replace("\r\n", "\n").replace("\r", "\n")

    normalized = normalized.replace("\n", " ").replace("\t", " ")

    normalized = re.sub(r"\s+", " ", normalized)

    if not config.case_sensitive:
        normalized = normalized.lower()

    return normalized.strip()
```

Esta solución:

* elimina tabs
* elimina saltos de línea
* colapsa múltiples espacios
* respeta configuración de mayúsculas/minúsculas

---

# 5. Resultado final

Después de aplicar las correcciones:

```
pytest
```

Resultado:

```
=====================
18 passed in 0.09s
=====================
```

Todos los tests pasan correctamente.

---

# 6. Aprendizajes clave

Durante la resolución del problema se reforzaron varios conceptos importantes:

### Testing

* importancia de los **tests unitarios**
* cómo pytest detecta funciones de test
* errores durante la **colección de tests**

### Limpieza de texto

uso de expresiones regulares:

```
re.sub(r"\s+", " ", text)
```

para normalizar whitespace.

### Buenas prácticas

* usar `strip()` para limpiar extremos
* usar **raw strings** para regex
* mantener funciones **puras y predecibles**

---

# 7. Estado actual del proyecto

Estado de la suite de tests:

```
18 tests
0 fallos
0 errores
1 advertencia menor
```

La aplicación y su sistema de pruebas funcionan correctamente.

---

```
====================================================================
```

5. Cuando resolvias los problemas de los test en perplexite se me quedo colgado en chat, me respondia pero solo lograba verse 2 o 3 lineas de todo lo que me habia dicho, por lo que decidi migrar a CHATGPT. Es con quien eh resuelto el problema y el documentado la incidencia de los test.
Pero todo lo antes creado en el proyecto fue con PERPLEXITY-
Es buena tiene sus ventajas y deventajas pero me abandono a mitad de camino. jajajaja

# FASE 1

Sin incidencias, todo fue integrado con exito.

# FASE 2

- Mientras me cambiaba de perplexity a chatgpt me sugerio muchos cambios lo cuales ignore. 
- Tambien me cambio el archivo creado con rich. 
- Problema: Historial no consistente entre CLI y GUI: TypeError: 'AnalysisResult' object is not subscriptable.
- Solución: función resumen_historial() para convertir objetos a string.
