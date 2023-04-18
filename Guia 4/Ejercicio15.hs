sumaRacionales :: Int -> Int -> Float
sumaRacionales x y  | x <= 0 || y <= 0 = 0
                    | otherwise = sumatoriaDoble (fromIntegral x) (fromIntegral y)

sumatoriaDoble :: Float -> Float -> Float
sumatoriaDoble x y  | x <= 0 || y <= 0 = 0
                    | otherwise = sumatoriaDoble (x-1) y + sumatoriaInterna x y                 

sumatoriaInterna :: Float -> Float -> Float
sumatoriaInterna n j| n <= 0 || j <= 0 = 0
                    | otherwise = n/j + sumatoriaInterna n (j-1)