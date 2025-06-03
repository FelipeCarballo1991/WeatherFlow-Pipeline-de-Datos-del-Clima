from dotenv import load_dotenv
import os

load_dotenv()  # carga las variables del archivo .env

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
CIUDADES = ["Buenos Aires", "Madrid", "New York"]
