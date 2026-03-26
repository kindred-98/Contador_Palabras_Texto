# 🚀 Configuración de GitHub Actions - Guía Rápida

## ✅ Qué ya está hecho

He creado dos workflows automatizados para tu proyecto:

### 1. **Tests y Cobertura** 
   - Ejecuta tests en Python 3.10, 3.11, 3.12, 3.13
   - Genera reportes de cobertura
   - Comenta en pull requests

### 2. **Linting y Análisis**
   - Valida formato de código (Black)
   - Orden de imports (isort)
   - Análisis estático (flake8)
   - Type checking (mypy)
   - Análisis de seguridad (bandit)

---

## 📋 Próximos pasos

### 1️⃣ Hacer push de los cambios a GitHub

```bash
# Agrega los archivos creados
git add .github/
git add README.md

# Haz commit
git commit -m "chore: add github actions workflows"

# Push
git push origin main
```

### 2️⃣ Verificar los workflows

1. Ve a tu repositorio en GitHub
2. Abre la pestaña **Actions**
3. Deberías ver:
   - ✅ **Tests y Cobertura** - ejecutándose
   - ✅ **Linting y Análisis** - ejecutándose

### 3️⃣ (Opcional) Configurar Codecov

Si quieres ver reportes de cobertura en la web:

1. Abre https://codecov.io
2. Haz login con GitHub
3. Conecta tu repositorio `Contador_Palabras_Texto`
4. ¡Listo! Los reportes se subirán automáticamente

---

## 🎯 Cómo funcionan los workflows

### Triggers automáticos:
- Cada `push` a `main` o `develop`
- Cada `pull request` a `main` o `develop`

### Resultados:
- **Pestaña Actions** — Logs completos
- **Comentarios en PRs** — Resumen de tests
- **Badges** — Estado en el README

---

## 📊 Archivos creados

```
.github/
├── workflows/
│   ├── tests.yml              # Testing multi-versión
│   ├── linting.yml            # Análisis de código
│   └── README.md              # Documentación
```

---

## 🆘 Troubleshooting

### ❌ Los workflows no aparecen en Actions

→ Espera 1-2 minutos después del push  
→ Recarga la página

### ❌ Tests fallan en GitHub Actions

→ Verifica los logs en la pestaña Actions  
→ Compara con `pytest` local: `pytest`

### ❌ Codecov no recibe reportes

→ Configura Codecov en https://codecov.io  
→ El upload automático necesita el repositorio conectado

---

## 📚 Documentación completa

Para más detalles sobre cada workflow, lee:
`.github/workflows/README.md`

---

## ✨ Beneficios

✅ **Automatización** — Los tests corren sin hacer nada  
✅ **Múltiples versiones** — Compatibilidad garantizada  
✅ **Calidad de código** — Linting automático  
✅ **Seguridad** — Análisis de vulnerabilidades  
✅ **Documentación** — Reportes de cobertura  

---

**¡Listo para usar! 🎉**
