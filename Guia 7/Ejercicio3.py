def alguno_es_0(numero1, numero2) -> bool:
    return numero1 == 0 or numero2 == 0

def ambos_son_0(numero1, numero2) -> bool:
    return numero1 == 0 and numero2 == 0

def es_nombre_largo(nombre: str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8

def es_bisiesto(año: int) -> bool:
    return año % 400 == 0 or (año % 100 != 0 and año % 4 == 0)