-- No editar esta parte
main :: IO()
main = do {
  x <- readLn ;
  print(combinacionesMenoresOiguales(x ::(Integer)))
  }

combinacionesMenoresOiguales :: Integer -> Integer
-- Completar la definición de la función
combinacionesMenoresOiguales n = sumatoriaExterna n n n
-- Pueden agregan las funciones que consideren necesarias
sumatoriaExterna :: Integer -> Integer -> Integer -> Integer
sumatoriaExterna n1 n2 n0 | n1 == 1 = sumatoriaInterna n1 n2 n0
                          | otherwise = sumatoriaInterna n1 n2 n0 + sumatoriaExterna (n1-1) n2 n0

sumatoriaInterna :: Integer -> Integer -> Integer -> Integer
sumatoriaInterna n1 n2 n0 | n2 == 1 = if n1*n2 <= n0 then 1 else 0
                          | n1 * n2 <= n0 = 1 + sumatoriaInterna n1 (n2-1) n0
                          | otherwise = sumatoriaInterna n1 (n2-1) n0

