-- No editar esta parte
main :: IO()
main = do {
  x <- readLn ;
  print(sumaPrimerosNImpares(x ::(Integer)))
  }

sumaPrimerosNImpares :: Integer -> Integer
-- Completar la definición de la función
sumaPrimerosNImpares n = productoImpares ((2*n) - 1) 
-- Pueden agregan las funciones que consideren necesarias
productoImpares :: Integer -> Integer
productoImpares n | n == 1 = 4
                  | n == 0 = 0
                  | otherwise = if even n then 0 + productoImpares (n-1) else ((2*n) + 2) + productoImpares (n-1)