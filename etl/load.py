# etl/load.py
import os
import json
from datetime import datetime

def guardar_json_crudo(data, ciudad):
    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    carpeta = f"data/raw/{ciudad.lower().replace(' ', '_')}"
    os.makedirs(carpeta, exist_ok=True)
    ruta = f"{carpeta}/{fecha}.json"

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ JSON guardado en {ruta}")
