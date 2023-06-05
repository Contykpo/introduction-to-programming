from queue import Queue
from typing import List

import random

def jugarCartonDeBingo(carton: List[int], bolillero: Queue[int]) -> int:
    bolitas: Queue[int] = bolillero
    cantidadDeJugadas: int = 0
    for iterador in range(0, bolitas.qsize(), 1):
        bolita = bolitas.get()
        if bolita in carton:
            cantidadDeJugadas += iterador - cantidadDeJugadas
    return cantidadDeJugadas

def armarSecuenciaBingo() -> Queue[int]:
    bolitas: Queue[int] = Queue(maxsize=100)
    for numero in random.sample(range(0,100), 100):
        bolitas.put(numero)
    return bolitas

def generarNumeroAlAzar(cantidad:int, desde:int, hasta:int) -> List[int]:
    lista: List[int] = []
    for iterador in range(0,cantidad,1):
        lista.append(random.randrange(desde,hasta))
    return lista

cartonsito = generarNumeroAlAzar(12, 0,100)
bolillerito = armarSecuenciaBingo()

print(str(jugarCartonDeBingo(cartonsito, bolillerito)))

print(str(cartonsito))