# Reglas APA 7ª Edición - Guía de Referencia

Esta guía cubre las reglas principales del formato APA 7ª edición implementadas en el APA Checker.

## 1. Citas en el Texto

### 1.1 Citas Parentéticas

**Un solo autor:**
- `(García, 2020)`
- `(Smith, 2021)`

**Dos autores:**
- `(García & López, 2020)` ← Siempre usar `&`, no "y" ni "and"
- `(Smith & Jones, 2021)`

**Tres o más autores:**
- Primera mención: `(García et al., 2019)`
- Menciones subsecuentes: `(García et al., 2019)`
- ⚠️ APA 7 usa "et al." desde la primera cita con 3+ autores

**Mismo autor, mismo año:**
- `(García, 2020a)` y `(García, 2020b)`
- Usar letras para distinguir obras del mismo año

**Múltiples citas:**
- Ordenar alfabéticamente: `(García, 2020; López, 2018; Smith, 2021)`
- Separar con punto y coma (`;`)
- Mismo autor, diferentes años: `(García, 2018, 2020, 2021)`

### 1.2 Citas Narrativas

**Formato:**
- García (2020) demostró que...
- Según Smith y Jones (2021)...
- López et al. (2019) encontraron...

**Reglas:**
- Año entre paréntesis: `García (2020)` no `García(2020)`
- Dos autores: "y" en narrativa, "&" en paréntesis
  - Narrativa: `Smith y Jones (2021) afirman...`
  - Paréntesis: `...es evidente (Smith & Jones, 2021)`

### 1.3 Citas Directas

**Citas cortas (< 40 palabras):**
```
Como afirmó García (2020), "la investigación empírica demuestra" (p. 45).
```

**Citas largas (≥ 40 palabras):**
```
García (2020) explicó el fenómeno:

> La investigación empírica demuestra que los factores ambientales
> juegan un rol crucial en el desarrollo cognitivo. Este hallazgo
> contradice teorías previas que enfatizaban únicamente factores
> genéticos. (p. 45)
```

## 2. Referencias Bibliográficas

### 2.1 Estructura General

**Formato básico:**
```
Autor(es). (Año). Título de la obra. Fuente.
```

### 2.2 Artículos de Revista

**Con DOI:**
```
Apellido, I. I., & Apellido, I. I. (Año). Título del artículo. Nombre de la Revista, volumen(número), pp-pp. https://doi.org/xxxxx
```

**Ejemplo:**
```
García, J. M., & López, A. (2020). Efectos del cambio climático en ecosistemas marinos. Revista de Biología Marina, 15(3), 234-256. https://doi.org/10.1234/rbm.2020.15.3.234
```

**Sin DOI (con URL):**
```
Smith, A. B. (2021). Title of the article. Journal Name, 10(2), 45-60. https://www.journalwebsite.com/article
```

**Sin DOI ni URL:**
```
Jones, C. (2019). Another article title. Psychology Today, 25(4), 12-20.
```

### 2.3 Libros

**Libro completo:**
```
Apellido, I. I. (Año). Título del libro (edición, si no es la primera). Editorial.
```

**Ejemplo:**
```
García, M. (2018). Introducción a la psicología cognitiva (3ª ed.). McGraw-Hill.
```

**Libro con editores:**
```
Apellido, I. I., & Apellido, I. I. (Eds.). (Año). Título del libro. Editorial.
```

**Capítulo de libro:**
```
Apellido, I. I. (Año). Título del capítulo. En I. I. Editor & I. I. Editor (Eds.), Título del libro (pp. xx-xx). Editorial.
```

**Ejemplo:**
```
López, A. (2020). Teorías del aprendizaje. En M. García & J. Pérez (Eds.), Manual de psicología educativa (pp. 45-78). Pearson.
```

### 2.4 Fuentes Electrónicas

**Página web:**
```
Autor/Organización. (Año, Día Mes). Título de la página. Nombre del Sitio. URL
```

**Ejemplo:**
```
Organización Mundial de la Salud. (2021, 15 marzo). Efectos del COVID-19 en la salud mental. OMS. https://www.who.int/es/mental-health-covid
```

**Artículo de periódico online:**
```
Apellido, I. I. (Año, Día Mes). Título del artículo. Nombre del Periódico. URL
```

### 2.5 Otros Tipos

**Tesis:**
```
Apellido, I. I. (Año). Título de la tesis [Tesis doctoral, Nombre de la Universidad]. Base de datos. URL
```

**Conferencia:**
```
Apellido, I. I. (Año, Día-Día Mes). Título de la presentación [Presentación de conferencia]. Nombre de la Conferencia, Lugar.
```

