"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    parejas = []
    resultado = []
    with open ('files/input/data.csv', 'r') as file:
        for linea in file:
            columnas = linea.strip().split('\t')
            letras = columnas[0]
            valor = int(columnas[1])
            for letra in letras:
                parejas.append((letra, valor))
            parejas = sorted(parejas)

        for clave, valor in parejas:
                if resultado and resultado[-1][0] == clave:
                 resultado[-1] = (clave, resultado[-1][1] + valor)
                else:
                 resultado.append((clave, valor))
        return resultado
    
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
print(pregunta_03())  
