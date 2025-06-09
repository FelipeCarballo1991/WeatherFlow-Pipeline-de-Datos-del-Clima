# etl/transform.py
import pandas as pd
from datetime import datetime

def transformar_clima(data):
    fila = {
        "ciudad": data["name"],
        "pais": data["sys"]["country"],
        "fecha": datetime.fromtimestamp(data["dt"]).strftime("%Y-%m-%d %H:%M:%S"),
        "temperatura": data["main"]["temp"],
        "humedad": data["main"]["humidity"],
        "clima": data["weather"][0]["description"],
        "viento_kph": data["wind"]["speed"] * 3.6  # m/s a km/h
    }

    return pd.DataFrame([fila])
