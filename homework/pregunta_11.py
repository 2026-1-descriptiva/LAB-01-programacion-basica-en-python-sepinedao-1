"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_11():

    resultado = {}
    with open ('files/input/data.csv', 'r') as file:
        for line in file:
            columnas = line.strip().split('\t')
            valor = int(columnas[1])
            letras = columnas[3]
            letra = letras.split(',')

            for l in letra:
               if l in resultado:
                    resultado[l] += valor
               else:
                    resultado[l] = valor
                    
        return dict(sorted(resultado.items()))

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
print(pregunta_11())
