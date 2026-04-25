"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():


    resultado = []

    with open ('files/input/data.csv', 'r') as file:
        for line in file:
            columnas = line.strip().split('\t')
            parejas = columnas[4].split(',')
        

            for par in parejas:
                clave = par.split(':')[0]
                valor = int(par.split(':')[1])
                if clave in [t[0] for t in resultado]:
                    for i, t in enumerate(resultado):
                       if t[0] == clave:
                            minimo = t[1]
                            maximo = t[2]
                            if valor < minimo:
                                minimo = valor
                            if valor > maximo:
                                maximo = valor
                            resultado[i] = (clave, minimo, maximo)
                else:
                    resultado.append((clave, valor, valor))

    return sorted(resultado)
    
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
print(pregunta_06())
