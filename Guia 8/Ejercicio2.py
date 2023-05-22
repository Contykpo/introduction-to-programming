# 1

def borrar_numeros_en_posiciones_pares(lista: list) -> list:
    for i in range(0,len(lista),2):
        lista[i] = 0
    return lista

# 2

def borrar_numeros_en_posiciones_pares_copia(lista: list) -> list:
    for i in range(0,len(lista),2):
        lista[i] = 0
    listaCopia = lista.copy()
    return listaCopia

# 3

def borrar_vocales_en_palabra(palabra: str) -> str:
    listaDeVocales = ["a","A","e","E","i","I","o","O","u","U"]
    for caracter in palabra:
        if caracter in listaDeVocales:
            palabra = palabra.replace(caracter, "")
    return palabra

# 4

def reemplazar_vocales_en_palabra(palabra: str) -> str:
    listaDeVocales = ["a","A","e","E","i","I","o","O","u","U"]
    for caracter in palabra:
        if caracter in listaDeVocales:
            palabra = palabra.replace(caracter, "-")
    return palabra

# 5

def dar_vuelta_str(string: str) -> str:
    return string[::-1]