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