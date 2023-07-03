-- Problema reemplazar vocales

reemplazarVocales :: [Char] -> [Char]
reemplazarVocales [] = []
reemplazarVocales (caracter : caracteres)   | pertenece caracter vocales = reemplazarVocales caracteres
                                            | otherwise = caracter : reemplazarVocales caracteres

vocales :: [Char]
vocales = "aeiou"

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece elem (elemento : elementos)   | elemento == elem = True
                                        | otherwise = pertenece elem elementos

-- Problema dar vuelta arreglo de caracteres

darVueltaString0 :: [Char] -> [Char]
darVueltaString0 [] = []
darVueltaString0 (caracter : caracteres) = darVueltaString caracteres ++ [caracter]


darVueltaString :: [Char] -> [Char]
darVueltaString string = invertir string []

invertir :: [Char] -> [Char] -> [Char]
invertir [] cadena = cadena 
invertir (caracter : caracteres) inversa = invertir caracteres (caracter : inversa)

-- Guia 5 - Ejercicio 6.2 - Partes del conjunto {1,2, ..., n}

type Set = [Integer]

partes :: Integer -> [Set]
partes 0 = [[],[1]]
partes n = agregarTodos (partes (n-1)) n ++ partes (n-1)

agregarTodos :: [[Integer]] -> Integer -> [[Integer]]
agregarTodos [] _ = []
agregarTodos (conjunto : conjuntos) elemento = (elemento : conjunto) : agregarTodos conjuntos elemento

-- Guia 5 - Ejercicio 6.3 - Producto cartesiano entre un conjunto A y otro conjunto B

type SetX = [(Integer, Integer)]

productoCartesiano :: Set -> Set -> SetX
productoCartesiano [] conjuntoB = []
productoCartesiano (elementoA : elementosA) conjuntoB = (productoCartesianoAux elementoA conjuntoB) ++ (productoCartesiano elementosA conjuntoB)

productoCartesianoAux :: Integer -> Set -> SetX
productoCartesianoAux x [] = []
productoCartesianoAux elementoA (elementoB : elementosB) = (elementoA, elementoB) : (productoCartesianoAux elementoA elementosB)

-- Guia 5 - Ejercicio 4 - Palabra mas larga.

palabraMasLarga :: [Char] -> [Char]
palabraMasLarga [] = []
palabraMasLarga texto = maxima (generarPalabras texto [])

generarPalabras :: [Char] -> [Char] -> [[Char]]
generarPalabras [] _ = []
generarPalabras (caracter : caracteres) palabra | not (caracter == ' ') = generarPalabras caracteres (palabra ++ [caracter])
                                                | otherwise = palabra : generarPalabras caracteres []

maxima :: [[Char]] -> [Char]
maxima [] = []
maxima [palabra] = palabra
maxima (palabra1 : palabra2 : palabras) | length palabra1 > length palabra2 = maxima (palabra1 : palabras)

-- Guia 5 - Ejercicio 3.8 - Multiplos de un numero entero dentro de una una lista de enteros

multiplosN :: Integer -> [Integer] -> [Integer]
multiplosN numero (elemento : elementos)    | null elementos = if mod elemento numero == 0 then [elemento] else []
                                            | mod elemento numero == 0 = elemento : multiplosN numero elementos
                                            | otherwise = multiplosN numero elementos

-- Guia 5 - Ejercicio 4.7 - Aplanar lista de lista de caracteres con una n cantidad de espacios blancos.

aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] _ = []
aplanarConNBlancos (palabra : palabras) cantidad = palabra ++ generarNBlancos cantidad [] ++ aplanarConNBlancos palabras cantidad

generarNBlancos :: Integer -> [Char] -> [Char]
generarNBlancos 0 _ = []
generarNBlancos cantidad blancos    | cantidad == 1 = ' ' : blancos
                                    | otherwise = (' ' : blancos) ++ generarNBlancos (cantidad -1) blancos

-- Guia 4 - Ejercicio 7 - Chquear si todos los digitos de un numero son iguales.

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales numero = if numero == sumaDigitos numero (cantidadDigitos numero) then True else False

sumaDigitos :: Integer -> Integer -> Integer
sumaDigitos numero 0 = 0
sumaDigitos numero  n = (mod numero 10) * (10^(n-1)) + sumaDigitos numero (n-1)

cantidadDigitos :: Integer -> Integer
cantidadDigitos 0 = 0
cantidadDigitos numero = 1 + cantidadDigitos (div numero 10)

