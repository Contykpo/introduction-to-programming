from random import choice

# 1
def armar_lista_con_nombres_solicitados() -> list:
    listaDeNombres: list = list()
    while True:
        print("Escriba un nombre o la palbra listo para terminar")
        entrada = input()
        if (entrada.lower() == "listo"):
            break
        listaDeNombres.append(entrada)
    return listaDeNombres

# 2

def historial_de_movimientos() -> list:
    historial: list = list()
    while True:
        print("C: Cargar creditos.")
        print("D: Descontar creditos.")
        print("X: Finalizar operacion.")
        entrada = input()
        if entrada.upper() == "C":
            print("Escriba el monto que desea cargar:")
            entradaMonto = input()
            historial.append((entrada, entradaMonto))
        elif entrada.upper() == "D":
            print("Escriba el monto que desea descontar:")
            entradaMonto = input()
            historial.append((entrada, entradaMonto))
        elif entrada.upper() == "X":
            break
    return historial

# 3

def jugar_7_y_medio() -> list:
    historial: list = list()
    puntuacion: int = 0
    while True:
        numero: int = choice([i for i in range(1,12) if i not in [8,9]])
        print("S: Sacar otra carta.")
        print("P: Plantarse.")
        entrada = input()
        if entrada.upper() == "S":
            historial.append((entrada, numero))
            if numero < 10:
                puntuacion += numero
            else:
                puntuacion += 1.5
                
            if puntuacion >= 7.5:
                print("Has perdido, con un puntaje de: " + str(puntuacion))
                break
        elif entrada.upper() == "P":
            break
    return historial

print(str(jugar_7_y_medio()))