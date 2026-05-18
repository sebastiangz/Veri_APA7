# Veri_APA7 - Verificador y Corrector de Formato APA 7ª Edición

Un verificador/corrector automático de formato APA (7ª edición) para documentos Markdown y repositorios Git. Diseñado para ser usado de forma independiente o como skill/plugin para tus TOOLS ( LLMs cómo Ollama, ChatGPT, Gemini, etc.).

## 🎯 Características

- ✅ **Verificación de citas en texto**: (Autor, Año), (Autor & Autor, Año), (Autor et al., Año)
- ✅ **Corrección de referencias bibliográficas**: Formato, orden alfabético, puntuación
- ✅ **Validación de encabezados**: Niveles jerárquicos según APA 7
- ✅ **Procesamiento flexible**: Archivos individuales, repositorios completos, o selección específica
- ✅ **Reportes detallados**: Resumen de correcciones con estadísticas
- ✅ **No destructivo**: Genera archivos corregidos sin modificar originales

## 📦 Instalación

### Opción 1: Uso Independiente (Recomendado)

```bash
# Clonar el repositorio
git clone https://github.com/sebastiangz/Veri_APA7.git
cd Veri_APA7

# El script no requiere dependencias adicionales (solo Python 3.7+)
python scripts/Veri_APA7.py --help
```

### Opción 2: Como Skill/Plugin para LLMs

**Para IA LOCAL:**
```bash
# Copiar a directorio de skills de Claude
cp -r Veri_APA7 ~/.ollama/skills/
```

**Para otros LLMs:**
- Consulta el archivo `SKILL.md` para instrucciones de integración
- Adapta según las capacidades de tu LLM (ChatGPT, Gemini, etc.)

Ver [INSTALACION.md](INSTALACION.md) para guía detallada.

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

- **[INSTALACION.md](INSTALACION.md)** - Guía rápida de instalación y configuración
- **[SKILL.md](SKILL.md)** - Instrucciones para integración con LLMs
- **[references/apa7_rules.md](references/apa7_rules.md)** - Guía detallada de reglas APA 7
- **[references/examples.md](references/examples.md)** - Ejemplos de uso extensos

## ⚠️ Limitaciones

- No verifica el **contenido** de las citas (solo el formato)
- No valida que todas las citas tengan su referencia correspondiente
- No procesa citas dentro de imágenes o tablas complejas
- Asume texto en español o inglés
- Algunas correcciones complejas requieren revisión manual

## 🧪 Testing

El repositorio incluye archivos de prueba:

```bash
# Ejecutar prueba básica
python scripts/Veri_APA7.py tests/ejemplo_test.md

# Verificar resultados
cat tests/ejemplo_test_APA_CORREGIDO.md
cat REPORTE_APA.md
```

## 🤝 Contribuir

¿Encontraste un error o quieres agregar una funcionalidad?

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

### Ideas de Contribución

- Agregar soporte para más tipos de referencias (redes sociales, podcasts)
- Mejorar la detección de citas narrativas vs. parentéticas
- Implementar verificación de citas cruzadas
- Agregar soporte para otros formatos de entrada (Word, LaTeX)
- Crear interfaz gráfica (GUI)

## 📝 Licencia

MIT License - Libre para uso académico y comercial

Copyright (c) 2025 Sebastián González

Ver [LICENSE](LICENSE) para más detalles.

## 🔗 Referencias

- [Manual APA 7ª Edición Oficial](https://apastyle.apa.org/)
- [APA Style Blog](https://apastyle.apa.org/blog)
- [Guía de Citación APA (Español)](https://normas-apa.org/)

## 📞 Contacto

- **Repositorio**: [https://github.com/sebastiangz/Veri_APA7](https://github.com/sebastiangz/Veri_APA7)
- **Issues**: [https://github.com/sebastiangz/Veri_APA7/issues](https://github.com/sebastiangz/Veri_APA7/issues)
- **Autor**: [@sebastiangz](https://github.com/sebastiangz)

## ⭐ Agradecimientos

Si este proyecto te fue útil, considera darle una estrella ⭐ en GitHub.

---

**Creado para facilitar el trabajo académico y la investigación 🎓📚**
