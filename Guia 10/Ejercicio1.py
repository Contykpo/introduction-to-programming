# 1

def contarLineas(nombreArchivo: str) -> int:
    archivoReporte = open(nombreArchivo+".txt", "r")
    cantidadLineas: int = archivoReporte.readlines()
    archivoReporte.close()
    return  cantidadLineas

def existePalabra(palabra: str, nombreArchivo: str) -> bool:
    nombreArchivo = open(nombreArchivo+".txt", "r")
    contenido: str = nombreArchivo.read()
    nombreArchivo.close()
    if palabra in contenido:
        return True
    else:
        return False

def cantidadDeApariciones(palabra: str, nombreArchivo: str) -> int:
    nombreArchivo = open(nombreArchivo + ".txt", "r")
    cantidadApariciones: int = 0
    for linea in nombreArchivo:
        cantidadApariciones += linea.count(palabra)
    nombreArchivo.close()
    return cantidadApariciones

def cantidadDeApariciones1(palabra: str, nombreArchivo: str) -> int:
    nombreArchivo = open(nombreArchivo + ".txt", "r")
    cantidadApariciones: int = 0
    cantidadApariciones += nombreArchivo.read().count(palabra)
    nombreArchivo.close()
    return cantidadApariciones

print(str(cantidadDeApariciones1("tal","Prueba1")))