-- Guia 4 - Ejercicio 21 - Funcion pitagoras que cuenta la cantidad de pares (p,q) con 0<=p<=m y 0<=q<=n que satisfacen  m^2 + n^2 <= r^2.

pitagoras :: Int -> Int -> Int -> Int
pitagoras m n r | m <= 0 || n <= 0 = 0
                | otherwise = sumatoriaExterna m n r

sumatoriaExterna :: Int -> Int -> Int -> Int
sumatoriaExterna m n r  | m == 0 = sumatoriaInterna m n r
                        | otherwise = sumatoriaInterna m n r + sumatoriaExterna (m-1) n r

sumatoriaInterna :: Int -> Int -> Int -> Int
sumatoriaInterna m n r  | n == 0 = if m^2 <= r^2 then 1 else 0
                        | m^2 + n^2 <= r^2 = 1 + sumatoriaInterna m (n-1) r
                        | otherwise = sumatoriaInterna m (n-1) r

-- Guia 5 - Ejercicio 5.6 - Descomponer elementos de una una lista de enteros en sus factores primos.

descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (numero : numeros)  | numero == 1 = [numero] : descomponerEnPrimos numeros
                                        | numero == 0 = [numero] : descomponerEnPrimos numeros
                                        | esPrimo numero = [numero] : descomponerEnPrimos numeros
                                        | otherwise = factoresPrimos numero 2 : descomponerEnPrimos numeros

factoresPrimos :: Integer -> Integer -> [Integer]
factoresPrimos numero factor    | factor < numero = if esPrimo factor && (mod numero factor == 0) then factor : factoresPrimos numero (factor + 1) else factoresPrimos numero (factor + 1)
                                | otherwise = []

esPrimo :: Integer -> Bool
esPrimo entero  | entero <= 1 = False
                | entero == 2 = True
                | otherwise = esPrimoAuxiliar entero 2

esPrimoAuxiliar :: Integer -> Integer -> Bool
esPrimoAuxiliar entero divisor  | divisor > (div entero 2) = True
                                | mod entero divisor == 0 = False
                                | otherwise = esPrimoAuxiliar entero (divisor + 1)


-- Guia 6 - Ejercicio 4 - Dado un valor y una lista del mismo tipo, devuelve la misma lista, pero sin los elementos del valor dado.

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos posibleElemento (elemento : elementos)  | elemento == posibleElemento = quitarTodos posibleElemento elementos
                                                    | otherwise = elemento : quitarTodos posibleElemento elementos

-- Ejercicio Parcial - Dada una lista de enteros, retornar una tupla con una lista de aquellos elementos que no esten repetidos en la lista origina, y en el segun elemento,
-- Una lista de tupas de enteros, donde el primer elmento es el entero repetido, y el segundo es la cantidad de apariciones en toda la lista.

eliminarYContarRepetidos :: [Integer] -> ([Integer], [(Integer, Integer)])
eliminarYContarRepetidos [] = ([],[])
eliminarYContarRepetidos lista = (eliminarRepetidos lista, contarRepetidos lista)

eliminarRepetidos :: [Integer] -> [Integer]
eliminarRepetidos [] = []
eliminarRepetidos (elemento : elementos)    | elemento `elem` elementos = eliminarRepetidos elementos
                                            | otherwise = elemento : eliminarRepetidos elementos

contarRepetidos :: [Integer] -> [(Integer, Integer)]
contarRepetidos [] = []
contarRepetidos (elemento : elementos)  | elemento `elem` elementos = (elemento, cantidadApariciones elemento elementos) : contarRepetidos (quitarTodos elemento elementos)
                                        | otherwise = contarRepetidos elementos

cantidadApariciones :: Integer -> [Integer] -> Integer
cantidadApariciones _ [] = 0
cantidadApariciones posibleElemen (elemento : elementos)    | elemento == posibleElemen = 1 + cantidadApariciones posibleElemen elementos
                                                            | otherwise = cantidadApariciones posibleElemen elementos

-- Otra implementacion de lo anterior:

eliminarYContarRepetidos2 :: [Integer] -> ([Integer], [(Integer, Integer)])
eliminarYContarRepetidos2 [elemento] = ([elemento], [])
eliminarYContarRepetidos2 (elemento : elementos)      | elemento `elem` listaSinRepetidos = (listaSinRepetidos, contarRepetidos2 elemento repeticiones)
                                                      | otherwise = (elemento : listaSinRepetidos, repeticiones)
                                                      where (listaSinRepetidos, repeticiones) = eliminarYContarRepetidos2 elementos

