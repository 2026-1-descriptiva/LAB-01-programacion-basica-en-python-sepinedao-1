"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():


    with open ('files\input\data.csv', 'r') as file:
        acumulado = {}
        resultado = []
       
        for line in file:
            columnas = line.strip().split('\t')
            clave = columnas[1]
            letra = list(columnas[0])

            if clave not in acumulado:
                acumulado[clave]= []
            
            if letra not in acumulado[clave]:
                acumulado[clave].append(letra)
        
        for clave in acumulado.keys():
            resultado.append((clave, sorted(acumulado[clave])))
        
        return sorted(resultado)
            
  
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """

print(pregunta_08())