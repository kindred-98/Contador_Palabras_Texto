# 🧪 Fase 7 — Documentación de Tests

Registro completo del proceso de pruebas de **Text Analyzer**: decisiones, incidencias, soluciones y aprendizajes.

---

## 📌 Objetivo

Documentar exhaustivamente el proceso de testing, incluyendo:

- Decisiones del desarrollador y acuerdos o desacuerdos con la IA
- Incidencias encontradas
- Prompts utilizados y respuestas obtenidas
- Soluciones implementadas
- Recomendaciones aceptadas y rechazadas
- Flujo del proceso de testeo paso a paso

---

## 1. Decisiones del desarrollador

| Decisión | Descripción | Aprobada por IA |
|---|---|:---:|
| Mantener estructura original del GUI | No modificar lógica ni interfaz principal, solo corregir errores de test | ✅ |
| Mockear todos los widgets de CustomTkinter | Evitar errores de Tcl/Tk en entornos headless | ✅ |
| No modificar funcionalidad de exportar archivos | Se mantiene la escritura real en disco para verificar contenido | ✅ |
| Evitar cambios globales en el código de análisis | Mantener `analizar_texto` y `analizar_palabra` intactas | ✅ |
| No usar try/except en GUI para tests | Se prefiere mocking a cambios en la lógica real | ✅ |

---

## 2. Incidencias encontradas

### 🔴 Errores de Tkinter en entorno headless

```
_tkinter.TclError: Can't find a usable init.tcl
_tkinter.TclError: invalid command name "tcl_findLibrary"
```

**Solución:** mock completo de `customtkinter.CTk`, `CTkTextbox`, `CTkLabel`, `CTkFrame`, `CTkButton` y `filedialog`.

---

### 🔴 Errores en tests de exporter

```
TypeError: use setattr(target, name, value)
```

**Solución:** ajustar el patching para usar `monkeypatch.setattr` correctamente y no interferir con clases reales.

---

### 🔴 Fallas de contenido en tests GUI

Los textos en `TextBox` traían `\n` al final, causando fallos en comparaciones.

**Solución:** aplicar `.rstrip()` al obtener el contenido en `exportar` y mockear `get()` para simular el retorno esperado.

---

## 3. Prompts y respuestas de la IA

| Paso | Prompt | Acción tomada |
|---|---|---|
| 1 | "Tengo errores `_tkinter.TclError` en mis tests GUI, ¿cómo arreglarlo sin cambiar el código?" | Mock completo de widgets y `filedialog` para entorno headless |
| 2 | "Quiero arreglar los tests de exporter que dan TypeError al hacer patching" | Ajuste del patching usando `monkeypatch.setattr` en lugar de patch directo |
| 3 | "Quiero que los tests de GUI no fallen por saltos de línea extra o get/insert" | Mock de métodos `get`, `insert`, `delete` de `CTkTextbox` + `.rstrip()` en exportar |
| 4 | "Genera un test completo mockeando todo CustomTkinter para que pase todo" | Archivo `test_gui.py` completo con fixtures y mocks, sin errores de Tcl/Tk |

---

## 4. Soluciones implementadas

**GUI Mocking**
- Mock de todos los widgets de CustomTkinter: `CTk`, `CTkTextbox`, `CTkLabel`, `CTkFrame`, `CTkButton`
- Mock de `filedialog.askopenfilename` y `filedialog.asksaveasfilename`

**Exporter Mocking**
- `monkeypatch.setattr` aplicado correctamente en `export_txt`, `export_json` y `export_csv`
- Se eliminó el `TypeError` causado por patching incorrecto de clases GUI

**Tests de texto**
- `.get()` simulado para cada `TextBox`
- `.insert()` y `.delete()` mockeados
- `.rstrip()` para eliminar saltos de línea y evitar fallos en comparaciones

**Botón salir**
- `exit_handler` definido con mock de `sys.exit`
- Se verificó que la función se llamara correctamente sin cerrar la sesión de tests

---

## 5. Ajustes del desarrollador

- Se aplicó `.rstrip()` en el método `exportar` del GUI para coincidir con los tests.
- No se modificó la lógica de análisis ni los paneles.
- `analizar_texto` y `analizar_palabra` quedaron intactas — solo se ajustó el mocking.

---

## 6. Recomendaciones de la IA

- Mockear **siempre todos los widgets** de CustomTkinter en tests unitarios.
- Separar **tests de GUI** de **tests de lógica/exporter** para que errores de Tcl/Tk no contaminen otros tests.
- Usar `.rstrip()` o `.strip()` en outputs de `TextBox` antes de comparar en tests.
- Mantener el código de producción intacto — los mocks viven solo en los tests.

---

## 7. Aceptación / Rechazo de cambios

| Acción | Estado | Motivo |
|---|:---:|---|
| Mock completo de GUI | ✅ Aceptado | Resuelve todos los errores de Tcl/Tk en headless |
| Ajustes en exporter | ✅ Aceptado | Elimina TypeError y mantiene exportación correcta |
| Cambios en lógica de análisis | ❌ Rechazado | No era necesario, se mantuvo el original |
| Cambios en flujo de GUI | ❌ Rechazado | Solo se mockea, no se altera la interfaz |

---

## 8. Flujo de testeo paso a paso

**Paso 1 — Mocking general**
Fixture `mock_ctk` con `MagicMock` para todos los widgets y `filedialog`. Elimina todos los errores `_tkinter.TclError`.

**Paso 2 — Tests de texto**
`test_analizar_texto_basic` y `test_analizar_texto_empty`. Verificación de llamadas a `.get()`, `.insert()` y `.delete()`.

**Paso 3 — Tests de palabra**
`test_analizar_palabra_basic` y `test_analizar_palabra_empty`. Mock de `analyze_single_word`. Verificación del texto insertado en `result_box`.

**Paso 4 — Carga de archivo**
Mock de `filedialog.askopenfilename`. Verificación de llamadas a `.delete()` e `.insert()` en `text_input`.

**Paso 5 — Exportar**
Mock de `filedialog.asksaveasfilename`. Se comprueba creación del archivo y su contenido. `.rstrip()` aplicado para evitar fallos por salto de línea.

**Paso 6 — Botón salir**
Mock de `sys.exit`. Llamada a `exit_handler` y verificación de que fue invocado.

**Paso 7 — Tests de exporter**
Corrección del patching en `export_txt`, `export_json` y `export_csv` para eliminar el `TypeError`.

---

## 9. Conclusión

Todos los tests pasan correctamente en entorno headless. Los errores de Tkinter y el `TypeError` se eliminaron mediante mocking y ajuste del patching. La lógica de producción quedó intacta y el flujo de tests está documentado paso a paso para referencia futura.
