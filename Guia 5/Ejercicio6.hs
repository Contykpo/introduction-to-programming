-- A
type Set = [Integer]

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
agregarTodos (xs:xss) y = (y : xs) : agregarTodos xss y

-- C
--productoCartesiano :: Set -> Set -> [(Integer, Integer)]
--productoCartesiano xs ys = [(x,y) | x <- xs, y <- ys]

productoCartesiano :: Set -> Set -> [(Integer,Integer)]
productoCartesiano [] ys = []
productoCartesiano (a:b) ys = (productoCartesiano' a ys) ++ (productoCartesiano b ys)

productoCartesiano' :: Integer -> Set -> [(Integer,Integer)]
productoCartesiano' x [] = []
productoCartesiano' x (a:b) = (x, a) : (productoCartesiano' x b)

-- Helper Functions --

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece x lista   | lista == [] = False
                    | head lista == x = True
                    | otherwise = pertenece x (tail lista) 