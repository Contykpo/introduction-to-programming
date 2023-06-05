from queue import Queue
from typing import List

import random

def armarColaEnteros(listaEnteros: List[int]) -> Queue[int]:
    colaEnteros = Queue(maxsize=len(listaEnteros))
    for entero in listaEnteros:
        colaEnteros.put(entero)
    return colaEnteros


def generarNumeroAlAzar(cantidad:int, desde:int, hasta:int) -> List[int]:
    lista: List[int] = []
    for iterador in range(0,cantidad,1):
        lista.append(random.randrange(desde,hasta))
    print(str(lista))
    return lista

colaEnteros = armarColaEnteros(generarNumeroAlAzar(4,1,10))

for iterador in range(0, colaEnteros.qsize(),1):
    print(colaEnteros.get())