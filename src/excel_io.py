from __future__ import annotations
from pathlib import Path
import pandas as pd

# Columnas esperadas en el Excel maestro
EXPECTED_COLS = ["nombre", "cohorte", "ruta"]

# Lee el Excel maestro y devuelve un DataFrame normalizado
def read_master_excel(path: Path) -> pd.DataFrame:
    df = pd.read_excel(path, dtype=str).fillna("")
    # normaliza encabezados
    df.columns = [c.strip().lower() for c in df.columns]
    # reordena / filtra columnas esperadas (mantiene extra como ctes)
    missing = [c for c in EXPECTED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas en el Excel: {missing}. Debe incluir {EXPECTED_COLS}")
    return df[EXPECTED_COLS]

# Escribe un Excel para un coder específico
def write_coder_excel(row: pd.Series, path: Path) -> Path:
    df = row.to_frame().T  # una sola fila
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_excel(path, index=False)
    return path
