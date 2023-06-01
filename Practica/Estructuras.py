# Simulador de cocina restaurante:

# TODO: Actualizar el programa para permitir la generacion de recibos archivos de texto para cada cliente _
# TODO: _ y por ultimo un resumen del dia para la administracion del restaurante.

# Tambien estaria bueno especificar el programa final en el cuaderno y escribir una pequeña test-suite.

from typing import Tuple

from typing import List
from typing import Dict

from queue import Queue
from queue import LifoQueue

opcionMenu: List[str] = ["Pizzas", "Empanadas", "Hamburguesas"]

menuPizzas: Dict[str, int] = { "Muzzarella" : 1600, "Probolone" : 1240, "Anana" : 1640 }
menuEmpanadas: Dict[str, int] = { "JYQ" : 220, "Carne" : 250, "Cebolla" : 200 }
menuHamburguesas: Dict[str, int] = { "Completa" : 2100, "Colon" : 2540, "BigColon" : 2840 }

hambrientos: List[str] = ["Bigote", "Samurai", "Charley", "Eber"]
def cargarClientes(clients: List[str]) -> Queue[str]:
    clientes = Queue(maxsize=4)
    for cliente in clients:
        clientes.put(cliente)
    return clientes


def administracionRestaurante(comensales: Queue[str]) -> List[Tuple[str, str, int]]:
    comensalesNoAtentidos: Queue[str] = comensales
    reporte: List[Tuple[str, str, int]] = []
    while not comensalesNoAtentidos.empty():
        comensal:str = comensalesNoAtentidos.get()
        reporte.append(atenderComensal(comensal))
    return reporte


def atenderComensal(comensal: str) -> Tuple[str, str, int]:
    print("Muy buenos dias, que desea ordenar de nuestro menu?\n"+str(opcionMenu)+"\nEscriba su opcion")
    opcion = input()
    if opcion == "Pizzas":
        print("\nQue pizza deseas?\n"+str(menuPizzas)+"\nEscriba su opcion\n")
        pizza = input()
        if pizza in menuPizzas.keys():
            print("\nAhi va una "+pizza+" flaque\n")
            return (comensal, pizza, menuPizzas.get(pizza))
        else:
            print("\nNo se que hayas querido decir, pero te quedaste sin pizza.")
    elif opcion == "Empanadas":
        print("\nQue empanada deseas?\n"+str(menuEmpanadas)+"\nEscriba su opcion\n")
        empanada = input()
        if empanada in menuEmpanadas.keys():
            print("\nAhi va una "+empanada+" flaque\n")
            return (comensal, empanada, menuEmpanadas.get(empanada))
        else:
            print("\nNo se que hayas querido decir, pero te quedaste sin empanadas.")
    elif opcion == "Hamburguesas":
        print("\nQue hamburguesa deseas?\n"+str(menuHamburguesas)+"\nEscriba su opcion\n")
        borgor = input()
        if borgor in menuHamburguesas.keys():
            print("\nAhi va una "+borgor+" flaque\n")
            return (comensal, borgor, menuHamburguesas.get(borgor))
        else:
            print("\nNo se que hayas querido decir, pero te quedaste sin hamburguesas.")
    return (comensal, "no pidio nada", 0)


print("El reporte del dia de hoy es:\n"+str(administracionRestaurante(cargarClientes(hambrientos))))