"""
src/word_generator.py

Archivo que contiene la lógica para generar documentos de Word a partir de una plantilla y datos proporcionados.

Funciones:
- render_word: Genera un documento de Word basado en una plantilla y un contexto de datos.

Importaciones:
- from __future__ import annotations: Permite el uso de anotaciones de tipo futuras.
- from pathlib import Path: Proporciona una forma orientada a objetos de manejar rutas de sistema de archivos.
- from docxtpl import DocxTemplate: Permite trabajar con plantillas de documentos Word (.docx).
"""

from __future__ import annotations
from pathlib import Path
from docxtpl import DocxTemplate

def render_word(template_path: Path, context: dict, out_path: Path) -> Path:
    tpl = DocxTemplate(str(template_path))
    tpl.render(context)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tpl.save(str(out_path))
    return out_path
