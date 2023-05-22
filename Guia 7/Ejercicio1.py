import math

def raizDe2() -> float:
    return round(math.sqrt(2), 2)

def imprimir_hola():
    print("Hola mundo")

def imprimir_verso():
    print("Sean bienvenidos a este planeta\nDonde la locura se adueñara de ti\nDonde no saldrás cuerdo\nSean bienvenidos a este planeta Vegetta")

def factorial_de_dos() -> int:
    return 2*1

def factorial_de_tres() -> int:
    return 3*2*1

def factorial_de_cuatro() -> int:
    return 4*3*2*1

def factorial_de_cinco() -> int:
    return 5*4*3*2*1

def factorial_como_la_gente(numero: int) -> int:
    factorial = 1
    for factor in range(1, (numero+1),1):
        factorial *= factor
    return factorial

print(str(factorial_como_la_gente(3)))
    