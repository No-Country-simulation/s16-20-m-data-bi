# **Predicciones Climáticas para la Toma de Decisiones en Prácticas Vitivinícolas en la Región de Mendoza**

<img src="reports/figures/mendoza_vineyard.png">

## **Descripción del Proyecto**
Este proyecto tiene como objetivo desarrollar un modelo predictivo para condiciones climáticas específicas en la Región de Mendoza, Argentina, con el fin de optimizar las prácticas vitivinícolas. Utilizando datos climáticos históricos y técnicas avanzadas de Machine Learning, buscamos proporcionar a los viticultores herramientas precisas para la toma de decisiones informadas que mejoren la eficiencia y calidad de la producción de vino.

## **Puntos Claves del Proyecto**
- **Predicción Climática:** Desarrollar modelos predictivos para variables climáticas clave como temperatura mínima (TMIN), temperatura máxima (TMAX), temperatura promedio (TAVG), precipitación y nevadas.
- **Optimización de Prácticas Vitivinícolas:** Utilizar las predicciones climáticas para informar decisiones en aspectos críticos del cultivo de la vid.
- **Escalabilidad y Reproducibilidad:** Crear un flujo de trabajo escalable y reproducible que pueda ser aplicado a otras regiones vitivinícolas.

## **Metodología**
- **Recopilación de Datos:** Se obtuvieron datos climáticos de NOAA's National Centers for Environmental Information (NCEI) de la Provincia de Mendoza en Argentina, correspondiente a la estación `AR000087418`, correspondiente a la estación `AERO MENDOZA, AR`.
- **Análisis Exploratorio de Datos (EDA):** Se realizó un análisis exhaustivo para entender las características de los datos que puedan aportar a las prácticas de viticultura en la Región.
- **Desarrollo de Modelos Predictivos:** Se utilizaron técnicas de Machine Learning para predecir las condiciones climáticas para que aporten a la toma de decisiones en las prácticas vitivinicolas en la Región.
- **Implementación:** Se Creó una plataforma para que los agricultores puedan acceder a condiciones climáticas de la Región y predicción mediante el modelo desarrollado.

### **Tecnologías Utilizadas**
- **Lenguajes de Programación:** Python
- **Visualización de Datos:** Power BI
- **Herramientas de Gestión de Proyectos:** Trello, GitHub

### **Extracción de datos**
Para la extracción de datos se empleo la API del Centro NCEI, empleando el siguiente codigo:
```
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
```
Después de obtener el dataset, se realizó un pre-proceso de los datos, adicionando los datos de estaciones y ciclo fenológico con respecto a la Región de Mendoza.

### **Diccionario de Variables del Dataset**
| Variable          | Tipo        | Descripción                                     |
|-------------------|-------------|-------------------------------------------------|
| `date`            | Categórica  | Fecha en formato datetime                       |
| `year`            | Numérica    | Año                                             |
| `month`           | Numérica    | Mes                                             |
| `day`             | Numérica    | Día del mes                                     |
| `season`          | Categórica  | Estación del año (autumn, winter, spring, summer) |
| `phenology_cycle` | Categórica  | Ciclo fenológico (7 categorías diferentes)      |
| `tmin`            | Numérica    | Temperatura mínima                              |
| `tmax`            | Numérica    | Temperatura máxima                              |
| `tavg`            | Numérica    | Temperatura promedio                            |
| `precipitation`   | Numérica    | Precipitación (mm)                              |
| `snowfall`        | Numérica    | Nieve caída (mm)                                |

## **Resultados**
- Se observaron comportamiento normal en datos de Temperatura, con datos muy variados en variables de precipitaciones y nevadas:

<img src="reports/figures/analisis_variables.png">

- Se adicionaron dos variables categóricas que ayudan a enlazar las practicas vitivinícolas con las variables climáticas:

<img src="reports/figures/variables_categoricas.png">

- Obtenido el dataset y analizado se crea un dasboard para que los viticultores pueden tomar decisiones en base a diferentes vizualizaciones:
    #### ***Portada:***

    <img src="reports/dashboard/portada.png">

    #### ***Producción:***

    <img src="reports/dashboard/produccion.png">

    #### ***Clima:***

    <img src="reports/dashboard/clima.png">

    #### ***Se puede interactuar con el Dashboard en el siguiente enlace:***
    [Dashboard Interactivo](https://app.powerbi.com/view?r=eyJrIjoiZDFkN2RjMWQtMTZlOC00MTI4LTgwMTYtNjU4MTllODYzOTZkIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9)

### Predicciones
Mediante la implementación de modelo de Machine Learning se obtuvo un modelos de predicción Climatica obteniendo datos de 180 días.

<img src="reports/figures/prediccion_temp.png">

## **Como Contribuir**
Para contribuir a este proyecto, por favor sigue estos pasos:
- Haz un fork del repositorio.
- Crea una nueva rama `git checkout -b feature/nueva-caracteristica`
- Realiza tus cambios y haz commit `git commit -m 'Agrega nueva característica'`
- Empuja tu rama `git push origin feature/nueva-caracteristica`
- Abre un Pull Request.

## Contacto
Para preguntas o más información sobre el proyecto, puedes contactar a:
- **Arelys Acevedo** - *Data Analyst*
&nbsp;
[![Linkedin](https://i.sstatic.net/gVE0j.png) LinkedIn](https://www.linkedin.com/in/arelys-acevedo)
&nbsp;
[![GitHub](https://i.sstatic.net/tskMh.png) GitHub](https://github.com/acad2018)

- **Ariana Maldonado** - *Data Analyst*
&nbsp;
[![Linkedin](https://i.sstatic.net/gVE0j.png) LinkedIn](https://www.linkedin.com/in/AriMaldo19)
&nbsp;
[![GitHub](https://i.sstatic.net/tskMh.png) GitHub](https://github.com/AriMaldo19)

- **Brayan C'carita Cruz** - *Data Analyst*
&nbsp;
[![Linkedin](https://i.sstatic.net/gVE0j.png) LinkedIn](https://www.linkedin.com/in/arelys-acevedo)
&nbsp;
[![GitHub](https://i.sstatic.net/tskMh.png) GitHub](https://github.com/hallzyx)

- **Cecilia Aponte** - *Data Scienctist*
&nbsp;
[![Linkedin](https://i.sstatic.net/gVE0j.png) LinkedIn](https://www.linkedin.com/in/ceci-aponte-data)
&nbsp;
[![GitHub](https://i.sstatic.net/tskMh.png) GitHub](https://github.com/CCAponte)

- **Fidel Vera Chourio** - *Data Scientist*
&nbsp;
[![Linkedin](https://i.sstatic.net/gVE0j.png) LinkedIn](https://www.linkedin.com/in/fverachourio)
&nbsp;
[![GitHub](https://i.sstatic.net/tskMh.png) GitHub](https://github.com/fevc08)

- **Noe Machaca Chambilla** - *Data Analyst*
&nbsp;
[![Linkedin](https://i.sstatic.net/gVE0j.png) LinkedIn](https://www.linkedin.com/in/noe-u-machaca)
&nbsp;
[![GitHub](https://i.sstatic.net/tskMh.png) GitHub](https://github.com/newneo4)

- **Raul Almao** - *Data Scientist*
&nbsp;
[![Linkedin](https://i.sstatic.net/gVE0j.png) LinkedIn](https://www.linkedin.com/in/ralmao)
&nbsp;
[![GitHub](https://i.sstatic.net/tskMh.png) GitHub](https://github.com/Ralmao)
