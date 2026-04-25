"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    
    parejas = []
    resultado = []
    with open ('files\\input\\data.csv', 'r') as file:
        for line in file:
            columnas = line.strip().split('\t')
            letras = columnas[0]
            parejas.extend((letra, 1) for letra in letras)
            parejas = sorted(parejas)

        for key, value in parejas:
                if resultado and resultado[-1][0] == key:
                 resultado[-1] = (key, resultado[-1][1] + value)
                else:
                 resultado.append((key, value))
        return resultado   
    
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordenadas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

print(pregunta_02())


