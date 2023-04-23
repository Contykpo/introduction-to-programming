-- No editar esta parte
main :: IO ()
main = do
  x <- readLn
  print (sumaMenosQueMax (x :: (Int, Int, Int)))

sumaMenosQueMax :: (Int, Int, Int) -> Bool
-- Completar acá la definición de la función
sumaMenosQueMax (a, b, c) = maximo a b c > ((minimo a b c) + (medio a b c))
                            where
                              maximo x y z = max x (max y z)
                              minimo x y z = min a (min b c)

-- Pueden agregan las funciones que consideren necesarias

medio :: Int -> Int -> Int -> Int
medio a b c | (a > b && a < c) || (a > c && a < b) = a
            | (b > a && b < c) || (b > c && b < a) = b
            | (c > a && c < b) || (c > b && c < a) = c
            | otherwise = if a == b then a else c