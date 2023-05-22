import numpy

from typing import Iterable

# 1

def pertenece_a_cada_uno(listaDeListas: list, elemento) -> bool:
    validacion: int = 0
    for lista in listaDeListas:
        if elemento in lista:
            validacion += 1
    return validacion == len(listaDeListas)

# 2

def es_matriz(listaDeListas: list) -> bool:
    alarma: int = 0
    if len(listaDeListas) > 0 and len(listaDeListas[0]) > 0:
        for iterator in range(1,len(listaDeListas),1):
            if len(listaDeListas[iterator]) != len(listaDeListas[0]):
                alarma += 1
    else:
        return False
    return alarma == 0

# 3

def filas_ordenadas(listaDeListas: list) -> list:
    sonOrdenadas: list = list()
    for lista in listaDeListas:
        sonOrdenadas.append(ordenados(lista))
    return sonOrdenadas

def ordenados(lista) -> bool:
    alerta: int = 0
    i = 1
    while i < len(lista):
        if (lista[i] < lista[i - 1]):
            alerta = 1
        i += 1
    return alerta < 1

# 4

def multiplicar_matriz_generada_al_azar(dimensionesMatriz: int, potencia: int) -> list:
    matriz: list = numpy.random.random((dimensionesMatriz, dimensionesMatriz))
    nuevaMatriz = numpy.empty((dimensionesMatriz,dimensionesMatriz))
    for iterador in range(1,potencia+1,1):
        # Iteramos por las filas de la primer matriz.
        for i in range(len(matriz)):
            # Iteramos por las columnas de la segunda matriz.
            for j in range(len(matriz[0])):
                # Iteramos por las filas de la segunda matriz.
                for k in range(len(matriz)):
                    nuevaMatriz[i][j] += matriz[i][k] * matriz[k][j]
    return nuevaMatriz

def multiplicar_matriz_generada_al_azar_2(dimensionesMatriz: int, potencia: int) -> list:
    matriz: list = numpy.random.random((dimensionesMatriz, dimensionesMatriz))**potencia
    return matriz


print(str(multiplicar_matriz_generada_al_azar(3, 2)))
print(str(multiplicar_matriz_generada_al_azar_2(3, 2.5)))
