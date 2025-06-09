# etl/extract.py

import requests
from config import API_KEY
import certifi

def obtener_clima(ciudad, pais="AR"):
    # url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={API_KEY}&units=metric&lang=es"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
    respuesta = requests.get(url,verify=certifi.where())

    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos
    else:
        print(f"❌ Error {respuesta.status_code}: {respuesta.text}")
        return None
