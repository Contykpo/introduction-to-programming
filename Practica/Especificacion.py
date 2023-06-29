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
            listaDeFactores.append([numero])
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

# CM3 - Ejercicio 1 - Polaca inversa:

from queue import LifoQueue

def calcular_expresion(expr:str) -> float:
    expresion:List[str] = expr.split()
    pila: LifoQueue[int] = LifoQueue(maxsize=len(expresion))
    operadores: str = "/*+-"
    for elemeneto in expresion:
        if not elemeneto in operadores:
            pila.put(float(elemeneto))
        elif elemeneto != ' ':
            operadoresDerechos = pila.get()
            operadoresIzquierdos = pila.get()
            if elemeneto == '+':
                pila.put(operadoresIzquierdos + operadoresDerechos)
            elif elemeneto == '-':
                pila.put(operadoresIzquierdos - operadoresDerechos)
            elif elemeneto == '*':
                pila.put(operadoresIzquierdos * operadoresDerechos)
            elif elemeneto == '/':
                pila.put(int(operadoresIzquierdos / operadoresDerechos))
    return pila.get()

expresion1:str = "2 5 * 7 +"
expresion2:str = "2 3.5 -"
expresion3:str = "- 10"

print(f"Expresion en notacion pocala + {expresion1}: {calcular_expresion(expresion1)}")

# CM3 - Ejercicio 2 - Unir diccionarios:

from typing import Dict

def unir_diccionarios(a_unir: List[Dict[str,str]]) -> Dict[str,List[str]]:
    resultado: Dict[str,str] = {}
    for diccionario in a_unir:
        listaValores: List[str] = []
        for key in diccionario.keys():
            if key in resultado.keys():
                listaValores.append(diccionario.get(key))
                for elemento in resultado.get(key):
                    if elemento not in listaValores:
                        listaValores.append(elemento)
                resultado.update({key:listaValores[::-1]})
            else:
                resultado.update({key: diccionario.get(key)})
    return resultado

print(f"Unir diccionarios: {unir_diccionarios([{'a': '1', 'b': '2'}, {'b': '3', 'c': '4'}, {'a': '5'}])}")

# CM3 - Ejercicio 3 - Procesamiento de pedidos:

from typing import Union

from queue import Queue

def procesamiento_pedidos(pedidos: Queue[dict],
                          stock_productos: Dict[str, int],
                          precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
    resultado: List[dict] = []
    while not pedidos.empty():
        pedido = pedidos.get()
        pedidoId = pedido.get("id")
        pedidoCliente = pedido.get("cliente")
        pedidoProductos = pedido.get("productos")
        pedidoPrecioTotal: float = 0.0
        pedidoEstado: str = ""
        for keyProducto in pedidoProductos.keys():
            if keyProducto in stock_productos.keys() and keyProducto in precios_productos.keys():
                stockProducto:int = stock_productos.get(keyProducto)
                precioProducto:float = precios_productos.get(keyProducto)
                cantidadProductos:int = pedidoProductos.get(keyProducto)
                if pedidoProductos.get(keyProducto) <= stockProducto:
                    pedidoPrecioTotal += cantidadProductos * precioProducto
                    stockProducto -= pedidoProductos.get(keyProducto)
                    stock_productos.update({keyProducto:stockProducto})
                    pedidoEstado = "completo"
                else:
                    pedidoPrecioTotal += stockProducto * precioProducto
                    pedidoProductos.update({keyProducto: stockProducto})
                    stock_productos.update({keyProducto:0})
                    pedidoEstado = "incompleto"
        pedidoFinal = {"id": pedidoId, "cliente": pedidoCliente, "productos": pedidoProductos, "precio_total": pedidoPrecioTotal, "estado": pedidoEstado}
        resultado.append(pedidoFinal)
    return resultado

def procesar_pedidos(pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]],
                     stock_productos: Dict[str, int],
                     precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
    pedidos_procesados = []
    while not pedidos.empty():
        pedido = pedidos.get()
        pedido_procesado = {
            'id': pedido['id'],
            'cliente': pedido['cliente'],
            'productos': {},
            'precio_total': 0.0,
            'estado': 'completo'
        }
        for producto, cantidad in pedido['productos'].items():
            if producto not in stock_productos or stock_productos[producto] < cantidad:
                pedido_procesado['estado'] = 'incompleto'
                cantidad_disponible = stock_productos.get(producto, 0)
                pedido_procesado['productos'][producto] = min(cantidad_disponible, cantidad)
                pedido_procesado['precio_total'] += min(cantidad_disponible, cantidad) * precios_productos[producto]
            else:
                stock_productos[producto] -= cantidad
                pedido_procesado['productos'][producto] = cantidad
                pedido_procesado['precio_total'] += cantidad * precios_productos[producto]
        pedidos_procesados.append(pedido_procesado)
    return pedidos_procesados