contarRepetidos2 :: Integer -> [(Integer, Integer)] -> [(Integer, Integer)]
contarRepetidos2 elemento [] = [(elemento, 1)]
contarRepetidos2 elemento ((elementoActual, repeticiones) : elementos)  | elementoActual == elemento = (elementoActual, repeticiones + 1) : elementos
                                                                        | otherwise = (elementoActual, repeticiones) : contarRepetidos2 elemento elementos

-- CMS1 - Ejercicio 5 - Combinaciones menores o iguales.

combinacionesMenoresOIguales :: Integer -> Integer
combinacionesMenoresOIguales numero = sumatoriaExterna2 numero numero numero

sumatoriaExterna2 :: Integer -> Integer -> Integer -> Integer
sumatoriaExterna2 indiceE indiceI numero | indiceE == 1 = if indiceE * indiceI <= numero then 1 else 0
                                        | otherwise = sumatoriaInterna2 indiceE indiceI numero + sumatoriaExterna2 (indiceE - 1) indiceI numero

sumatoriaInterna2 :: Integer -> Integer -> Integer -> Integer
sumatoriaInterna2 indiceE indiceI numero | indiceI == 1 = if indiceE * indiceI <= numero then 1 else 0
                                        | indiceE * indiceI <= numero = 1 + sumatoriaInterna2 indiceE (indiceI - 1) numero
                                        | otherwise = sumatoriaInterna2 indiceE (indiceI - 1) numero

-- Armar Triplas Pitagoricas

armarTriplasPitagoricas :: [Integer] -> [(Integer,Integer,Integer)]
armarTriplasPitagoricas lista = pitagoricas (componerTuplas lista)

pitagoricas :: [(Integer,Integer,Integer)] -> [(Integer,Integer,Integer)]
pitagoricas [] = []
pitagoricas ((t0,t1,t2):elementos)  | t0 <= t1 && t1 <= t2 = if t0^2 + t1^2 == t2^2 then (t0,t1,t2) : pitagoricas elementos else pitagoricas elementos
                                    | otherwise = pitagoricas elementos

componerTuplas :: [Integer] -> [(Integer,Integer,Integer)]
componerTuplas [] = []
componerTuplas [e1] = []
componerTuplas [e1,e2] = []
componerTuplas (e0:e1:e2:e3:elementos)  | null elementos = componerElementosTupla (e0,e1,e2)
                                        | otherwise = componerElementosTupla (e0,e1,e2) ++ componerTuplas lista
                                        where lista = e1:e2:e3:elementos

componerElementosTupla :: (Integer,Integer,Integer) -> [(Integer,Integer,Integer)]
componerElementosTupla (e0,e1,e2) = [(e0,e1,e2)] ++ [(e0,e2,e1)] ++ [(e1,e0,e2)] ++ [(e1,e2,e0)] ++ [(e2,e0,e1)] ++ [(e2,e1,e0)]

-- Calcular ganancia

calcularGanancia :: [(Integer,Integer)] -> Integer -> Integer
calcularGanancia [] _ = 0
calcularGanancia ((compra,venta):precios) presupuesto   | null precios = if compra <= presupuesto then venta - compra else 0
                                                        | otherwise = maximo (sumaGananciasPosibles listaPrecios presupuesto)
                                                        where listaPrecios = (compra,venta): precios

sumaGananciasPosibles :: [(Integer,Integer)] -> Integer -> [Integer]
sumaGananciasPosibles ((compra,venta):precios) presupuesto  | null precios = if compra <= presupuesto then [venta - compra] else [0]
                                                            | compra <= presupuesto = sumarGananciasDeComprasPosibles (sumaGananciasPosibles precios (presupuesto - compra)) (venta - compra) ++ sumaGananciasPosibles precios presupuesto
                                                            | otherwise = sumaGananciasPosibles precios presupuesto

sumarGananciasDeComprasPosibles :: [Integer] -> Integer -> [Integer]
sumarGananciasDeComprasPosibles [] _ = []
sumarGananciasDeComprasPosibles (gananciaActual : ganancias) ganancia = (ganancia + gananciaActual) : sumarGananciasDeComprasPosibles ganancias ganancia 

maximo :: [Integer] -> Integer
maximo [elemento] = elemento
maximo (elemento1:elemento2:elementos)  | elemento1 > elemento2 = maximo (elemento1 : elementos)
                                        | otherwise = maximo (elemento2 : elementos) 


-- Orden Lexografico

