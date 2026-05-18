# Guía Rápida de Instalación - Veri_APA7

## 🚀 Instalación en 3 Pasos

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/sebastiangz/Veri_APA7.git
cd Veri_APA7
```

### Paso 2: Verificar Requisitos

**Python 3.7 o superior** (el script no necesita dependencias adicionales)

```bash
# Verificar versión de Python
python --version
# o
python3 --version
```

### Paso 3: ¡Probar!

```bash
# Probar con el archivo de ejemplo incluido
python scripts/Veri_APA7.py tests/ejemplo_test.md

# Verificar que se generaron los archivos
ls tests/ejemplo_test_APA_CORREGIDO.md
ls REPORTE_APA.md
```

## 📝 Primer Uso

### Ejemplo: Corregir tu primer archivo

1. **Crea un archivo de prueba** (`mi_prueba.md`):

```markdown
# Mi Artículo

Según García(2020), esto es importante.
Los estudios (Smith y Jones, 2021) lo confirman.

## Referencias

Smith, A. and Jones, B. (2021). Título. Revista, 10, 23-45
García, M.(2020). Otro título. Journal, 5, 12-20.
```

2. **Ejecuta el verificador**:

```bash
python scripts/Veri_APA7.py mi_prueba.md
```

3. **Revisa los resultados**:

```bash
# Ver archivo corregido
cat mi_prueba_APA_CORREGIDO.md

# Ver reporte detallado
cat REPORTE_APA.md
```

## 🎯 Casos de Uso Comunes

### Caso 1: Tesis o Artículo Individual

```bash
python scripts/Veri_APA7.py mi_tesis.md
```

### Caso 2: Proyecto con Múltiples Capítulos

```bash
# Procesar todos los archivos .md del proyecto
python scripts/Veri_APA7.py ./mi-proyecto --mode all
```

### Caso 3: Solo el README de un Repo

```bash
python scripts/Veri_APA7.py ./mi-repo --mode readme
```

### Caso 4: Archivos Específicos

```bash
python scripts/Veri_APA7.py ./proyecto --mode specific --files capitulo1.md capitulo2.md conclusiones.md
```

### Caso 5: Repositorio Git Remoto

```bash
python scripts/Veri_APA7.py https://github.com/usuario/mi-tesis.git --mode all
```

## 🔧 Uso como Skill/Plugin para LLMs

### Para Claude

```bash
# Copiar a directorio de skills de Claude
cp -r Veri_APA7 ~/.claude/skills/

# Claude detectará automáticamente el skill
```

### Para Otros LLMs (ChatGPT, Gemini, etc.)

El archivo `SKILL.md` contiene las instrucciones que puedes:

1. **Copiar y pegar** en el contexto del LLM
2. **Usar como referencia** para crear un plugin personalizado
3. **Adaptar** según las capacidades de tu LLM

```bash
# Ver las instrucciones del skill
cat SKILL.md
```

## ⚙️ Requisitos del Sistema

### Requisitos Mínimos

- **Python**: 3.7 o superior
- **Sistema Operativo**: Linux, macOS, o Windows
- **Git** (opcional): Solo para clonar repositorios remotos

### Verificar Instalación

```bash
# Python
python --version  # o python3 --version

# Git (opcional)
git --version
```

### Instalar Python (si no lo tienes)

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**macOS:**
```bash
brew install python3
```

**Windows:**
- Descarga desde [python.org](https://www.python.org/downloads/)
- Durante la instalación, marca "Add Python to PATH"

## 🐛 Solución de Problemas

### Error: "No se encontró Python"

```bash
# En vez de 'python', usa 'python3'
python3 scripts/Veri_APA7.py archivo.md
```

### Error: "Permission denied"

```bash
# Hacer ejecutable el script
chmod +x scripts/Veri_APA7.py

# Luego ejecutar
./scripts/Veri_APA7.py archivo.md
```

### No se genera archivo corregido

- ✅ Verifica que el archivo original existe
- ✅ Asegúrate de tener permisos de escritura en el directorio
- ✅ Revisa que el archivo sea .md válido
- ✅ Comprueba que el archivo contenga citas APA

### Script no encuentra módulos

El script usa **solo librerías estándar de Python**, no necesitas instalar nada adicional:
- `re` - Expresiones regulares
- `sys` - Interacción con sistema
- `argparse` - Argumentos de línea de comandos
- `os` - Operaciones de sistema operativo
- `pathlib` - Manejo de rutas
- `json` - Procesamiento JSON
- `subprocess` - Para clonar repos Git
- `tempfile` - Archivos temporales
- `shutil` - Operaciones de archivos

## 📖 Siguientes Pasos

1. **Lee el [README.md](README.md)** para conocer todas las funcionalidades
2. **Consulta [references/apa7_rules.md](references/apa7_rules.md)** para entender las reglas
3. **Revisa [references/examples.md](references/examples.md)** para ver más ejemplos
4. **Explora [SKILL.md](SKILL.md)** para integración con LLMs

## ✅ Verificación de Instalación

Ejecuta este comando para verificar que todo funciona:

```bash
cd Veri_APA7
python scripts/Veri_APA7.py tests/ejemplo_test.md && echo "✅ ¡Instalación exitosa!"
```

Si ves el mensaje "✅ ¡Instalación exitosa!" y se generan los archivos:
- `tests/ejemplo_test_APA_CORREGIDO.md`
- `REPORTE_APA.md`

**¡Estás listo para usar Veri_APA7!**

## 🤔 ¿Necesitas Ayuda?

- 📝 [Crea un Issue](https://github.com/sebastiangz/Veri_APA7/issues) en GitHub
- 📚 Consulta la documentación en `references/`
- 💡 Revisa los ejemplos en `tests/`

---

**¡Feliz escritura académica! 🎓📚**