pedidos: Queue = Queue(maxsize=2)
pedidos.put({"id":21,"cliente":"Gabriela", "productos":{"Manzana":2}})
pedidos.put({"id":1,"cliente":"Juan","productos":{"Manzana":2,"Pan":4,"Factura":6}})
stock_productos = {"Manzana":10, "Leche":5, "Pan":3, "Factura":0}
precios_productos = {"Manzana":3.5, "Leche":5.5, "Pan":3.5, "Factura":5}

print(str(procesamiento_pedidos(pedidos,stock_productos,precios_productos)))

# CM3 - Ejercicio 4 - Fila del banco:

def avanzarFila(fila: Queue, min: int):
  cronometro_caja_1: int = 0
  cronometro_caja_2: int = 0
  cronometro_caja_3: int = 0
  cronometro_atendido_3: int = 0
  atendido1: int = 0
  atendido2: int = 0
  atendido3: int = 0
  atendidos: [int] = []
  contadorMinutos: int = 0
  while contadorMinutos <= min:
    if contadorMinutos % 4 == 0:
      fila.put(nueva_persona_n(fila,atendidos))
    # Caja 1
    if contadorMinutos >= 1 and not fila.empty():
      if cronometro_caja_1 == 0:
        if atendido1 in atendidos:
          atendidos.remove(atendido1)
        atendido1 = fila.get()
        atendidos.append(atendido1)
        cronometro_caja_1 = 10
      else:
        cronometro_caja_1 -= 1
    # Caja 2
    if contadorMinutos >= 3 and not fila.empty():
      if cronometro_caja_2 == 0:
        if atendido2 in atendidos:
          atendidos.remove(atendido2)
        atendido2 = fila.get()
        atendidos.append(atendido2)
        cronometro_caja_2 = 4
      else:
        cronometro_caja_2 -= 1
    # Caja 3
    if contadorMinutos >= 2 and not fila.empty():
      if cronometro_caja_3 == 0:
        atendido3 = fila.get()
        atendidos.append(atendido3)
        cronometro_caja_3 = 4
        cronometro_atendido_3 = 3
      else:
        cronometro_caja_3 -= 1
        cronometro_atendido_3 -= 1
    if contadorMinutos >= 2 and cronometro_atendido_3 == 0 and atendido3 in atendidos:
      fila.put(atendido3)
      atendidos.remove(atendido3)
      atendido3 = 0
    contadorMinutos += 1


# Funcion auxiliar para determinar el entero que debe representar la nueva persona que se suma a la fila del banco cada 4 minutos.
def nueva_persona_n(fila: Queue, atendidos: [int]) -> int:
  if fila.qsize() > 0:
    personas: [int] = []
    for iterador in range(0, fila.qsize(), 1):
      personas.append(fila.get())
    maximoPersona: int = personas[0]
    for persona in personas:
      fila.put(persona)
      if persona > maximoPersona:
        maximoPersona = persona
    return maximoPersona + 1
  elif len(atendidos) > 0:
    maximoAtendido: int = atendidos[0]
    for atendido in atendidos:
      if atendido > maximoAtendido:
        maximoAtendido = atendido
    return maximoAtendido + 1
  else:
    return 1


personas: Queue = Queue(maxsize=1000)
personas.put(1)
personas.put(2)
personas.put(3)

avanzarFila(personas,5)

for iterado in range(0,personas.qsize(),1):
    print(f"Persona: {personas.get()}")

# Caja1: Empieza a atender 10:01, y atiende a una persona cada 10 minutos
# Caja2: Empieza a atender 10:03, atiende a una persona cada 4 minutos
# Caja3: Empieza a atender 10:02, y atiende una persona cada 4 minutos, pero no le resuelve el problema y la persona debe volver a la fila (se va al final y tarda 3 min en llegar. Es decir, la persona que fue atendida 10:02 vuelve a entrar a la fila a las 10:05)
# La fila empieza con las n personas que llegaron antes de que abra el banco. Cuando abre (a las 10), cada 4 minutos llega una nueva persona a la fila (la primera entra a las 10:00)


# Parcial 2023 - Ejercicio 2 - Decodificar.

def decodificar(reglas_codificado: List[Tuple[str,str]], mensaje_codificado: str) -> str:
    mensaje_decodificado: str = ""
    codigos_y_reglas: Tuple[List[str],List[str]] = ([],[])
    for codigo, significado in reglas_codificado:
        codigos_y_reglas[0].append(codigo)
        codigos_y_reglas[1].append(significado)
    for simbolo in mensaje_codificado:
        for codiguito in codigos_y_reglas[0]:
            if codiguito == simbolo:
                mensaje_decodificado += codigos_y_reglas[1][codigos_y_reglas[0].index(codiguito)]
                pass
    return mensaje_decodificado


print(decodificar([("a", "h"),("b", "o"),("x", "y"),("c","l"),("d","a")], "abcd"))