modificar :: [Integer] -> [Integer] -> Integer
modificar _ [] = 0
modificar lista1 lista2 | length lista2 > length lista1 = 0
                        | otherwise = distanciaManhattan lista1 (modificarLista lista1 lista2)

distanciaManhattan :: [Integer] -> [Integer] -> Integer
distanciaManhattan [elemento1] [elemento2] = abs(elemento1 - elemento2)
distanciaManhattan (elemento1:elementos1) (elemento2:elementos2) = abs(elemento1 - elemento2) + distanciaManhattan elementos1 elementos2

modificarLista :: [Integer] -> [Integer] -> [Integer]
modificarLista lista1 lista2    | menorLex lista1 lista2 = lista1
                                | otherwise = modificarListaAuxiliar lista1 lista2 []

modificarListaAuxiliar :: [Integer] -> [Integer] -> [Integer] -> [Integer]
modificarListaAuxiliar [] _  _ = []
modificarListaAuxiliar _ []  _ = []
modificarListaAuxiliar (elemento1Actual:elemento1Siguiente:elementos1) (elemento2Actual:elemento2Siguiente:elementos2) cabezal1 | elemento1Actual == elemento2Actual = if elemento1Siguiente < elemento2Siguiente then cabezal1 ++ (elemento1Actual:elemento1Siguiente:elementos1) else cabezal1 ++ (elemento1Actual:(elemento1Siguiente - (elemento1Siguiente-elemento2Siguiente-1)):elementos1)
                                                                                                                                | otherwise = modificarListaAuxiliar (elemento1Siguiente:elementos1) (elemento2Siguiente:elementos2) (elemento1Actual : cabezal1)

menorLex :: [Integer] -> [Integer] -> Bool
menorLex (elemento1:elemento1Siguiente:elementos1) (elemento2:elemento2Siguiente:elementos2)    | elemento1 == elemento2 && ((length lista1 < length lista2) || (elemento1Siguiente < elemento2Siguiente)) = True
                                                                                                | otherwise = menorLex (elemento1Siguiente:elementos1) (elemento2Siguiente:elementos2)
                                                                                                where lista1 = elemento1:elemento1Siguiente:elementos1
                                                                                                      lista2 = elemento2:elemento2Siguiente:elementos2

-- Parcial 2023 - Ejercicio 2 - Decodificar.

decodificar :: [(Char, Char)] -> [Char] -> [Char]
decodificar [] mensaje = mensaje
decodificar _ [] = []
decodificar ((codigo, significado) : reglas) (simbolo : simbolos) | simbolo == codigo = significado : decodificar reglasCodificado simbolos
                                                                  | otherwise = (obtenerSignificado reglas simbolo) : decodificar reglasCodificado simbolos
                                                                  where reglasCodificado = (codigo, significado) : reglas

obtenerSignificado :: [(Char,Char)] -> Char -> Char
obtenerSignificado [] simbolo = simbolo
obtenerSignificado ((codigo, significado) : reglas) simbolo | simbolo == codigo = significado
                                                            | otherwise = obtenerSignificado reglas simbolo

pruebaDecodificar = decodificar [('a', 'h'),('b', 'o'),('x', 'y'),('c','l'),('d','a')] ['a','b','c','d']


-- Parcial 2023 Simulacro - Ejercicio 2 - Elimniar y contar repetidos.

eliminarYContarRepetidos3 :: [Integer] -> ([Integer],[(Integer,Integer)])
eliminarYContarRepetidos3 [] = ([],[])
eliminarYContarRepetidos3 [elemento] = ([elemento],[])
eliminarYContarRepetidos3 (elemento : elementos)      | elemento `elem` listaSinRepetidos = (listaSinRepetidos, contarRepeticiones elemento repeticiones)
                                                      | otherwise = (elemento : listaSinRepetidos, repeticiones)
                                                      where (listaSinRepetidos, repeticiones) = eliminarYContarRepetidos3 elementos

contarRepeticiones :: Integer -> [(Integer,Integer)] -> [(Integer,Integer)]
contarRepeticiones elemento [] = [(elemento,1)]
contarRepeticiones elemento ((elementoRepetido, repeticiones) : otrasRepeticiones)  | elementoRepetido == elemento = (elementoRepetido, repeticiones + 1) : otrasRepeticiones
                                                                                    | otherwise = (elementoRepetido, repeticiones) : contarRepeticiones elemento otrasRepeticiones

pruebaEliminarRepeticiones = eliminarYContarRepetidos3 [1,2,3,4,5,1,2,4,5,6,7,8,9,10]


-- Ejercicio de parcial - Maxima ganancia entre compras posibles.

