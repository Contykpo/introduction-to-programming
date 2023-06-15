from typing import List
from typing import Tuple

# Guia 7 - Ejercicio 6.5 - Monitorear tiempo:

def monitoreo_temporal(anoPartida: int, anoLlegada) -> List[int]:
    anosRetrocedidos: List[int] = []
    for iterador in range(0,(anoPartida-anoLlegada),1):
        anosRetrocedidos.append(anoLlegada+iterador)
    return anosRetrocedidos[::-1]

print(str(monitoreo_temporal(2023, 2012)))

# Guia 8 - Ejercicio 2 - Reemplazar vocales - Dar vuelta string:

def reemplazar_vocales(texto: str) -> str:
    vocales:str = "aeiou"
    textoSinVocales:str = ""
    for caracter in texto:
        if not caracter in vocales:
            textoSinVocales += caracter
    return textoSinVocales

def dar_vuelta_string(texto: str) -> str:
    return texto[::-1]


def dar_vuelta_string_alternativo(texto: str) -> str:
    textoInvertido:str = ""
    for caracter in texto:
        textoInvertido = caracter + textoInvertido
    return textoInvertido


print(reemplazar_vocales("Hola que tal?, buen dia"))
print(dar_vuelta_string("abc"))
print(dar_vuelta_string_alternativo("redrum"))

# Guia 9 - Ejercicio 16 - Es subsecuencia:

def es_subsecuencia(secuencia: List[int], subsecuencia: List[int]) -> bool:
    resultado: bool = False
    ultimoIndice:int = len(secuencia) - len(subsecuencia)
    for iterador in range(0, ultimoIndice + 1, 1):
        subsecuencita: List[int] = generar_subsecuencia(secuencia, iterador, len(subsecuencia))
        if son_iguales(subsecuencita, subsecuencia):
            resultado = True
            break
    return resultado


def generar_subsecuencia(secuencia: List[int], desde:int, longitud: int) -> List[int]:
    nuevaSubsecuencia: List[int] = []
    hasta: int = desde + longitud
    for iterador in range(desde,hasta,1):
        elemento: int = secuencia[iterador]
        nuevaSubsecuencia.append(elemento)
    return nuevaSubsecuencia


def son_iguales(subsecuenciaA: List[int], subsecuenciaB: List[int]) -> bool:
    resultado: bool = True
    if len(subsecuenciaA) == len(subsecuenciaB):
        for iterador in range(0, len(subsecuenciaA),1):
            if subsecuenciaA[iterador] != subsecuenciaB[iterador]:
                resultado = False
                break
    else:
        resultado = False
    return resultado


print(str(es_subsecuencia([1,2,3,4,5,6], [4,5,6])))

# Guia 9 - Ejercicio 17 - Calcular fragemnto mas largo:

def calcular_fragmento_mas_largo(texto:str) -> int:
    fragmentos: List[str] = texto.split(";")
    maximoFragmento: int = 0
    for fragmento in fragmentos:
        if len(fragmento) > maximoFragmento:
            maximoFragmento = len(fragmento)
    return maximoFragmento


print(str(calcular_fragmento_mas_largo("Mercurio;Venus;Tierra;Marten;Saturno;Jupiter")))

# Guia 8 - Ejercicio 1.7 - Analizar contrañas:

def analizar_contrasena(contrasena: str) -> str:
    if len(contrasena) > 8:
        tieneMayus: bool = False
        tieneMinus: bool = False
        tieneNumeros: bool = False
        for caracter in contrasena:
            if "A" <= caracter <= "Z":
                tieneMayus = True
            if "a" <= caracter <= "z":
                tieneMinus = True
            if "0" <= caracter <= "9":
                tieneNumeros = True
        if tieneMayus and tieneMinus and tieneNumeros:
            return "VERDE"
    elif len(contrasena) < 5:
        return "ROJO"
    return "AMARILLO"


print(analizar_contrasena("CacaDeVaca123"))

# Guia 9 - Ejercicio 15 - Cantidad de primos y determinar si un numero es primo.

def cantidad_de_primos(numero: int) -> int:
    resultado: int = 0
    for entero in range(2,numero+1,1):
        if es_primo(entero):
            resultado += 1
    return resultado


def es_primo(numero: int) -> bool:
    if numero >= 2:
        for entero in range(2, numero, 1):
            if numero % entero == 0:
                return False
        return True
    return False


print("Es primo: "+str(es_primo(10)))
print("Cantidad de primos hasta: "+str(cantidad_de_primos(10)))

# Guia 5 - Ejercicio 5.6 - Descomponer elementos de una una lista de enteros en sus factores primos.

def descomponer_en_primos(numeros: List[int]) -> List[List[int]]:
    listaDeFactores: List[List[int]] = []
    for numero in numeros:
        if es_primo(numero) or (numero >= -1 and numero <= 1):
            listaDeFactores.append(numero)
        else:
            listaDeFactores.append(obtener_factores(numero))
    return listaDeFactores


def obtener_factores(numero:int) -> List[int]:
    factores: List[int] = []
    posibleFactor: int = 2
    while posibleFactor < numero:
        if es_primo(posibleFactor) and (numero % posibleFactor == 0):
            factores.append(posibleFactor)
        posibleFactor += 1
    return factores

print(str(descomponer_en_primos([1,2,4,15,21,17])))

# Guia 9 - Ejercicio 10 - Devolver maximo comun divisior entre dos enteros.

