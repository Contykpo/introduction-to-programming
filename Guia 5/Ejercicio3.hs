-- A
sumatoria :: [Integer] -> Integer
sumatoria lista | lista == [] = 0
                | longitud lista <= 1 = head lista
                | otherwise = (head lista) + sumatoria (tail lista)

-- B
productoria :: [Integer] -> Integer
productoria lista | lista == [] = 0
                | longitud lista <= 1 = head lista
                | otherwise = (head lista) * productoria (tail lista)

-- C
--maximo :: [Integer] -> Integer
--maximo lista    | longitud lista <= 1 = if longitud lista == 1 then head lista else 0
--                | otherwise = max (head lista) (maximo (tail lista))

maximo :: [Int] -> Int
maximo (x:xs)   | cantidadElementos (x:xs) == 1 = x
                | cantidadElementos (x:xs) == 0 = 0
                | otherwise = max x (maximo xs)

-- D
sumarN :: Integer -> [Integer] -> [Integer]
sumarN n lista  | lista == [] = [n]
                | otherwise = revertir (sumarN' n lista) 

sumarN' :: Integer -> [Integer] -> [Integer] 
sumarN' n lista = sumarN' n ((tail lista) ++ [((head lista) + n)])
{-
-- E
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero  | lista == [] = []
                | otherwise = revertir (sumarElPrimero' (head lista) lista) 

sumarElPrimero' :: Integer -> [Integer] -> [Integer] 
sumarElPrimero' n lista = sumarElPrimero' n ((tail lista) ++ [((head lista) + n)])

-- F
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo  | lista == [] = []
                | otherwise = revertir (sumarElUltimo' (last lista) lista) 

sumarElUltimo' :: Integer -> [Integer] -> [Integer] 
sumarElUltimo' n lista = sumarElUltimo' n ((tail lista) ++ [((head lista) + n)])
-}
-- G
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs)    | even x = x : pares xs
                | otherwise = pares xs

-- H
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n lista    | lista == [] = []
                        | mod (head lista) n == 0 = (head lista) : (multiplosDeN n (tail lista))
                        | otherwise = multiplosDeN n (tail lista)

-- I
ordenar :: [Integer] -> [Integer]
{-
ordenar lista   | lista == [] = []
                | otherwise = (ordenar (quitar (minimo lista) lista)) ++ [(minimo lista)] 
-}
ordenar lista   | lista == [] = []
                | otherwise = ordenar [a | a <- (tail lista), a < (head lista)] ++ [(head lista)] ++ ordenar [b | b <- (tail lista), b >= (head lista)]

-- Helper functions --

longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

revertir :: [a] -> [a] 
revertir []  = [] 
revertir lista = revertir (tail lista) ++ [head lista]

minimo :: [Integer] -> Integer
minimo lista    | longitud lista <= 1 = if longitud lista == 1 then head lista else 0
                | otherwise = min (head lista) (minimo (tail lista))

quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar x (y:ys) | x == y = (tail ys)
                | otherwise = y : quitar x ys