**Informe técnico:**
```
Autor Corporativo. (Año). Título del informe (Informe N.º xxx). Editorial/Institución. URL
```

## 3. Formato de Títulos y Encabezados

### 3.1 Niveles de Encabezados

**Nivel 1 (Centrado, Negrita, Título Capitalizado)**
```markdown
# Metodología
```

**Nivel 2 (Alineado a Izquierda, Negrita, Título Capitalizado)**
```markdown
## Participantes
```

**Nivel 3 (Alineado a Izquierda, Negrita, Cursiva, Título Capitalizado)**
```markdown
### Criterios de Inclusión
```

**Nivel 4 (Sangría, Negrita, Título Capitalizado, Termina con Punto, Texto Continúa en Misma Línea)**
```markdown
#### Criterio Principal.
```

**Nivel 5 (Sangría, Negrita, Cursiva, Título Capitalizado, Termina con Punto, Texto Continúa en Misma Línea)**
```markdown
##### Subcategoría Específica.
```

### 3.2 Capitalización de Títulos

**Capitalizar:**
- Primera palabra
- Primera palabra después de dos puntos o guión
- Sustantivos, pronombres, verbos, adjetivos, adverbios
- Todas las palabras de 4+ letras

**NO capitalizar:**
- Artículos (a, an, the, el, la, los, las)
- Preposiciones cortas (in, on, at, of, to, en, de, con)
- Conjunciones (and, but, or, y, pero, o)

**Ejemplo:**
- ✅ `The Effects of Climate Change on Marine Ecosystems`
- ❌ `The Effects Of Climate Change On Marine Ecosystems`

## 4. Formato General del Documento

### 4.1 Espaciado
- Doble espacio en todo el documento
- No espacios adicionales después de títulos
- Una línea en blanco entre párrafos (en Markdown: línea vacía)

### 4.2 Márgenes
- 2.54 cm (1 pulgada) en todos los lados

### 4.3 Fuente
- Times New Roman, 12 pt
- Arial, 11 pt
- Calibri, 11 pt
- Georgia, 11 pt

### 4.4 Sangría
- Primera línea de cada párrafo: 1.27 cm (0.5 pulgadas)
- Referencias: sangría francesa (hanging indent)

## 5. Orden de Secciones (Artículo Típico)

1. Página de título
2. Resumen (Abstract)
3. Texto principal
   - Introducción
   - Método
   - Resultados
   - Discusión
4. Referencias
5. Notas al pie (si aplica)
6. Tablas
7. Figuras
8. Apéndices (si aplica)

## 6. Reglas Especiales

### 6.1 Números
- 0-9: escribir con palabras (excepto medidas, estadísticas)
- 10+: usar dígitos
- Inicio de oración: siempre con palabras

**Ejemplos:**
- ✅ `cinco participantes` pero `15 participantes`
- ✅ `3 cm`, `7%`, `5 mg`
- ✅ `Veinte por ciento de los participantes...`

### 6.2 Abreviaturas
- Primera mención: término completo seguido de abreviatura entre paréntesis
- Menciones subsecuentes: solo abreviatura

**Ejemplo:**
```
La Organización Mundial de la Salud (OMS) reportó... 
Según la OMS...
```

### 6.3 Listas

**Dentro del párrafo:**
```
Los tres factores son: (a) edad, (b) género, y (c) educación.
```

**Lista con viñetas:**
- Use viñetas para listas sin orden específico
- Use números para listas secuenciales

**Lista numerada:**
1. Primer paso
2. Segundo paso
3. Tercer paso

## 7. Errores Comunes

### ❌ Errores Frecuentes

1. **`(García 2020)`** → `(García, 2020)` - Falta coma
2. **`García(2020)`** → `García (2020)` - Falta espacio
3. **`(Smith y Jones, 2021)`** → `(Smith & Jones, 2021)` - Usar &
4. **`(García, López, Martínez, 2020)`** → `(García et al., 2020)` - 3+ autores
5. **`Garcia, J. (2020)`** → `García, J. (2020)` - Mantener acentos
6. **Referencias sin ordenar alfabéticamente**
7. **Títulos de artículos en mayúsculas** → Solo primera palabra
8. **Nombres de revistas sin cursiva**
9. **DOI sin formato https://doi.org/**
10. **Citas de citas (citado en...)** - Evitar, citar fuente original

## 8. Referencias Útiles

- Manual APA 7ª edición oficial: https://apastyle.apa.org/
- Blog APA Style: https://apastyle.apa.org/blog
- Generadores de referencias: Zotero, Mendeley, EndNote

---

*Esta guía es un resumen de las reglas principales. Consulte el Manual APA 7ª edición para casos especiales.*
