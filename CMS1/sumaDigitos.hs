-- No editar esta parte
main :: IO()
main = do {
  x <- readLn ;
  print(sumaDigitos(x ::(Int)))
  }

sumaDigitos :: Int -> Int
-- Completar la definición de la función
sumaDigitos n   | n == 0 = 0
                | n < 0 = sumaDigitos (abs n)
                | otherwise = (n `mod` 10) + sumaDigitos (n `div` 10)
-- Pueden agregan las funciones que consideren necesarias