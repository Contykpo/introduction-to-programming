import math

def imprimir_saludo(nombre: str):
    print("Holis "+nombre+" por pantalla")

def raiz_cuadrada_de(numero: int) -> float:
    return round(math.sqrt(numero), 2)

def imprimir_dos_veces(estribillo: str):
    print(estribillo*2)

def es_multiplo_de(multiplo: int, numero: int) -> bool:
    if (multiplo % numero == 0):
        return True
    else:
        return False
    
def es_par(numero: int) -> bool:
    return numero % 2 == 0

def cantidad_de_pizzas(comensales: int, minimasPorciones: int) -> int:
    return math.ceil(comensales*minimasPorciones / 8)