calcularMaximaGanancia :: [(Integer, Integer)] -> Integer -> Integer
calcularMaximaGanancia [] _ = 0
calcularMaximaGanancia ((compra,venta): precios) presupuesto      | null precios = if compra <= presupuesto then venta - compra else 0
                                                                  | otherwise = maximo (sumaGananciasPosibles2 listadoPrecios presupuesto ++ sumaGananciasCompraRepetida listadoPrecios presupuesto)
                                                                  where listadoPrecios = (compra,venta) : precios

sumaGananciasPosibles2 :: [(Integer,Integer)] -> Integer -> [Integer]
sumaGananciasPosibles2 ((compra,venta): precios) presupuesto      | null precios = if compra <= presupuesto then [venta - compra] else [0]
                                                                  | compra <= presupuesto = sumaGananciasPorCompraPosibles (sumaGananciasPosibles2 precios (presupuesto - compra)) (venta-compra) ++ sumaGananciasPosibles2 precios presupuesto
                                                                  | otherwise = sumaGananciasPosibles precios presupuesto

sumaGananciasPorCompraPosibles :: [Integer] -> Integer -> [Integer]
sumaGananciasPorCompraPosibles [] _ = []
sumaGananciasPorCompraPosibles (gananciaActual : ganancias) nuevaGanancia = (gananciaActual + nuevaGanancia) : sumaGananciasPorCompraPosibles ganancias nuevaGanancia

sumaGananciasCompraRepetida :: [(Integer,Integer)] -> Integer -> [Integer]
sumaGananciasCompraRepetida ((compra, venta):precios) presupuesto | null precios = if compra <= presupuesto then [(venta-compra)* div presupuesto compra] else [0]
                                                                  | compra <= presupuesto = ((venta-compra) * div presupuesto compra) : sumaGananciasCompraRepetida precios presupuesto
                                                                  | otherwise = sumaGananciasCompraRepetida precios presupuesto

maximo2 :: [Integer] -> Integer
maximo2 [elemento] = elemento
maximo2 (elemento:segundoElemento:elementos)    | elemento > segundoElemento = maximo2 (elemento : elementos)
                                                | otherwise = maximo2 (segundoElemento : elementos)

pruebaCalcularMaximaGanancia = calcularMaximaGanancia [(10,11),(10,11),(9,13)] 33


-- Ejercicio crear una funcion que invierte el orden de los elementos de una lista

invertirListado :: [a] -> [a] 
invertirListado [] = [] 
invertirListado (elemento:elementos) = invertirListado elementos ++ [elemento]

-- Guia 5 - Ejercicio 5.6 - Descomponer en primos:

descomponerEnFactoresPrimos :: [Integer] -> [[Integer]]
descomponerEnFactoresPrimos [] = []
descomponerEnFactoresPrimos (numero : numeros)  | numero == 1 || numero == 0 = [numero] : descomponerEnFactoresPrimos numeros
                                                | esPrimo2 numero = [numero] : descomponerEnFactoresPrimos numeros
                                                | otherwise = obtenerFactoresPrimos numero 2 : descomponerEnFactoresPrimos numeros

obtenerFactoresPrimos :: Integer -> Integer -> [Integer]
obtenerFactoresPrimos numero factor | factor > numero = []
                                    | esPrimo2 factor  && (mod numero factor == 0) && mod (div numero factor) factor == 0 = obtenerFactoresMultiples numero factor ++ obtenerFactoresPrimos numero (factor+1)
                                    | esPrimo2 factor && (mod numero factor == 0) = factor : obtenerFactoresPrimos numero (factor+1)
                                    | otherwise = obtenerFactoresPrimos numero (factor+1)

obtenerFactoresMultiples :: Integer -> Integer -> [Integer]
obtenerFactoresMultiples numero factor    | mod numero factor == 0 = factor : obtenerFactoresMultiples (div numero factor) factor
                                          | otherwise = []

esPrimo2 :: Integer -> Bool
esPrimo2 numero   | numero == 1 = False
                  | numero == 2 = True
                  | otherwise = esPrimoAuxiliar numero 2

esPrimo2Auxiliar :: Integer -> Integer -> Bool
esPrimo2Auxiliar numero divisor     | divisor > div numero 2 = True
                                    | mod numero divisor == 0 = False
                                    | otherwise = esPrimo2Auxiliar numero (divisor+1)

pruebaDescomponerEnFactoresPrimos = descomponerEnFactoresPrimos [4,3,5,6,7,1,0,10,13,81]