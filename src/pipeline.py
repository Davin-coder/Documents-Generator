"""
src/pipeline.py

Archivo que contiene la lógica principal para procesar el archivo Excel maestro y generar los documentos necesarios.

Funciones:
- process_all: Procesa todos los registros del Excel maestro y genera los archivos correspondientes.

Importaciones:
- from __future__ import annotations: Permite el uso de anotaciones de tipo futuras.
- from pathlib import Path: Proporciona una forma orientada a objetos de manejar rutas de sistema de archivos.
- from typing import Iterable: Proporciona soporte para anotaciones de tipo genéricas.
- from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn: Permite mostrar barras de progreso en la consola.
- from rich.console import Console: Proporciona una consola enriquecida para la salida de texto.

- from excel_io import read_master_excel, write_coder_excel: Funciones para leer y escribir archivos Excel.
- from word_generator import render_word: Función para generar documentos de Word.
- from file_ops import ensure_dir, safe_folder_name: Funciones para operaciones de archivos y manejo de nombres seguros.
"""

from __future__ import annotations
from pathlib import Path
from typing import Iterable
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn
from rich.console import Console

from excel_io import read_master_excel, write_coder_excel
from word_generator import render_word
from file_ops import ensure_dir, safe_folder_name

console = Console()

def process_all(excel_path: Path, template_path: Path, out_dir: Path) -> None:
    console.rule("[bold]Generando documentos por persona")
    df = read_master_excel(excel_path)
    ensure_dir(out_dir)

    progress = Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total}"),
        TimeElapsedColumn(),
        console=console,
    )
    with progress:
        task = progress.add_task("Procesando", total=len(df))
        for _, row in df.iterrows():
            nombre = row["nombre"].strip() or "Sin nombre"
            carpeta = out_dir / safe_folder_name(nombre)
            ensure_dir(carpeta)

            # 1) Excel individual
            excel_out = carpeta / f"{safe_folder_name(nombre)}.xlsx"
            write_coder_excel(row, excel_out)

            # 2) Word desde plantilla
            context = {
                "nombre": row["nombre"],
                "cohorte": row["cohorte"],
                "ruta": row["ruta"],
            }
            word_out = carpeta / f"{safe_folder_name(nombre)}.docx"
            render_word(template_path, context, word_out)

            progress.advance(task)

    console.print("[green]Listo.[/green] Archivos generados en:", out_dir)
