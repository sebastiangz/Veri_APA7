# APA Checker - Verificador y Corrector de Formato APA 7ª Edición

Un skill/aditamentto que verifica y corrige automáticamente el formato APA (7ª edición) en documentos Markdown y repositorios Git.

## 🎯 Características

- ✅ **Verificación de citas en texto**: (Autor, Año), (Autor & Autor, Año), (Autor et al., Año)
- ✅ **Corrección de referencias bibliográficas**: Formato, orden alfabético, puntuación
- ✅ **Validación de encabezados**: Niveles jerárquicos según APA 7
- ✅ **Procesamiento flexible**: Archivos individuales, repositorios completos, o selección específica
- ✅ **Reportes detallados**: Resumen de correcciones con estadísticas
- ✅ **No destructivo**: Genera archivos corregidos sin modificar originales

## 📦 Instalación

### Opción 1: Usar como Skill Local de tu TOOL 

1. Copia la carpeta `apa-checker-skill` a tu directorio de skills:
   ```bash
   cp -r Veri_APA7-skill ~/.TOOL/skills/
   ```

2. O clona desde el repositorio:
   ```bash
   git clone [URL_DEL_REPO] ~/.TOOL/skills/Veri_APA7-skill
   ```

3. Tu TOOL detectará automáticamente el skill cuando menciones APA, citas, o referencias académicas.

### Opción 2: Uso Independiente

```bash
# Clonar o descargar
git clone [[URL_DEL_REPO](https://github.com/sebastiangz/Veri_APA7/)] Veri_APA7-skill
cd Veri_APA7-skill

# El script no requiere dependencias adicionales (solo Python 3.7+)
python scripts/Veri_APA7.py --help
```

## 🚀 Uso Rápido

### Procesar un archivo individual

```bash
python scripts/Veri_APA7.py mi_articulo.md
```

Esto genera:
- `mi_articulo_APA_CORREGIDO.md` - Versión corregida
- `REPORTE_APA.md` - Resumen de correcciones

### Procesar todos los .md de un directorio

```bash
python scripts/Veri_APA7.py /ruta/a/proyecto --mode all
```

### Procesar solo README.md

```bash
python scripts/Veri_APA7.py /ruta/a/proyecto --mode readme
```

### Procesar archivos específicos

```bash
python scripts/Veri_APA7.py /ruta/a/proyecto --mode specific --files intro.md metodo.md
```

### Procesar repositorio Git remoto

```bash
python scripts/Veri_APA7.py https://github.com/usuario/repo.git --mode all
```

## 📋 Ejemplos

### Antes (Errores Comunes)

```markdown
# Introducción

Según García(2020), los resultados son significativos.
Otros estudios (Smith y Jones, 2021) confirman esto.
La investigación de López, Martínez, Rodríguez(2019) muestra datos.

## Referencias

Smith, A. and Jones, B. (2021). Título del artículo. Revista, 10(2), 45-60
García, M.(2020). Otro artículo. Journal, 5, 12-20.
```

### Después (Formato APA 7 Correcto)

```markdown
# Introducción

Según García (2020), los resultados son significativos.
Otros estudios (Smith & Jones, 2021) confirman esto.
La investigación de López et al. (2019) muestra datos.

## Referencias

García, M. (2020). Otro artículo. *Journal*, *5*, 12-20.

Smith, A., & Jones, B. (2021). Título del artículo. *Revista*, *10*(2), 45-60.
```

## 🔍 Qué Verifica

### Citas en Texto

- ✅ Espacio antes del paréntesis: `García (2020)` no `García(2020)`
- ✅ Coma entre autor y año: `(García, 2020)` no `(García 2020)`
- ✅ Ampersand (&) en citas: `(Smith & Jones, 2021)` no `(Smith y Jones, 2021)`
- ✅ "et al." para 3+ autores: `(López et al., 2019)`
- ✅ Punto y coma en múltiples citas: `(A, 2020; B, 2021)`

### Referencias Bibliográficas

- ✅ Orden alfabético por apellido
- ✅ Ampersand (&) en lugar de "and" o "y"
- ✅ Puntuación correcta
- ✅ Punto final en cada referencia
- ✅ Formato de nombres de revistas en cursiva

### Encabezados

- ✅ Niveles 4 y 5 terminan con punto
- ✅ Capitalización apropiada (se reporta, no se corrige automáticamente)

## 📊 Reporte Generado

Cada ejecución genera `REPORTE_APA.md`:

```markdown
# Reporte de Verificación APA 7ª Edición

## Resumen
- Archivos procesados: 5
- Exitosos: 5
- Con correcciones: 3
- Total de problemas detectados: 18

## Detalle por Archivo
### 🔧 articulo.md
**Problemas encontrados**: 8
- Encontradas 3 citas sin espacio antes del paréntesis
- Corrigiendo 2 citas con 'y' en lugar de '&'
...
```

## ⚙️ Opciones Avanzadas

```bash
# Cambiar sufijo de archivos corregidos
python scripts/Veri_APA7.py archivo.md --output-suffix "_CORREGIDO_APA"

# No generar reporte
python scripts/Veri_APA7.py archivo.md --no-report

# Ver todas las opciones
python scripts/Veri_APA7.py --help
```

## 📚 Documentación

- **[SKILL.md](SKILL.md)** - Instrucciones completas para tu TOOL
- **[references/apa7_rules.md](references/apa7_rules.md)** - Guía detallada de reglas APA 7
- **[references/examples.md](references/examples.md)** - Ejemplos de uso extensos

## ⚠️ Limitaciones

- No verifica el **contenido** de las citas (solo el formato)
- No valida que todas las citas tengan su referencia correspondiente
- No procesa citas dentro de imágenes o tablas complejas
- Asume texto en español o inglés
- Algunas correcciones complejas requieren revisión manual

## 🤝 Contribuir

¿Encontraste un error o quieres agregar una funcionalidad?

1. Reporta issues con ejemplos específicos
2. Sugiere mejoras en las reglas de verificación
3. Comparte casos de uso interesantes

## 📝 Licencia

MIT License - Libre para uso académico y comercial

## 🔗 Referencias

- [Manual APA 7ª Edición Oficial](https://apastyle.apa.org/)
- [APA Style Blog](https://apastyle.apa.org/blog)

---

**Creado para facilitar el trabajo académico y la investigación 🎓**
