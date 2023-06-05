from typing import List

def agregarFraseAlInicio(frase: str, nombreArchivo: str):
    archivo = open(nombreArchivo + ".txt", "r")
    lineas: List[str] = []
    for linea in archivo:
        lineas.append(linea)
    archivo.close()
    archivo = open(nombreArchivo + ".txt", "w")
    archivo.writelines(frase+"\n")
    for linea in lineas:
        archivo.writelines(linea)
    archivo.close()

agregarFraseAlInicio("Hello Hello", "Prueba1")