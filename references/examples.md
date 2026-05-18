# Ejemplos de Uso - APA Checker

Este documento contiene ejemplos prácticos de uso del verificador APA.

## Ejemplo 1: Artículo Académico Simple

### Entrada (`articulo_ejemplo.md`)

```markdown
# Efectos del Cambio Climático en la Biodiversidad Marina

## Introducción

Según García(2020), el cambio climático representa una amenaza significativa.
Estudios previos (Smith y Jones, 2021) han documentado efectos en ecosistemas costeros.
La investigación de López, Martínez, Rodríguez y Sánchez(2019) mostró datos alarmantes.

## Metodología

### Participantes

Los participantes fueron seleccionados mediante muestreo aleatorio.

### Procedimiento

Se siguió el protocolo establecido por Johnson and Williams(2020).

## Resultados

Los resultados confirmaron las hipótesis (García 2020, Smith 2021).

## Referencias

Smith, A. and Jones, B. (2021). Marine ecosystems under stress. Ocean Science, 15(2), 123-145
García, M.(2020). Climate change impacts. Environmental Review, 10, 45-67.
López, J., Martínez, A., Rodríguez, C. and Sánchez, M. (2019). Biodiversity loss. Marine Biology, 25(3), 234-256.
Johnson, P. and Williams, R. (2020). Research methods in marine science. Academic Press
```

### Salida (`articulo_ejemplo_APA_CORREGIDO.md`)

```markdown
# Efectos del Cambio Climático en la Biodiversidad Marina

## Introducción

Según García (2020), el cambio climático representa una amenaza significativa.
Estudios previos (Smith & Jones, 2021) han documentado efectos en ecosistemas costeros.
La investigación de López et al. (2019) mostró datos alarmantes.

## Metodología

### Participantes

Los participantes fueron seleccionados mediante muestreo aleatorio.

### Procedimiento

Se siguió el protocolo establecido por Johnson & Williams (2020).

## Resultados

Los resultados confirmaron las hipótesis (García, 2020; Smith, 2021).

## Referencias

García, M. (2020). Climate change impacts. *Environmental Review*, *10*, 45-67.

Johnson, P., & Williams, R. (2020). Research methods in marine science. Academic Press.

López, J., Martínez, A., Rodríguez, C., & Sánchez, M. (2019). Biodiversity loss. *Marine Biology*, *25*(3), 234-256.

Smith, A., & Jones, B. (2021). Marine ecosystems under stress. *Ocean Science*, *15*(2), 123-145.
```

### Correcciones Aplicadas:

1. ✅ `García(2020)` → `García (2020)` - Agregado espacio antes del paréntesis
2. ✅ `(Smith y Jones, 2021)` → `(Smith & Jones, 2021)` - Cambiado "y" por "&"
3. ✅ `López, Martínez, Rodríguez y Sánchez(2019)` → `López et al. (2019)` - 3+ autores
4. ✅ `Johnson and Williams(2020)` → `Johnson & Williams (2020)` - "and" por "&" y espacio
5. ✅ `(García 2020, Smith 2021)` → `(García, 2020; Smith, 2021)` - Formato múltiples citas
6. ✅ Referencias ordenadas alfabéticamente
7. ✅ `and` → `&` en referencias
8. ✅ Nombres de revistas en cursiva
9. ✅ Puntos finales agregados

---

## Ejemplo 2: Tesis de Posgrado

### Entrada (`tesis_ejemplo.md`)

```markdown
# Análisis del Comportamiento del Consumidor Digital

## Marco Teórico

### Modelos de Comportamiento

El modelo propuesto por Davis(1989) sigue siendo relevante.
Sin embargo, Venkatesh y Morris y Davis y Davis(2003) expandieron este modelo.
Investigaciones recientes (Kim 2020, Lee 2020, Park 2021) han actualizado el marco.

## referencias

Venkatesh, V., Morris, M. G., Davis, G. B. and Davis, F. D. (2003). User acceptance of information technology. MIS Quarterly, 27(3), 425-478
Davis, F. D.(1989). Perceived usefulness, perceived ease of use. MIS Quarterly, 13(3), 319-340
Kim, S. (2020). Digital consumer behavior. Journal of Marketing, 45, 12-30
Lee, J.(2020). Online shopping patterns. E-Commerce Research, 10(2), 56-78.
Park, H. (2021). Mobile commerce adoption. Technology Acceptance, 5(1), 89-102
```

