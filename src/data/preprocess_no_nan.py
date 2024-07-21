import pandas as pd

# Iniciar el dataset
data = pd.read_csv("../data/raw/clima_raw.csv")

# Transformar datos de la columna 'DATE' en tipo datetime
data['DATE'] = pd.to_datetime(data['DATE'])

# Transformar datos de las columnas 'TAVG', 'TMIN', 'TMAX', 'PRCP', 'SNWD' en tipo numérico
numeric_columns = ['TAVG', 'TMIN', 'TMAX', 'PRCP', 'SNWD']
for i in numeric_columns:
    data[i] = data[i].map(lambda x: (float(x)/10))

# Cambiar la posición de las columnas del dataset
data = data[['NAME', 'STATION', 'DATE', 'TMIN', 'TMAX', 'TAVG', 'PRCP', 'SNWD']]

# Dataset eliminando NaN
no_nan_data = data[["DATE",	"TMIN", "TMAX", "TAVG", "PRCP", "SNWD"]]

# Eliminar las columna 'SNWD'
no_nan_data.drop(['SNWD'], axis=1, inplace=True)

# Eliminar demás datos NaN
no_nan_data = no_nan_data.dropna()

# Desglozamos la columna DATE para tener una mejor perspectiva predictiva
no_nan_data['year'] = no_nan_data['DATE'].dt.year
no_nan_data['month'] = no_nan_data['DATE'].dt.month
no_nan_data['day'] = no_nan_data['DATE'].dt.day

# Cambiamos la posición de las columnas
no_nan_data = no_nan_data[["DATE", "year", "month", "day", "TMIN", "TMAX", "TAVG", "PRCP"]]

# Cambiar los nombres de las columnas
no_nan_data.rename(columns={'DATE':'date', 'TMIN':'tmin(°C)', 'TMAX':'tmax(°C)', 'TAVG':'tavg(°C)', 'PRCP':'precipitaciones(mm)'}, inplace=True)

# Guardar el dataset como archivo csv
no_nan_data.to_csv("../data/processed/preprocessed_clima_non_nan.csv")