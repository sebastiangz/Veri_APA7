#!/usr/bin/env python3
"""
APA 7th Edition Checker and Corrector for Markdown files
Verifica y corrige formato APA versión 7 en documentos Markdown
"""

import re
import sys
import argparse
import os
from pathlib import Path
from typing import List, Tuple, Dict
import json
import subprocess
import tempfile
import shutil


class APAChecker:
    """Verificador y corrector de formato APA 7ª edición"""
    
    def __init__(self, strict_mode=True):
        self.strict_mode = strict_mode
        self.errors = []
        self.corrections = []
        
    def check_and_fix_in_text_citations(self, text: str) -> Tuple[str, List[str]]:
        """Verifica y corrige citas en el texto"""
        errors = []
        
        # Patrón para citas en texto: (Autor, Año) o (Autor et al., Año)
        # Detectar errores comunes
        
        # 1. Falta de espacio después de paréntesis: García(2020)
        pattern1 = r'(\w+)\((\d{4})\)'
        matches1 = re.findall(pattern1, text)
        if matches1:
            errors.append(f"Encontradas {len(matches1)} citas sin espacio antes del paréntesis")
            text = re.sub(pattern1, r'\1 (\2)', text)
        
        # 2. Coma faltante en citas: (García 2020) -> (García, 2020)
        pattern2 = r'\(([A-ZÁÉÍÓÚÑa-záéíóúñ\s&]+)\s+(\d{4})\)'
        def fix_comma(match):
            author = match.group(1)
            year = match.group(2)
            # Si no tiene coma ni "et al.", agregarla
            if ',' not in author and 'et al.' not in author:
                return f'({author}, {year})'
            return match.group(0)
        
        matches2 = re.findall(pattern2, text)
        if matches2:
            errors.append(f"Verificando {len(matches2)} citas para formato de coma")
            text = re.sub(pattern2, fix_comma, text)
        
        # 3. "y" en lugar de "&" en citas: (Smith y Jones, 2021) -> (Smith & Jones, 2021)
        pattern3 = r'\(([A-ZÁÉÍÓÚÑa-záéíóúñ]+)\s+y\s+([A-ZÁÉÍÓÚÑa-záéíóúñ]+),\s*(\d{4})\)'
        matches3 = re.findall(pattern3, text)
        if matches3:
            errors.append(f"Corrigiendo {len(matches3)} citas con 'y' en lugar de '&'")
            text = re.sub(pattern3, r'(\1 & \2, \3)', text)
        
        # 4. "and" en lugar de "&": (Smith and Jones, 2021) -> (Smith & Jones, 2021)
        pattern4 = r'\(([A-ZÁÉÍÓÚÑa-záéíóúñ]+)\s+and\s+([A-ZÁÉÍÓÚÑa-záéíóúñ]+),\s*(\d{4})\)'
        matches4 = re.findall(pattern4, text)
        if matches4:
            errors.append(f"Corrigiendo {len(matches4)} citas con 'and' en lugar de '&'")
            text = re.sub(pattern4, r'(\1 & \2, \3)', text)
        
        # 5. Más de dos autores sin "et al.": (García, López, Martínez, 2019)
        pattern5 = r'\(([A-ZÁÉÍÓÚÑa-záéíóúñ]+),\s*([A-ZÁÉÍÓÚÑa-záéíóúñ]+),\s*([A-ZÁÉÍÓÚÑa-záéíóúñ]+)(?:,\s*[A-ZÁÉÍÓÚÑa-záéíóúñ]+)*,\s*(\d{4})\)'
        matches5 = re.findall(pattern5, text)
        if matches5:
            errors.append(f"Corrigiendo {len(matches5)} citas de 3+ autores a formato 'et al.'")
            text = re.sub(pattern5, r'(\1 et al., \4)', text)
        
        # 6. Múltiples citas separadas incorrectamente: (García 2020, López 2021) -> (García, 2020; López, 2021)
        pattern6 = r'\(([A-ZÁÉÍÓÚÑa-záéíóúñ\s&]+),\s*(\d{4}),\s*([A-ZÁÉÍÓÚÑa-záéíóúñ\s&]+),\s*(\d{4})\)'
        matches6 = re.findall(pattern6, text)
        if matches6:
            errors.append(f"Corrigiendo {len(matches6)} citas múltiples con punto y coma")
            text = re.sub(pattern6, r'(\1, \2; \3, \4)', text)
        
        return text, errors
    
    def check_and_fix_references(self, text: str) -> Tuple[str, List[str]]:
        """Verifica y corrige la sección de referencias bibliográficas"""
        errors = []
        
        # Buscar sección de Referencias
        ref_patterns = [
            r'##?\s*Referencias?\s*\n',
            r'##?\s*Reference[s]?\s*\n',
            r'##?\s*Bibliografía\s*\n'
        ]
        
        ref_section_start = None
        for pattern in ref_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                ref_section_start = match.end()
                break
        
        if not ref_section_start:
            errors.append("No se encontró sección de Referencias")
            return text, errors
        
        # Extraer sección de referencias (hasta el final o siguiente sección #)
        ref_text = text[ref_section_start:]
        next_section = re.search(r'\n##?\s+[A-ZÁÉÍÓÚÑa-záéíóúñ]', ref_text)
        if next_section:
            ref_text = ref_text[:next_section.start()]
        
        # Dividir en referencias individuales (cada línea no vacía que no sea encabezado)
        ref_lines = [line.strip() for line in ref_text.split('\n') if line.strip() and not line.strip().startswith('#')]
        
        if not ref_lines:
            errors.append("Sección de Referencias vacía")
            return text, errors
        
        corrected_refs = []
        
        for ref in ref_lines:
            corrected_ref = ref
            
            # 1. Corregir "and" por "&" en autores
            corrected_ref = re.sub(r'\s+and\s+', ' & ', corrected_ref)
            corrected_ref = re.sub(r'\s+y\s+', ' & ', corrected_ref)
            
            # 2. Asegurar formato de nombre: Apellido, I. I.
            # (este es complejo, solo verificamos que tenga la estructura básica)
            
            # 3. Italizar nombres de revistas/libros (títulos después del año)
            # Patrón: (Año). Título. *Nombre Revista*
            # Esto es aproximado, en Markdown usamos *cursiva*
            
            # 4. Verificar punto al final
            if not corrected_ref.endswith('.') and not corrected_ref.endswith(')'):
                corrected_ref += '.'
                errors.append(f"Agregado punto final a referencia: {ref[:50]}...")
            
            corrected_refs.append(corrected_ref)
        
        # Ordenar alfabéticamente
        corrected_refs.sort(key=lambda x: x.split(',')[0].strip() if ',' in x else x)
        
        # Reconstruir texto
        new_ref_section = '\n\n' + '\n\n'.join(corrected_refs) + '\n'
        
        # Reemplazar sección antigua con nueva
        before_refs = text[:ref_section_start]
        after_refs = ''
        if next_section:
            after_refs = text[ref_section_start:][next_section.start():]
        
        text = before_refs + new_ref_section + after_refs
        
        errors.append(f"Procesadas {len(corrected_refs)} referencias bibliográficas")
        
        return text, errors
    
    def check_and_fix_headings(self, text: str) -> Tuple[str, List[str]]:
        """Verifica y corrige formato de títulos y encabezados según APA 7"""
        errors = []
        
        lines = text.split('\n')
        corrected_lines = []
        
        for line in lines:
            # Verificar si es un encabezado
            heading_match = re.match(r'^(#{1,5})\s+(.+)$', line)
            
            if heading_match:
                level = len(heading_match.group(1))
                title = heading_match.group(2).strip()
                
                # Nivel 4 y 5 deben terminar con punto
                if level >= 4:
                    if not title.endswith('.'):
                        title += '.'
                        errors.append(f"Agregado punto final a encabezado nivel {level}: {title[:30]}...")
                
                # Verificar capitalización (Cada Palabra en Mayúscula)
                # Este es un tema complejo, solo lo mencionamos
                
                corrected_lines.append(f"{'#' * level} {title}")
            else:
                corrected_lines.append(line)
        
        return '\n'.join(corrected_lines), errors
    
    def process_file(self, filepath: str, output_suffix: str = "_APA_CORREGIDO") -> Dict:
        """Procesa un archivo Markdown completo"""
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return {
                'filepath': filepath,
                'success': False,
                'error': str(e)
            }
        
        original_content = content
        all_errors = []
        
        # 1. Verificar y corregir citas en texto
        content, citation_errors = self.check_and_fix_in_text_citations(content)
        all_errors.extend(citation_errors)
        
        # 2. Verificar y corregir referencias
        content, ref_errors = self.check_and_fix_references(content)
        all_errors.extend(ref_errors)
        
        # 3. Verificar y corregir encabezados
        content, heading_errors = self.check_and_fix_headings(content)
        all_errors.extend(heading_errors)
        
        # Guardar archivo corregido
        base_name = Path(filepath).stem
        ext = Path(filepath).suffix
        dir_name = Path(filepath).parent
        
        output_path = dir_name / f"{base_name}{output_suffix}{ext}"
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Calcular estadísticas
        changes_made = content != original_content
        
        return {
            'filepath': filepath,
            'success': True,
            'output_path': str(output_path),
            'errors_found': len(all_errors),
            'errors': all_errors,
            'changes_made': changes_made
        }


