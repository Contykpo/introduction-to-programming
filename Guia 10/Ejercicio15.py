from queue import Queue
from typing import List

def buscarMaximo(cola: Queue[int]) -> int:
    listaEnteros: List[int] = []
    maximo: int = 0
    for iterador in range(0,cola.qsize(),1):
        listaEnteros.append(cola.get())
    for numero in listaEnteros:
        if numero > maximo:
            maximo = numero
    return maximo

colita: Queue[int] = Queue(maxsize=4)
colita.put(1)
colita.put(5)
colita.put(2)
colita.put(8)

print(str(buscarMaximo(colita)))