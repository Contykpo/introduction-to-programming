-- A
type Set = [Integer]

agregarATodos :: Integer -> [Set] -> [Set]
agregarATodos _ [] = []
agregarATodos n (x:xs) = if pertenece n x then agregarATodos n xs else (n : x) : agregarATodos n xs

-- B
partes :: [Integer] -> [Set]
partes []  = [[]]
partes (x:xs) = partes xs ++ map (x:) (partes xs)

-- C
productoCartesiano :: Set -> Set -> [(Integer, Integer)]
productoCartesiano xs ys = [(x,y) | x <- xs, y <- ys]

-- Helper Functions --

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece x lista   | lista == [] = False
                    | head lista == x = True
                    | otherwise = pertenece x (tail lista) 