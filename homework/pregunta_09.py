"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():

    resultado = {}
    with open ('files/input/data.csv' , 'r') as file:
        for linea in file:
            columnas = linea.strip().split('\t')
            linea = columnas[4].split(',')
            for l in linea:
                clave = l.split(':')[0]
                if clave in resultado:
                    resultado[clave] +=1
                else:
                    resultado[clave] = 1
            
           
        return dict(sorted(resultado.items()))
    
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
print(pregunta_09())