def maximo_comun_divisior(entero1:int, entero2:int) -> int:
    assert(entero1 >= 0 and entero2 >= 0)
    temporary: int = 0
    while entero2 != 0:
        temporary = entero1 % entero2
        entero1 = entero2
        entero2 = temporary
    return entero1

print(str(maximo_comun_divisior(15,27)))

# Ejercicio Parcial - Dada una lista de enteros, retornar una tupla con una lista de aquellos elementos que no esten repetidos en la lista origina, y en el segun elemento,
# una lista de tupas de enteros, donde el primer elmento es el entero repetido, y el segundo es la cantidad de apariciones en toda la lista.

def eliminar_y_contar_repetidos(lista: List[int]) -> Tuple[List[int],List[Tuple[int,int]]]:
    listaSinRepetidos: List[int] = []
    listaDeRepetidos: List[Tuple[int,int]] = []
    for elemento in lista:
        if not elemento in listaSinRepetidos:
            cantidadDeRepetidos: int = lista.count(elemento)
            if cantidadDeRepetidos > 1:
                listaDeRepetidos.append((elemento, cantidadDeRepetidos - 1))
            listaSinRepetidos.append(elemento)
    return (listaSinRepetidos, listaDeRepetidos)


print(str(eliminar_y_contar_repetidos([1,2,3,2,3,4,5,6,3])))

# CM2 - Dada una matriz, retornar verdadero si sus filas mantienen un diferencia identica en cada columna.

def filas_parecidas(matriz: List[List[int]]) -> bool:
    if len(matriz) == 1:
        return True
    diferencia: int = matriz[1][0] - matriz[0][0]
    for iteradorFila in range(1, len(matriz),1):
        for iteradorColumna in range(0, len(matriz[iteradorFila]), 1):
            if matriz[iteradorFila][iteradorColumna] != (matriz[iteradorFila - 1][iteradorColumna] + diferencia):
                return False
    return True

print("Tiene filas parecidas: "+str(filas_parecidas([[1,2,3],[4,5,6]])))

# CM2 - Ejercicio 5 - Se puede llegar.

def se_puede_llegar(origen:str, destino:str, vuelos: List[Tuple[str,str]]) -> int:
    vuelosValidos: List[Tuple[str,str]] = vuelos
    ciudadActual: str = origen
    vuelosTomados: int = 0
    while ciudadActual != destino and len(vuelosValidos) > 0:
        for vuelo in vuelosValidos:
            if ciudadActual == vuelo[0]:
                ciudadActual = vuelo[1]
                vuelosTomados += 1
                vuelosValidos.remove(vuelo)
                break
            if vuelosValidos.index(vuelo) == (len(vuelosValidos) - 1):
                return -1
    if ciudadActual != destino:
        return -1
    return vuelosTomados

print("La ruta es: " + str(se_puede_llegar("BuenosAires","Toronto",[("BuenosAires","Utah"),("Utah","Toronto")])))

# Armar triplas pitagoricas

def armar_triplas_pitagoricas(lista: List[int]) -> List[Tuple[int,int,int]]:
    lista.sort()
    resultado: List[Tuple[int,int,int]] = []
    for iterador in range(0,len(lista) - 2,1):
        izquierda = iterador + 1
        derecha = len(lista) - 1
        while izquierda < derecha:
            resultado.append((lista[iterador], lista[izquierda], lista[derecha]))
            izquierda += 1
            derecha -= 1
    for tripla in resultado:
        if tripla[0]**2 + tripla[1]**2 > tripla[2]**2:
            resultado.remove(tripla)
    return resultado

def encontrar_mayor_igual(elemento: int, lista: List[int]) -> int:
    for posibleMaximo in lista:
        if posibleMaximo >= elemento:
            return posibleMaximo
    return elemento

print(str(armar_triplas_pitagoricas([4,4,5,3,1])))

# Calcular ganancia

from copy import copy

def calcular_ganancia(precios: List[Tuple[int,int]], presupuesto: int) -> int:
    gananciaPosible: List[int] = []
    for precio in precios:
        gananciaInicial: int = 0
        presupuestoTemporal: int = copy(presupuesto)
        if precio[0] <= presupuestoTemporal:
            presupuestoTemporal = presupuestoTemporal - precio[0]
            gananciaInicial = precio[1] - precio[0]
            ganaciasPosibles: List[int] = calcular_posibles_ganancias(precios,precio,gananciaInicial,presupuestoTemporal)
            for ganancia in ganaciasPosibles:
                gananciaPosible.append(ganancia)
    print(str(gananciaPosible))
    return maximo(gananciaPosible)

def calcular_posibles_ganancias(precios: List[Tuple[int,int]], precio: Tuple[int,int],ganancia:int,presupuesto:int) -> List[int]:
    resultado: List[int] = []
    iterador:int = 0
    while iterador < len(precios):
        presupuestoTemporal:int = presupuesto
        gananciasTotales:int = ganancia
        for precioI in precios:
            if precioI[0] <= presupuestoTemporal:
                presupuestoTemporal -= precioI[0]
                gananciasTotales += (precioI[1] - precioI[0])
        resultado.append(gananciasTotales)
        iterador += 1
    return resultado
def maximo(lista: List[int]) -> int:
    maximoActual: int = 0
    for elemento in lista:
        if elemento > maximoActual:
            maximoActual = elemento
    return maximoActual


print("La mayor ganancia es: "+str(calcular_ganancia([(10,11),(10,12),(17,19)],32)))