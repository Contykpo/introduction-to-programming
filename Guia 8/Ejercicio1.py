from typing import Iterable

# 1
def pertenece(elemento, lista) -> bool:
    return  elemento in lista

def perteneceFor(elemento: int, lista) -> bool:
    for element in lista:
        if (elemento == element):
            return True
        else:
            return False

def perteneceIf(elemento: int, lista) -> bool:
    if elemento in lista:
        return True
    else:
        return False

# Las primer funcion pertence puede utilizarse para buscar caracteres en un string que requerirse, ya que se estan utilizando tipos genericos en sus parametros.

# 2

def divideATodos(numero, lista) -> bool:
    for numerador in lista:
        if (numerador % numero != 0):
            return False
    return True

# 3

def sumaTotal(lista) -> int:
    sumaElementos: int = 0
    for elmento in lista:
        sumaElementos += elmento
    return sumaElementos

# 4

def ordenados(lista) -> bool:
    alerta: int = 0
    i = 1
    while i < len(lista):
        if (lista[i] < lista[i - 1]):
            flag = 1
        i += 1
    return alerta < 1

# 5

def palabra_con_mas_de_7_caracteres(lista) -> bool:
    for palabra in lista:
        if palabra.len() >= 7:
            return True
        else:
            return False

# 6
def es_palindroma(palabra: str) -> bool:
    copy_ = palabra[::-1]
    if palabra == copy_:
        return True
    else:
        return False

# 7

def analizar_contrasenia(contrasenia: str) -> str:
    puntitosParaVerde: int = 0
    puntitosParaAmarilla: int = 0
    puntitosParaRoja: int = 0
    if len(contrasenia) >= 8:
        puntitosParaVerde = 1
    elif len(contrasenia) < 5:
        puntitosParaRoja = 1
    else:
        return "AMARILLA"
    for caracter in contrasenia:
        if caracter.isupper():
            puntitosParaVerde += 1
        else:
            puntitosParaVerde += 1
    if (puntitosParaVerde > puntitosParaRoja):
        return "VERDE"
    elif (puntitosParaRoja > puntitosParaVerde):
        return "ROJA"

# 8

def movimiento_bancario(historial: Iterable[tuple]) -> int:
    sumaDeIngresos: int = 0
    sumaDeSalidas: int = 0
    for movimiento in historial:
        if movimiento[0] == "I":
            sumaDeIngresos += movimiento[1]
        elif movimiento[0] == "R":
            sumaDeSalidas += movimiento[1]
    return  sumaDeIngresos - sumaDeSalidas

# 9

def vocales_distintas_en_palabra(palabra: str) -> bool:
    listaDeVocales = ["a","A","e","E","i","I","o","O","u","U"]
    diferencia: int = 0
    for caracter in palabra:
        if caracter in listaDeVocales:
            listaDeVocales.remove(caracter.lower())
            listaDeVocales.remove(caracter.upper())
            diferencia += 1
    return diferencia >= 3

