import pandas as pd

STUDENT_AGES_PATH = "student_ages.csv"

AGES = [
    19, 29, 19, 22, 23, 19, 30, 19, 19, 19, 20, 20, 20, 18, 22, 19, 34, 
    34, 21, 21, 22, 28, 29, 19, 20, 19, 25, 28, 21, 22
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
    if not data or not isinstance(data, list):
        raise ValueError("Los datos deben estar dispuestos en una lista.")

    if len(data) == 0:
        raise ValueError("La lista no puede estar vacía.")

    for elem in data:
        if not isinstance(elem, float) and not isinstance(elem, int):
            raise ValueError(
                "Los elementos de la lista deben ser de tipo real.")

    # Convertimos la lista a un DataFrame para acceder
    # a los métodos de pandas.
    data_frame = pd.DataFrame(data, columns=["data"])

    # Creamos un DataFrame vacío para comenzar a construir la tabla
    table = pd.DataFrame()

    # Para calcular la frecuencia absoluta, agrupamos los valores
    # iguales y tomamos el tamaño de cada grupo.
    table["fi"] = data_frame.groupby("data").size()

    # Calculamos el resto de frecuencias.
    table["Fi"] = table["fi"].cumsum()
    table["ri"] = table["fi"] / (table["fi"].sum())
    table["Ri"] = table["ri"].cumsum()
    table["pi"] = table["ri"] * 100
    table["Pi"] = table["Ri"] * 100

    return table


def main():
    # Para demostrar el funcionamiento de `analisis_estadistico`,
    # usamos datos de las edades de compañeros del instituto.
    print(analisis_estadistico(AGES))


if __name__ == "__main__":
    main()
