"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    resultado = 0
    with open ('files/input/data.csv', 'r') as file:
        for linea in file:
            columna = linea.strip().split('\t')
            valor = int(columna[1])
            resultado += valor
    return resultado
    """
    Retorne la suma de la segunda columna.
    
    Rta/
    214

    """
print (pregunta_01())
