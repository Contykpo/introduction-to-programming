-- No editar esta parte
main :: IO()
main = do {
  x <- readLn ;
  print(prod(x ::(Integer)))
  }

prod :: Integer -> Integer
-- Completar la definición de la función
prod n = prod' (2*n) 
-- Pueden agregan las funciones que consideren necesarias
prod' :: Integer -> Integer
prod' n | n <= 1 = 3
        | otherwise = (n^2 + 2*n) * prod' (n-1)