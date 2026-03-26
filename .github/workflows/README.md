# GitHub Actions Workflows

Documentación completa de los workflows de CI/CD del proyecto.

## 📋 Workflows disponibles

### 1. Tests y Cobertura (`tests.yml`)

**Desencadenadores:**
- `push` a `main` o `develop`
- `pull_request` a `main` o `develop`

**¿Qué hace?**
- Ejecuta la suite de tests en Python 3.10, 3.11, 3.12 y 3.13
- Genera reportes de cobertura con `pytest-cov`
- Sube los reportes a Codecov
- Comenta automáticamente en PRs con los resultados

**Matrix Strategy:**
- Ejecuta jobs en paralelo para cada versión de Python
- Si un job falla, otros continúan (`fail-fast: false`)

**Pasos principales:**
1. Checkout del código
2. Setup de Python con la versión especificada
3. Caché de dependencias pip
4. Instalación de dependencias
5. Ejecución de tests con cobertura
6. Upload a Codecov
7. Comentario automático en PR (solo PRs)

**Salida:**
```
Coverage XML → Codecov
Coverage Term → Logs de GitHub Actions
```

---

### 2. Linting y Análisis (`linting.yml`)

**Desencadenadores:**
- `push` a `main` o `develop`
- `pull_request` a `main` o `develop`

**¿Qué hace?**
- Valida el formato del código con Black
- Verifica el orden de imports con isort
- Análisis estático con flake8
- Type checking con mypy
- Análisis de seguridad con bandit

**Python Version:**
- Solo Python 3.11 (para mantener velocidad)

**Pasos principales:**
1. Setup de Python
2. Instalación de herramientas de linting
3. Validación Black
4. Validación isort
5. Análisis flake8
6. Type checking mypy
7. Análisis de seguridad bandit

**Configuración:**
- Todos los pasos tienen `continue-on-error: true`
- Esto permite que el workflow termine exitosamente aunque haya warnings

---

## 🔧 Configuración de Codecov

Para habilitar reportes de cobertura en Codecov:

1. Ve a https://codecov.io
2. Conecta tu repositorio de GitHub
3. Los reportes se subirán automáticamente desde el workflow

---

## 📊 Badges para el README

Puedes agregar estos badges en tu README para mostrar el estado de los workflows:

```markdown
[![Tests](https://github.com/tu-usuario/Contador_Palabras_Texto/actions/workflows/tests.yml/badge.svg)](https://github.com/tu-usuario/Contador_Palabras_Texto/actions/workflows/tests.yml)
[![Linting](https://github.com/tu-usuario/Contador_Palabras_Texto/actions/workflows/linting.yml/badge.svg)](https://github.com/tu-usuario/Contador_Palabras_Texto/actions/workflows/linting.yml)
```

---

## 🆘 Troubleshooting

### Los tests fallan localmente pero pasan en GitHub Actions

Verifica:
- Que tengas la misma versión de Python
- Que hayas instalado todas las dependencias: `pip install -r requirements.txt`
- Variables de entorno diferentes

### La cobertura reportada es diferente

Posibles causas:
- Diferentes plataformas (Linux en Actions vs tu SO local)
- Archivo `.coveragerc` no configurado igual
- Versiones diferentes de pytest-cov

### Codecov no recibe reportes

Verifica:
- Que hayas conectado tu repo en codecov.io
- El archivo `coverage.xml` se genera correctamente
- No hay errores en el paso "Upload coverage to Codecov"

---

## ✏️ Personalización

### Cambiar ramas desencadenadoras

En `on.push.branches` y `on.pull_request.branches`:

```yaml
on:
  push:
    branches: [ main, develop, staging ]  # Agregar 'staging'
```

### Agregar más versiones de Python

En `strategy.matrix.python-version`:

```yaml
python-version: ['3.9', '3.10', '3.11', '3.12', '3.13']
```

### Cambiar el mensaje de PR

En `jobs.test.steps.Comment PR with test results`:

```yaml
body: |
  Tu mensaje personalizado aquí
  Con múltiples líneas
```

### Ejecutar solo en cambios específicos

```yaml
on:
  push:
    branches: [ main ]
    paths:
      - 'src/**'
      - 'test/**'
      - 'requirements.txt'
```

---

## 📚 Referencias

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [pytest-cov](https://pytest-cov.readthedocs.io/)
- [Codecov](https://codecov.io/)
- [Black](https://black.readthedocs.io/)
- [flake8](https://flake8.pycqa.org/)
- [mypy](https://www.mypy-lang.org/)
- [bandit](https://bandit.readthedocs.io/)
