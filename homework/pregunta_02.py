"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    
    parejas = []
    resultado = []
    with open ('files/input/data.csv', 'r') as file:
        for linea in file:
            columna = linea.strip().split('\t')
            letras = columna[0]
            for letra in letras:
                parejas.append((letra, 1))
            parejas = sorted(parejas)

        for clave, valor in parejas:
                if resultado and resultado[-1][0] == clave:
                 resultado[-1] = (clave, resultado[-1][1] + valor)
                else:
                 resultado.append((clave, valor))
        return resultado   
    
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordenadas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

print(pregunta_02())


