def agregarFrase(frase: str, nombreArchivo:str):
    archivo = open(nombreArchivo + ".txt", "a")
    archivo.write("\n"+frase)
    archivo.close()

agregarFrase("We won't stop fighting", "Prueba1")