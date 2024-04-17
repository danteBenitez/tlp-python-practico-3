import pandas as pd

STUDENT_AGES_PATH = "student_ages.csv"

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
    if not data or not isinstance(data, list):
        raise ValueError("Los datos deben estar dispuestos en una lista.")

    if len(data) == 0:
        raise ValueError("La lista no puede estar vacía.")
    
    for elem in data:
        if isinstance(elem, float):
            raise ValueError("Los elementos de la lista deben ser de tipo real.")

    # Convertimos la lista a un DataFrame para acceder
    # a los métodos de pandas.
    data_frame = pd.DataFrame(data)

    # Creamos un DataFrame vacío para comenzar a construir la tabla
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

def main():
    # Para demostrar el funcionamiento de `analisis_estadistico`,
    # usamos datos de un CSV.
    csv_data_frame = pd.read_csv(STUDENT_AGES_PATH, names=["Nombre", "Edad"], header=None)

    print(analisis_estadistico(csv_data_frame["Edad"].values.tolist()))

if __name__ == "__main__":
    main()
