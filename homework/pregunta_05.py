"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():

    resultado = []

    with open ('files\input\data.csv', 'r') as file:
        for line in file:
            columnas = line.strip().split('\t')
            clave = columnas[0]
            valor = int(columnas[1])
            if clave in [t[0] for t in resultado]:
                for i, t in enumerate(resultado):
                    if t[0] == clave:
                        if valor > t[1]:
                            resultado[i] = (clave, valor, t[2])
                        if valor < t[2]:
                            resultado[i] = (clave, t[1], valor)
            else:
                resultado.append((clave, valor, valor))
    
    return sorted(resultado)
        
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """


print(pregunta_05())

