import requests
import pandas as pd

# Definición de los parametros a emplear para extraer los datos.
params = {
    'dataset': 'daily-summaries',
    'startDate': '1957-06-30', # Periodo - Inicio
    'endDate': '2024-07-02', # Periodo - final
    'stations': 'AR000087418',  # Mendoza Aereo
    'format': 'json',
    'includeStationName': 'true',
}

# Dirección web de la cual obtenemos los datos
url = "https://www.ncei.noaa.gov/access/services/data/v1"

# Respuesta de la api de la NCEI
response=requests.get(url,params=params)

# Lectura de la respuesta en formato JSON
if response.status_code==200:
    info=response.json()
else:
    print(f"Estatus data 1:-> {response.status_code}")

#Transformación en dataframe de pandas
data=pd.DataFrame(info)

# guardar datos en csv
data.to_csv("../data/raw/clima_raw.csv")