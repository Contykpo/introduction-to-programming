from typing import Dict
from typing import List

def agruparPorLongitud(nombreArchivo:str) -> Dict[int,int]:
    archivo = open(nombreArchivo, "r")
    palabras: List[str] = []
    for linea in archivo:
        for palabrita in linea.split():
            palabras.append(palabrita)
    print(palabras)
    longitudesPalabras: List[int] = []
    agrupacion: Dict[int, int] = {}
    for palabra in palabras:
        longitudesPalabras.append(len(palabra))
    for longitud in longitudesPalabras:
        agrupacion.update({longitud : longitudesPalabras.count(longitud) })
    archivo.close()
    return agrupacion


print(str(agruparPorLongitud("Prueba3.txt")))