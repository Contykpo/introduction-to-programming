sumatoriaDoble :: Int -> Int -> Int
sumatoriaDoble x y  | x <= 0 || y <= 0 = 0
                    | otherwise = (sumatoriaDoble (x-1) y) + sumatoriaInterna x y

sumatoriaInterna :: Int -> Int -> Int
sumatoriaInterna n j| n <= 0 || j <= 0 = 0
                    | otherwise = n^j + (sumatoriaInterna n (j-1))