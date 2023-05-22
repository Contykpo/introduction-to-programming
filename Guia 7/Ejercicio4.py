def peso_pino(alturaEnCentimetros: int) -> int:
    if (alturaEnCentimetros <= 300):
        return 3*alturaEnCentimetros
    else:
        return 900 + (alturaEnCentimetros-300)*2

def es_peso_util(peso: int) -> int:
    return peso >= 400 and peso <= 1000

def sirve_pino(alturaEnCentimetros: int):
    if es_peso_util(peso_pino(alturaEnCentimetros)):
        print("El pino le sirve a la fabrica")
    else:
        print("El pino no le sirve a la fabrica")
