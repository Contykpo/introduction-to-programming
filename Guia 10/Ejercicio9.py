import random
from typing import List

from queue import LifoQueue

def armarPila(lista: List[int]) -> LifoQueue[int]:
    print(str(lista))
    pila = LifoQueue(maxsize=len(lista))
    for numero in lista:
        pila.put(numero)
    return pila

def generarNrosAlAzar(n: int, desde : int, hasta: int) -> List[int]:
    lista: List[int] = []
    for iterador in range(0,n,1):
        lista.append(random.randrange(desde,hasta))
    return lista

print(str(armarPila(generarNrosAlAzar(4,1,10))))