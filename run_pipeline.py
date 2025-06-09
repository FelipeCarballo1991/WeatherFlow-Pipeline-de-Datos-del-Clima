from etl.extract import obtener_clima
from etl.transform import transformar_clima
from etl.load import guardar_json_crudo
import os

ciudad = "Buenos Aires"
datos = obtener_clima(ciudad)

if datos:
    guardar_json_crudo(datos, ciudad)

    df = transformar_clima(datos)
    print("\n📋 Datos transformados:")
    print(df)

    # Asegurar que la carpeta processed exista
    ruta_carpeta = "data/processed"
    os.makedirs(ruta_carpeta, exist_ok=True)

    # Guardar como CSV
    df.to_csv(f"{ruta_carpeta}/{ciudad.lower().replace(' ', '_')}_clima.csv", mode='a', index=False, header=False)
