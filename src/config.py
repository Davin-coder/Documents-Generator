"""
src/config.py

Archivo que contiene las configuraciones del sistema.

Contiene las rutas de los archivos necesarios para la ejecución del sistema.

Rutas:
- excel_master: Ruta al archivo Excel maestro.
- word_template: Ruta a la plantilla de Word.
- out_dir: Ruta al directorio de salida donde se guardarán los archivos generados.

Importaciones:
- from dataclasses import dataclass: Permite la creación de clases de datos.
- from pathlib import Path: Proporciona una forma orientada a objetos de manejar rutas de sistema de archivos.
"""

from dataclasses import dataclass # dataclass es un decorador que se utiliza para crear clases de datos inmutables y con menos código boilerplate.
from pathlib import Path # Path es una clase que representa rutas de sistema de archivos de manera orientada a objetos.

@dataclass(frozen=True)
class Settings:
    excel_master: Path
    word_template: Path
    out_dir: Path
