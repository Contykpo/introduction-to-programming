from typing import List

def palabrasEnArchivoBinario(nombreArchivo: str) -> List[str]:
    archivo = open(nombreArchivo, "r")
    numbers: List[str] = ["1","2","3","4","5","6","7","8","9","0"]
    palabras: List[str] = []
    for linea in archivo:
        caracteresValidosConsecutivos: str = ""
        for caracter in linea:
            if caracter.isalpha() or (caracter in numbers) or caracter == " " or caracter == "-":
                caracteresValidosConsecutivos += caracter
            else:
                caracteresValidosConsecutivos = ""
        if len(caracteresValidosConsecutivos) >= 5:
            palabras.append(caracteresValidosConsecutivos)
    archivo.close()
    return palabras

