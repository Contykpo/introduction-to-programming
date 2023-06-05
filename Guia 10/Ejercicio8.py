import random
from typing import List

def generarNrosAlAzar(n: int, desde : int, hasta: int) -> List[int]:
    lista: List[int] = []
    for iterador in range(0,n,1):
        lista.append(random.randrange(desde,hasta))
    return lista


print(str(generarNrosAlAzar(4,1,10)))