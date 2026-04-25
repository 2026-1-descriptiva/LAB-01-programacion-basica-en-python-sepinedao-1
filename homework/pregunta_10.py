"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():

    resultado = []
    with open ('files/input/data.csv' , 'r') as file:
        for line in file:
            columnas = line.strip().split('\t')
            clave = columnas[0]
            columnas[3]=columnas[3].split(',')
            columnas[4]=columnas[4].split(',')
            valor1= len(columnas[3])
            valor2= len(columnas[4])
            resultado.append((clave, valor1, valor2))
        return resultado

    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
print(pregunta_10())
