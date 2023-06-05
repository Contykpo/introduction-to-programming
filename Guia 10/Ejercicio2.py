def clonarSinComentarios(nombreArchivo: str):
    archivoOriginal = open(nombreArchivo + ".txt", "r")
    archivoClon = open(nombreArchivo+"-clon.txt", "w")
    for linea in archivoOriginal:
        hayOtroCaracter: bool = False
        noEsComentario: bool = False
        for iterador in range(0,len(linea),1):
            if linea[iterador] != " ":
                hayOtroCaracter = True
            if linea[iterador] == "#":
                if hayOtroCaracter:
                    noEsComentario = True
                    print("No es comentario")
                break
        if not noEsComentario:
            archivoClon.writelines(linea)
    archivoOriginal.close()
    archivoClon.close()

clonarSinComentarios("Prueba2")