def clone_repo(repo_url: str, target_dir: str) -> bool:
    """Clona un repositorio Git"""
    try:
        subprocess.run(['git', 'clone', repo_url, target_dir], 
                      check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error clonando repositorio: {e.stderr.decode()}")
        return False


def find_markdown_files(directory: str, mode: str = 'all', specific_files: List[str] = None) -> List[str]:
    """Encuentra archivos Markdown según el modo especificado"""
    
    path = Path(directory)
    
    if mode == 'readme':
        # Buscar README.md (case insensitive)
        for readme in ['README.md', 'readme.md', 'Readme.md', 'README.MD']:
            readme_path = path / readme
            if readme_path.exists():
                return [str(readme_path)]
        return []
    
    elif mode == 'all':
        # Todos los archivos .md recursivamente
        return [str(p) for p in path.rglob('*.md')]
    
    elif mode == 'specific' and specific_files:
        # Archivos específicos
        result = []
        for file in specific_files:
            file_path = path / file
            if file_path.exists():
                result.append(str(file_path))
            else:
                print(f"Advertencia: No se encontró {file}")
        return result
    
    return []


def generate_report(results: List[Dict], output_path: str = 'REPORTE_APA.md'):
    """Genera un reporte consolidado en Markdown"""
    
    total_files = len(results)
    successful = sum(1 for r in results if r['success'])
    files_with_changes = sum(1 for r in results if r.get('changes_made', False))
    total_errors = sum(r.get('errors_found', 0) for r in results)
    
    report = f"""# Reporte de Verificación APA 7ª Edición

## Resumen

- **Archivos procesados**: {total_files}
- **Exitosos**: {successful}
- **Con correcciones**: {files_with_changes}
- **Total de problemas detectados**: {total_errors}

## Detalle por Archivo

"""
    
    for result in results:
        if not result['success']:
            report += f"\n### ❌ {result['filepath']}\n\n"
            report += f"**Error**: {result.get('error', 'Desconocido')}\n\n"
            continue
        
        icon = "✅" if not result['changes_made'] else "🔧"
        report += f"\n### {icon} {result['filepath']}\n\n"
        
        if result['changes_made']:
            report += f"**Archivo corregido**: `{result['output_path']}`\n\n"
            report += f"**Problemas encontrados**: {result['errors_found']}\n\n"
            
            if result['errors']:
                report += "**Detalles**:\n\n"
                for error in result['errors']:
                    report += f"- {error}\n"
                report += "\n"
        else:
            report += "✓ Sin problemas detectados\n\n"
    
    report += "\n---\n\n"
    report += "*Reporte generado por Veri_APA7 - Aditamento implementado por sebastiangz*\n"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description='Verificador y corrector de formato APA 7ª edición para Markdown'
    )
    
    parser.add_argument(
        'input',
        help='Archivo .md, directorio local, o URL de repositorio Git'
    )
    
    parser.add_argument(
        '--mode',
        choices=['readme', 'all', 'specific'],
        default='all',
        help='Modo de procesamiento para directorios/repos'
    )
    
    parser.add_argument(
        '--files',
        nargs='+',
        help='Lista de archivos específicos (solo con --mode specific)'
    )
    
    parser.add_argument(
        '--output-suffix',
        default='_APA_CORREGIDO',
        help='Sufijo para archivos corregidos'
    )
    
    parser.add_argument(
        '--no-report',
        action='store_true',
        help='No generar reporte REPORTE_APA.md'
    )
    
    args = parser.parse_args()
    
    # Determinar si es archivo, directorio o URL de Git
    input_path = args.input
    is_git_url = input_path.startswith('http') or input_path.endswith('.git')
    is_file = os.path.isfile(input_path)
    is_dir = os.path.isdir(input_path)
    
    temp_dir = None
    
    try:
        # Si es URL de Git, clonar primero
        if is_git_url:
            temp_dir = tempfile.mkdtemp()
            print(f"Clonando repositorio {input_path}...")
            if not clone_repo(input_path, temp_dir):
                print("Error al clonar repositorio")
                return 1
            input_path = temp_dir
            is_dir = True
        
        # Obtener lista de archivos a procesar
        if is_file:
            files_to_process = [input_path]
        elif is_dir:
            files_to_process = find_markdown_files(
                input_path, 
                mode=args.mode,
                specific_files=args.files
            )
        else:
            print(f"Error: {input_path} no es un archivo, directorio o URL de Git válido")
            return 1
        
        if not files_to_process:
            print("No se encontraron archivos Markdown para procesar")
            return 1
        
        print(f"\nProcesando {len(files_to_process)} archivo(s)...\n")
        
        # Procesar archivos
        checker = APAChecker()
        results = []
        
        for filepath in files_to_process:
            print(f"Procesando: {filepath}")
            result = checker.process_file(filepath, args.output_suffix)
            results.append(result)
            
            if result['success'] and result['changes_made']:
                print(f"  ✓ Corregido → {result['output_path']}")
                print(f"  {result['errors_found']} problema(s) detectado(s)")
            elif result['success']:
                print(f"  ✓ Sin problemas")
            else:
                print(f"  ✗ Error: {result.get('error')}")
            print()
        
        # Generar reporte
        if not args.no_report:
            report_path = generate_report(results)
            print(f"\n📋 Reporte generado: {report_path}")
        
        # Resumen final
        successful = sum(1 for r in results if r['success'])
        with_changes = sum(1 for r in results if r.get('changes_made', False))
        
        print(f"\n{'='*60}")
        print(f"Resumen: {successful}/{len(results)} archivos procesados exitosamente")
        print(f"         {with_changes} archivo(s) con correcciones aplicadas")
        print(f"{'='*60}\n")
        
        return 0
        
    finally:
        # Limpiar directorio temporal si se creó
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)


if __name__ == '__main__':
    sys.exit(main())
