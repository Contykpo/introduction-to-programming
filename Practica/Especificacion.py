from typing import List

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
