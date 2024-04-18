# Trabajo Práctico N°3

## Descripción

### Objetivo:
- El objetivo de este ejercicio es crear una función en python que tome como entrada una lista de edades de 30 alumnos del curso de segundo año de la tecnicatura superior en desarrollo de software multiplataforma y generar un análisis estadístico básico, calculando la frecuencia absoluta (fi), la frecuencia acumulada (Fi), la frecuencia relativa (ri), la frecuencia relativa acumulada (Ri), la probabilidad (pi) y la probabilidad acumulada (Pi). 
- Instrucciones:
    - Define una función llamada “analisis_estadistico” que acepte como parámetro una lista de valores numéricos. Implementa el cálculo de las siguientes columnas:
        - fi: Frecuencia absoluta de cada valor en la lista. 
        - Fi: Frecuencia acumulada, es decir, la suma acumulada de las frecuencias absolutas.
        - ri: Frecuencia relativa, que se calcula dividiendo la frecuencia absoluta de cada valor entre el tamaño total de la muestra. 
        - Ri: Frecuencia relativa acumulada, la suma acumulada de las frecuencias relativas.
        - pi: Probabilidad, que se obtiene dividiendo la frecuencia absoluta de cada valor entre el tamaño total de la muestra. 
        - Pi: Probabilidad acumulada, la suma acumulada de las probabilidades. Se debe devolver un dataframe que contenga estas columnas como claves y las listas correspondientes como valores asociados. 

### Criterios de evaluación:
- *Función analisis_estadistico*: La función debe tener el nombre exacto “analisis_estadistico” y aceptar una lista de valores numéricos como parámetro. 

- *Dato de retorno*: Se debe devolver el Dataframe con el contenido solicitado.

- *Diccionario de salida*: La función debe devolver un diccionario con las siguientes claves y sus correspondientes valores:
    - 'fi': Lista de frecuencias absolutas.
    - 'Fi': Lista de frecuencias acumuladas.
    - 'ri': Lista de frecuencias relativas.
    - 'Ri': Lista de frecuencias relativas acumuladas.
    - 'pi': Lista de probabilidades.
    - 'Pi': Lista de probabilidades acumuladas. 

- *Manejo de casos especiales*: La función debe manejar adecuadamente casos donde la lista de valores esté vacía, no contenga elementos no numéricos o no sea una lista en concreto.

- *Comentarios*: Se deben incluir comentarios en el código para explicar qué hace cada parte de la función. 

### Presentación del Trabajo Práctico:

LA PRESENTACIÓN DEL TRABAJO PRÁCTICO DEBE REALIZARSE EN UN
REPOSITORIO DE “GITHUB”, EL CUAL DEBE SER PÚBLICO PARA SU
POSTERIOR REVISIÓN Y EVALUACIÓN.

## Sobre el trabajo

- Para ejecutar el proyecto, primero instale las dependencias:

```bash
$ pip install -r requirements.txt
```

- Luego ejecute el siguiente comando:

```bash
$ python3 __init__.py
```

