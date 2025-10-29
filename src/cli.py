from __future__ import annotations
from pathlib import Path
import typer
from rich import print

from pipeline import process_all

app = typer.Typer(add_completion=False)

# Definición del comando principal
@app.command()
def run(
    excel: Path = typer.Option(..., help="Ruta al Excel maestro (coders.xlsx)"),
    template: Path = typer.Option(..., help="Ruta a la plantilla .docx con placeholders Jinja"),
    out: Path = typer.Option(Path("data/output"), help="Carpeta de salida"),
):
    # Procesa el Excel y genera carpetas + Excel/Word por persona.
    process_all(excel, template, out)

if __name__ == "__main__":
    app()
