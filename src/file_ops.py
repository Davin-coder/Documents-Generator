from pathlib import Path
from slugify import slugify

def safe_folder_name(name: str) -> str:
    # normaliza nombres con acentos/espacios y evita caracteres prohibidos
    return slugify(name, lowercase=False, separator=" ")

def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path
