"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    parejas = []
    resultado = []
    with open ('files\\input\\data.csv', 'r') as file:
        for line in file:
            columnas = line.strip().split('\t')
            letras = columnas[0]
            valor = int(columnas[1])
            parejas.extend((letra, valor) for letra in letras)
            parejas = sorted(parejas)

        for key, value in parejas:
                if resultado and resultado[-1][0] == key:
                 resultado[-1] = (key, resultado[-1][1] + value)
                else:
                 resultado.append((key, value))
        return resultado
    
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

print(pregunta_03())  