from queue import LifoQueue as Pila

from typing import List

def buscarMaximo(pila: Pila) -> int:
    lista: List[int] = []
    for iterador in range(0,pila.qsize(),1):
        lista.append(pila.get())
    # Ahora si busco el maximo dentro de la lista creada con los mismos elementos de la pila.
    maximo:int = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

pilita = Pila(maxsize=3)

pilita.put(3)
pilita.put(9)
pilita.put(8)

print(str(buscarMaximo(pilita)))
