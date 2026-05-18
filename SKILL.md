---
name: Veri_APA7
description: Verificador y corrector de formato APA 7ª edición para documentos Markdown y repositorios Git. Use este skill cuando el usuario mencione APA, citas académicas, referencias bibliográficas, formato de investigación, corrección de citado, verificación de estilo académico, o cuando necesite procesar archivos .md con contenido académico. También cuando el usuario pida "revisar las citas", "corregir formato APA", "validar referencias", o trabajar con documentos de investigación en Markdown.
---

# Veri_APA7 - Verificador y Corrector de Formato APA 7ª Edición

Este skill verifica y corrige automáticamente el formato APA 7ª edición en documentos Markdown y repositorios Git.

## Capacidades

### 1. Verificación Completa
- **Citas en el texto**: (Autor, Año), (Autor & Autor, Año), (Autor et al., Año)
- **Referencias bibliográficas**: Formato completo al final del documento
- **Títulos y encabezados**: Niveles jerárquicos según APA 7
- **Formato general**: Espaciado, puntuación, capitalización

### 2. Fuentes de Entrada
- Archivos Markdown individuales (.md)
- Repositorios Git completos (locales o remotos)
- Contenido de texto directo

### 3. Modos de Procesamiento
- **Archivo único**: Procesa un archivo específico
- **README only**: Solo el README.md del repositorio
- **Todos los .md**: Todos los archivos Markdown del repo
- **Selectivo**: Lista específica de archivos

## Flujo de Trabajo

### Paso 1: Ejecutar el verificador

```bash
# Procesar un archivo
python /home/claude/apa-checker-skill/scripts/Veri_APA7.py archivo.md

# Procesar README de un repo
python /home/claude/apa-checker-skill/scripts/Veri_APA7.py /ruta/repo --mode readme

# Procesar todos los .md de un repo
python /home/claude/apa-checker-skill/scripts/Veri_APA7.py /ruta/repo --mode all

# Procesar archivos específicos
python /home/claude/apa-checker-skill/scripts/Veri_APA7.py /ruta/repo --files archivo1.md archivo2.md

# Clonar repo remoto y procesar
python /home/claude/apa-checker-skill/scripts/Veri_APA7.py https://github.com/user/repo.git --mode all
```

### Paso 2: Revisar el reporte

El script genera:
- `REPORTE_APA.md`: Resumen de errores encontrados
- `archivo_APA_CORREGIDO.md`: Versión corregida de cada archivo
- Estadísticas de correcciones aplicadas

### Paso 3: Interpretar resultados

Consulta `references/apa7_rules.md` para entender las reglas aplicadas.

## Reglas APA 7 Implementadas

### Citas en Texto

**Un autor:**
- ❌ Incorrecto: `Según García(2020)` o `(García 2020)`
- ✅ Correcto: `Según García (2020)` o `(García, 2020)`

**Dos autores:**
- ❌ Incorrecto: `(Smith y Jones, 2021)` o `(Smith and Jones, 2021)`
- ✅ Correcto: `(Smith & Jones, 2021)`

**Tres o más autores:**
- ❌ Incorrecto: `(García, López, Martínez, 2019)`
- ✅ Correcto: `(García et al., 2019)`

**Citas múltiples:**
- ❌ Incorrecto: `(García 2020, López 2021)`
- ✅ Correcto: `(García, 2020; López, 2021)`

### Referencias Bibliográficas

El skill verifica:
- Orden alfabético por apellido del autor
- Formato de nombres (Apellido, I.)
- Puntuación correcta
- Sangría francesa (hanging indent)
- Capitalización de títulos
- Formato de DOI/URL

**Artículo de revista:**
```
Apellido, I. I., & Apellido, I. I. (Año). Título del artículo. Nombre de la Revista, volumen(número), pp-pp. https://doi.org/xxxxx
```

**Libro:**
```
Apellido, I. I. (Año). Título del libro (edición). Editorial.
```

**Capítulo de libro:**
```
Apellido, I. I. (Año). Título del capítulo. En I. I. Editor & I. I. Editor (Eds.), Título del libro (pp. xx-xx). Editorial.
```

### Títulos y Encabezados

**Niveles jerárquicos:**
- Nivel 1: Centrado, Negrita, Cada Palabra en Mayúscula
- Nivel 2: Alineado a la izquierda, Negrita, Cada Palabra en Mayúscula
- Nivel 3: Alineado a la izquierda, Negrita, Cursiva, Cada Palabra en Mayúscula
- Nivel 4: Sangría, Negrita, Cada Palabra en Mayúscula, termina con punto.
- Nivel 5: Sangría, Negrita, Cursiva, Cada Palabra en Mayúscula, termina con punto.

En Markdown:
- `# Título` → Nivel 1
- `## Título` → Nivel 2
- `### Título` → Nivel 3
- `#### Título.` → Nivel 4
- `##### Título.` → Nivel 5

## Ejemplos de Uso

### Ejemplo 1: Archivo Individual

```bash
python scripts/Veri_APA7.py mi_articulo.md
```

**Entrada** (`mi_articulo.md`):
```markdown
# Introducción

Según García(2020), la investigación muestra resultados significativos.
Los estudios previos (Smith y Jones, 2021) confirman esta hipótesis.

## Referencias

García, J. (2020). Título del artículo. Revista, 10(2), 45-60.
Smith, A. and Jones, B. (2021). Otro artículo. Journal, 5, 12-20.
```

**Salida** (`mi_articulo_APA_CORREGIDO.md`):
```markdown
# Introducción

Según García (2020), la investigación muestra resultados significativos.
Los estudios previos (Smith & Jones, 2021) confirman esta hipótesis.

## Referencias

García, J. (2020). Título del artículo. *Revista*, *10*(2), 45-60.

Smith, A., & Jones, B. (2021). Otro artículo. *Journal*, *5*, 12-20.
```

### Ejemplo 2: Repositorio Git

```bash
python scripts/Veri_APA7.py https://github.com/sebastiangz/veri_apa7.git --mode all
```

Procesa todos los archivos .md y genera versiones corregidas.

## Configuración Avanzada

Edita `scripts/config.json` para personalizar:

```json
{
  "strict_mode": true,
  "check_citations": true,
  "check_references": true,
  "check_headings": true,
  "auto_format_references": true,
  "preserve_comments": true,
  "output_suffix": "_APA_CORREGIDO"
}
```

## Limitaciones

- No verifica contenido de citas (solo formato)
- No valida si todas las citas tienen referencia (requiere análisis semántico)
- No procesa citas en imágenes o tablas complejas
- Asume que el texto está en español o inglés

## Referencias

Para detalles completos de las reglas APA 7, consulta:
- `references/apa7_rules.md`: Guía completa de reglas
- `references/examples.md`: Ejemplos de cada tipo de referencia

## Solución de Problemas

**Error: No se encontraron citas**
- Verifica que uses el formato `(Autor, Año)` y no `[Autor, Año]`

**Error: Repositorio no accesible**
- Asegúrate de tener permisos de lectura
- Para repos privados, configura credenciales Git

**Referencias no se ordenan correctamente**
- Verifica que cada referencia comience con el apellido del autor
- Usa sangría francesa en el Markdown original

## Mantenimiento

Para actualizar las reglas APA o agregar nuevas verificaciones:
1. Edita `scripts/apa_rules.py`
2. Actualiza los tests en `tests/test_apa.py`
3. Ejecuta: `python tests/test_apa.py`
