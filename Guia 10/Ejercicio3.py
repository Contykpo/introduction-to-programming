from typing import List

def invertirLineas(nombreArchivo: str):
    archivoOriginal = open(nombreArchivo + ".txt", "r")
    archivoReverso = open(nombreArchivo + "reverso.txt", "w")
    lineas: List[str] = []
    for linea in archivoOriginal:
        lineas.append(linea)
    lineasInvertidas: List[str] = lineas[::-1]
    lineasInvertidas[0] = lineasInvertidas[0]+"\n"
    for iterador in range(0,len(lineasInvertidas),1):
        archivoReverso.writelines(lineasInvertidas[iterador])


invertirLineas("Prueba1")