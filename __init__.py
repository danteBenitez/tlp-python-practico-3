import pandas as pd

AGES = [
    32, 26, 28, 33, 32, 21, 28, 24, 24, 26, 25, 30, 28, 25, 26, 26, 30, 24, 26, 21,
    18, 27, 28, 22, 34, 19, 25, 24, 31, 30
]

def analisis_estadistico(data: list[float | int]) -> pd.DataFrame:
    """
        Toma una lista de valores numéricos y devuelve un DataFrame de 
        pandas con las siguientes columnas:
            - x: Los valores únicos de la lista.
            - fi: La frecuencia absoluta de cada valor
            - Fi: La frecuencia acumulada
            - ri: La frecuencia relativa
            - Ri: La frecuencia relativa acumulada
            - pi: La frecuencia porcentual
            - Pi: La frecuencia porcentual acumulada.
    """

    # Convertimos la lista a un DataFrame para acceder
    # a los métodos de pandas.
    data_frame = pd.DataFrame(data)

    # Creamos un DataFrame vacío para crear la tabla
    table = pd.DataFrame() 

    # Para encontrar los valores de x, ordenamos los datos
    # y sólo contamos valores únicos.
    table["x"] = data_frame[0].sort_values(ascending=True).unique()

    # Para calcular la frecuencia absoluta, agrupamos los valores
    # iguales y tomamos el tamaño de cada grupo.
    table["fi"] = data_frame.groupby(0).size().values

    # Calculamos el resto de frecuencias.
    table["Fi"] = table["fi"].cumsum()
    table["fr"] = table["fi"] / (table["fi"].sum())
    table["Fr"] = table["fr"].cumsum()
    table["pi%"] = table["fr"] * 100
    table["Pi%"] = table["Fr"] * 100
    
    return table

print(analisis_estadistico(AGES).to_markdown())