-- A
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece x lista   | lista == [] = False
                    | head lista == x = True
                    | otherwise = pertenece x (tail lista) 

-- B
todosIguales :: (Eq t) => [t] -> Bool
todosIguales lista  | lista == [] = False
                    | head lista == head (tail lista) = True
                    | otherwise = todosIguales (tail lista)

-- C
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (elemento : elementos)   | elemento `elem` elementos = False
                                        | otherwise = todosDistintos elementos

-- D
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos lista  | longitud lista <= 1 = False
                    | otherwise = if elem (head lista) lista then True else hayRepetidos (tail lista)

-- E
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar x (y:ys) | x == y = (tail ys)
                | otherwise = y : quitar x ys

-- F
quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos x (y:ys)    | x == y = quitarTodos x ys
                        | otherwise = y : quitarTodos x ys

-- G
{-eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos lista | head lista == head (tail lista) = eliminarRepetidos tail (tail (tail lista))
                        | not (head lista == head (tail lista)) = eliminarRepetidos (tail lista)
                        | otherwise = lista
-}
-- H
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos lista1 lista2   | lista1 == [] || lista2 == [] = True
                                | pertenece (head lista1) lista2 = mismosElementos' (tail lista1) lista2 1
                                | otherwise = mismosElementos' (tail lista1) lista2 0

mismosElementos' :: (Eq t) => [t] -> [t] -> Integer -> Bool
mismosElementos' lista1 lista2 n    | lista1 == [] = False
                                    | n == longitud lista1 = True 
                                    | pertenece (head lista1) lista2 = mismosElementos' (tail lista1) lista2 (n+1)
                                    | otherwise = mismosElementos' (tail lista1) lista2 n

-- I
capicua :: (Eq t) => [t] -> Bool
capicua lista   | longitud lista <= 1 = True
                | otherwise = capicua' lista lista

capicua' :: (Eq t) => [t] -> [t] -> Bool
capicua' lista1 lista2  | lista1 == revertir lista2 = True
                        | otherwise = False

-- Helper functions --

longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

revertir :: [a] -> [a] 
revertir []  = [] 
revertir lista = revertir (tail lista) ++ [head lista]