### Salida (`tesis_ejemplo_APA_CORREGIDO.md`)

```markdown
# Análisis del Comportamiento del Consumidor Digital

## Marco Teórico

### Modelos de Comportamiento

El modelo propuesto por Davis (1989) sigue siendo relevante.
Sin embargo, Venkatesh et al. (2003) expandieron este modelo.
Investigaciones recientes (Kim, 2020; Lee, 2020; Park, 2021) han actualizado el marco.

## Referencias

Davis, F. D. (1989). Perceived usefulness, perceived ease of use. *MIS Quarterly*, *13*(3), 319-340.

Kim, S. (2020). Digital consumer behavior. *Journal of Marketing*, *45*, 12-30.

Lee, J. (2020). Online shopping patterns. *E-Commerce Research*, *10*(2), 56-78.

Park, H. (2021). Mobile commerce adoption. *Technology Acceptance*, *5*(1), 89-102.

Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology. *MIS Quarterly*, *27*(3), 425-478.
```

---

## Ejemplo 3: README de Proyecto Académico

### Entrada (`README.md`)

```markdown
# Proyecto de Análisis de Datos Ambientales

Este proyecto implementa los métodos descritos por Smith(2020).

## Métodos

Seguimos el framework de Johnson y Lee(2019) con modificaciones de García, López, Martínez(2021).

## Referencias Principales

Johnson, A. and Lee, B. (2019). Data analysis methods. Statistics Review, 15, 123-145
Smith, C.(2020). Environmental data processing. Data Science, 8(2), 67-89.
García, M., López, J. and Martínez, R. (2021). Advanced techniques. Journal of Environmental Science, 20(1), 34-56
```

### Comando:

```bash
python scripts/apa_checker.py README.md
```

### Salida (`README_APA_CORREGIDO.md`)

```markdown
# Proyecto de Análisis de Datos Ambientales

Este proyecto implementa los métodos descritos por Smith (2020).

## Métodos

Seguimos el framework de Johnson & Lee (2019) con modificaciones de García et al. (2021).

## Referencias Principales

García, M., López, J., & Martínez, R. (2021). Advanced techniques. *Journal of Environmental Science*, *20*(1), 34-56.

Johnson, A., & Lee, B. (2019). Data analysis methods. *Statistics Review*, *15*, 123-145.

Smith, C. (2020). Environmental data processing. *Data Science*, *8*(2), 67-89.
```

---

## Ejemplo 4: Múltiples Archivos en Repositorio

### Estructura:

```
mi-proyecto/
├── README.md
├── introduccion.md
├── metodologia.md
└── conclusiones.md
```

### Comando para procesar todos:

```bash
python scripts/apa_checker.py mi-proyecto/ --mode all
```

### Comando para procesar solo README:

```bash
python scripts/apa_checker.py mi-proyecto/ --mode readme
```

### Comando para procesar archivos específicos:

```bash
python scripts/apa_checker.py mi-proyecto/ --mode specific --files introduccion.md metodologia.md
```

### Salida:

```
Procesando 4 archivo(s)...

Procesando: mi-proyecto/README.md
  ✓ Corregido → mi-proyecto/README_APA_CORREGIDO.md
  5 problema(s) detectado(s)

Procesando: mi-proyecto/introduccion.md
  ✓ Corregido → mi-proyecto/introduccion_APA_CORREGIDO.md
  8 problema(s) detectado(s)

Procesando: mi-proyecto/metodologia.md
  ✓ Sin problemas

Procesando: mi-proyecto/conclusiones.md
  ✓ Corregido → mi-proyecto/conclusiones_APA_CORREGIDO.md
  3 problema(s) detectado(s)

📋 Reporte generado: REPORTE_APA.md

============================================================
Resumen: 4/4 archivos procesados exitosamente
         3 archivo(s) con correcciones aplicadas
============================================================
```

