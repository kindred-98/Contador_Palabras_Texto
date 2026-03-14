# Fase 7 – Documentación de Tests

## 1. Objetivo
Documentar exhaustivamente el proceso de pruebas de la aplicación **Text Analyzer**, incluyendo:

- Decisiones del desarrollador (Minato) y acuerdos o desacuerdos con la IA.
- Incidencias encontradas.
- Prompts utilizados.
- Soluciones implementadas.
- Ajustes realizados por el desarrollador.
- Recomendaciones de la IA.
- Aceptación o rechazo de cambios.
- Flujo del proceso de testeo (uno por uno y cambios globales).

---

## 2. Decisiones del Desarrollador
| Decisión | Descripción | Aprobada por IA |
|----------|-------------|----------------|
| Mantener estructura original del GUI | No modificar la lógica ni la interfaz principal, solo corregir errores de test. | Sí |
| Mockear todos los widgets de CustomTkinter en los tests | Evitar errores de Tcl/Tk en entornos headless. | Sí |
| No modificar funcionalidad de exportar archivos | Se mantiene la escritura real en disco para verificar contenido. | Sí |
| Evitar cambios globales en el código de análisis | Mantener funciones `analizar_texto` y `analizar_palabra` intactas. | Sí |
| No usar try/except en GUI para tests | Prefiere mocking a cambios en la lógica real. | Sí |

---

## 3. Incidencias Encontradas

1. **Errores de Tkinter en tests headless**:
   - `_tkinter.TclError: Can't find a usable init.tcl`
   - `_tkinter.TclError: invalid command name "tcl_findLibrary"`
   - Solución: mock completo de `customtkinter.CTk`, `CTkTextbox`, `CTkLabel`, `CTkFrame`, `CTkButton` y `filedialog`.

2. **Errores en tests de exporter**:
   - `TypeError: use setattr(target, name, value)` al mockear.
   - Solución: ajustar patching para usar `monkeypatch.setattr` correctamente y no interferir con clases reales.

3. **Fallas de contenido en tests GUI**:
   - Diferencias de `\n` al final de textos en `TextBox`.
   - Solución: usar `.rstrip()` al obtener contenido en exportar y mockear `get()` para simular retorno de texto esperado.

---

## 4. Prompts y Respuestas de la IA

| Paso | Prompt | Respuesta de IA / Acción |
|------|--------|-------------------------|
| 1 | “Tengo errores _tkinter.TclError en mis tests GUI, ¿cómo arreglarlo sin cambiar el código?” | Sugerencia de mock completo de widgets y filedialog para entorno headless. |
| 2 | “Quiero arreglar los tests de exporter que dan TypeError al hacer patching” | Ajuste del patching usando `monkeypatch.setattr` en lugar de patch directo, para evitar TypeError. |
| 3 | “Quiero que los tests de GUI no fallen por saltos de línea extra o get/insert” | Mockear métodos `get`, `insert`, `delete` de `CTkTextbox` y usar `.rstrip()` en exportar. |
| 4 | “Genera un test completo mockeando todo CustomTkinter para que pase todo” | Archivo `test_gui.py` completo con fixtures y mocks que elimina errores de Tcl/Tk y mantiene lógica de tests. |

---

## 5. Soluciones Implementadas

1. **GUI Mocking**:  
   - Mock de todos los widgets de `CustomTkinter` (`CTk`, `CTkTextbox`, `CTkLabel`, `CTkFrame`, `CTkButton`).  
   - Mock de `filedialog.askopenfilename` y `filedialog.asksaveasfilename`.

2. **Exporter Mocking**:
   - Uso de `monkeypatch.setattr` correctamente para funciones `export_txt`, `export_json`, `export_csv`.
   - Evitar TypeError en tests que mockeaban clases de GUI y funciones de exportación.

3. **Tests de texto**:
   - `.get()` simulado para cada TextBox.
   - `.insert()` y `.delete()` mockeados.
   - `.rstrip()` para eliminar saltos de línea al exportar y evitar fallos de comparación.

4. **Botón salir / cerrar ventana**:
   - `exit_handler` definido y mock de `sys.exit` para probar sin cerrar la sesión.
   - Se verificó que se llamara correctamente.

---

## 6. Ajustes realizados por el desarrollador

- Ajuste de `.rstrip()` en método `exportar` del GUI para coincidir con tests.
- No se modificó la lógica de análisis ni de paneles.
- Confirmación de que `analizar_texto` y `analizar_palabra` funcionan igual, solo se ajustó el mocking para tests.

---

## 7. Recomendaciones de la IA

- Mockear **siempre todos los widgets** de CustomTkinter en tests unitarios.
- Separar **tests de GUI** de **tests de lógica/exporter**, para que errores de Tcl/Tk no afecten tests de funcionalidad.
- Usar `.rstrip()` o `.strip()` en outputs de TextBox antes de comparar en tests.
- Mantener código de producción intacto, solo aplicar mocks en tests.

---

## 8. Aceptación / Rechazo

| Acción | Aceptado / Rechazado | Comentario |
|--------|--------------------|-----------|
| Mock completo GUI | Aceptado | Resuelve todos errores de Tcl/Tk en headless. |
| Ajustes en exporter | Aceptado | Evita TypeError y mantiene exportación correcta. |
| Cambios en lógica de análisis | Rechazado | No necesario, mantuvimos original. |
| Cambios en flujo de GUI | Rechazado | Solo se mockea, no se altera interfaz. |

---

## 9. Proceso de Testeo

### Paso 1 – Mocking general
- Se creó fixture `mock_ctk` con MagicMock para widgets y filedialog.
- Evita todos los errores `_tkinter.TclError`.

### Paso 2 – Tests de texto
- Test `analizar_texto_basic` y `analizar_texto_empty`.
- Verificación de llamadas a `.get()`, `.insert()`, `.delete()`.

### Paso 3 – Tests de palabra
- Test `analizar_palabra_basic` y `analizar_palabra_empty`.
- Mock de `analyze_single_word`.
- Verificación de texto insertado correctamente en `result_box`.

### Paso 4 – Test de carga de archivo
- Mock de `filedialog.askopenfilename`.
- Verificación de llamadas a `.delete()` y `.insert()` del `text_input`.

### Paso 5 – Test de exportar
- Mock de `filedialog.asksaveasfilename`.
- Se comprueba creación de archivo y contenido.
- `.rstrip()` aplicado para evitar fallos por salto de línea.

### Paso 6 – Test botón salir
- Mock de `sys.exit`.
- Llamada a `exit_handler` y verificación de que se llamó.

### Paso 7 – Tests de exporter
- Se corrigió patching en `export_txt`, `export_json` y `export_csv` para evitar TypeError.

---

## 10. Conclusión

- Todos los tests pasan correctamente en entorno headless.
- Errores de Tkinter y TypeError fueron eliminados mediante **mocking y ajustes de patching**.
- Se mantuvo la lógica de producción intacta.
- El flujo de tests quedó documentado paso a paso para referencia futura.