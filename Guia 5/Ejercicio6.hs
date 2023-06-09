-- A
type Set = [Integer]
type SetX = [(Integer,Integer)]

agregarATodos :: Integer -> [Set] -> [Set]
agregarATodos _ [] = []
agregarATodos n (x:xs) = if pertenece n x then agregarATodos n xs else (n : x) : agregarATodos n xs

-- B
{-
partes :: [Integer] -> [Set]
partes []  = [[]]
partes (x:xs) = partes xs ++ map (x:) (partes xs)
-}

partes :: Integer -> [Set]
partes 0 = [[],[1]]
partes n = agregarTodos (partes (n-1)) n ++ partes (n-1)

agregarTodos :: [[Integer]] -> Integer -> [[Integer]]
agregarTodos [] _ = []
agregarTodos (conjunto : conjuntos) elemento = (elemento : conjunto) : agregarTodos conjuntos elemento

-- C
--productoCartesiano :: Set -> Set -> [(Integer, Integer)]
--productoCartesiano xs ys = [(x,y) | x <- xs, y <- ys]

productoCartesiano :: Set -> Set -> SetX
productoCartesiano [] conjuntoB = []
productoCartesiano (elementoA : elementosA) conjuntoB = (productoCartesianoAux elementoA conjuntoB) ++ (productoCartesiano elementosA conjuntoB)

productoCartesianoAux :: Integer -> Set -> SetX
productoCartesianoAux x [] = []
productoCartesianoAux elementoA (elementoB : elementosB) = (elementoA, elementoB) : (productoCartesianoAux elementoA elementosB)

-- Helper Functions --

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece x lista   | lista == [] = False
                    | head lista == x = True
                    | otherwise = pertenece x (tail lista) 