---

## Ejemplo 5: Repositorio Git Remoto

### Comando:

```bash
python scripts/apa_checker.py https://github.com/usuario/tesis-doctoral.git --mode all
```

### Proceso:

1. Clona el repositorio en un directorio temporal
2. Encuentra todos los archivos `.md`
3. Procesa cada archivo
4. Genera versiones corregidas
5. Crea el reporte
6. Limpia el directorio temporal

### Ejemplo de Reporte Generado (`REPORTE_APA.md`):

```markdown
# Reporte de Verificación APA 7ª Edición

## Resumen

- **Archivos procesados**: 12
- **Exitosos**: 12
- **Con correcciones**: 9
- **Total de problemas detectados**: 47

## Detalle por Archivo

### 🔧 README.md

**Archivo corregido**: `README_APA_CORREGIDO.md`

**Problemas encontrados**: 3

**Detalles**:

- Encontradas 2 citas sin espacio antes del paréntesis
- Corrigiendo 1 citas con 'y' en lugar de '&'
- Procesadas 5 referencias bibliográficas

### ✅ introduccion.md

✓ Sin problemas detectados

### 🔧 capitulo1.md

**Archivo corregido**: `capitulo1_APA_CORREGIDO.md`

**Problemas encontrados**: 8

**Detalles**:

- Encontradas 3 citas sin espacio antes del paréntesis
- Corrigiendo 2 citas con 'and' en lugar de '&'
- Corrigiendo 1 citas de 3+ autores a formato 'et al.'
- Agregado punto final a encabezado nivel 4: Criterios de selección.
- Procesadas 15 referencias bibliográficas

[... continúa para cada archivo ...]

---

*Reporte generado por APA Checker - Skill para Claude*
```

---

## Ejemplo 6: Casos Especiales

### Citas Narrativas vs Parentéticas

**Entrada:**
```markdown
García(2020) demostró que... mientras que otros autores (Smith y Jones 2021) argumentan...
```

**Salida:**
```markdown
García (2020) demostró que... mientras que otros autores (Smith & Jones, 2021) argumentan...
```

### Múltiples Obras del Mismo Autor

**Entrada:**
```markdown
Los estudios (García 2019, García 2020a, García 2020b) muestran...
```

**Salida:**
```markdown
Los estudios (García, 2019, 2020a, 2020b) muestran...
```
*(Nota: Esta funcionalidad requiere implementación adicional)*

### Referencias con DOI

**Entrada:**
```markdown
Smith, A. (2021). Title of article. Journal Name, 10(2), 45-60. doi: 10.1234/journal.2021.001
```

**Salida:**
```markdown
Smith, A. (2021). Title of article. *Journal Name*, *10*(2), 45-60. https://doi.org/10.1234/journal.2021.001
```

---

## Consejos de Uso

### 1. Antes de Procesar

- ✅ Haz backup de tus archivos originales
- ✅ Revisa que el texto esté en formato Markdown válido
- ✅ Asegúrate de que la sección de referencias esté claramente marcada

### 2. Después de Procesar

- ✅ Revisa el archivo `REPORTE_APA.md` 
- ✅ Compara los archivos originales con los corregidos
- ✅ Verifica manualmente las correcciones complejas
- ✅ Mantén los archivos originales como respaldo

### 3. Casos que Requieren Revisión Manual

- Nombres de autores con caracteres especiales
- Referencias de tipos inusuales (redes sociales, podcast, etc.)
- Citas con información adicional (capítulo, página específica)
- Abreviaturas latinas (et al., i.e., e.g.)

---

*Para más información, consulta el manual APA 7ª edición oficial.*
