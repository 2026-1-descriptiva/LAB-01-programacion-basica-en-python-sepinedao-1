"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_12():

    resultado = {}
    with open('files/input/data.csv', 'r') as file:
        for linea in file:
            columnas = linea.strip().split('\t')
            clave = columnas[0]
            pares = columnas[4].split(',')
            valor = sum(int(par.split(':')[1]) for par in pares) 
            if clave in resultado:
                resultado[clave] += valor
            else:
                resultado[clave] = valor
    return dict(sorted(resultado.items()))

    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
print(pregunta_12())
