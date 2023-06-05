from typing import List

def palabraMasFrecuente(nombreArchivo: str) -> str:
    archivo = open(nombreArchivo, "r")
    maximaAparicion: int = 0
    palabras: List[str] = []
    palabraFrecuente:str = ""
    for linea in archivo:
        for palabrita in linea.split():
            palabras.append(palabrita)
    for palabra in palabras:
        if palabras.count(palabra) > maximaAparicion:
            maximaAparicion = palabras.count(palabra)
            palabraFrecuente = palabra
    return palabraFrecuente


print(str(palabraMasFrecuente("Prueba3.txt")))