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

