pitagoras :: Int -> Int -> Int -> Int
pitagoras n m r | m <= 0 || n <= 0 = 0
                | otherwise = sumatoriaDoble n m r

sumatoriaDoble :: Int -> Int -> Int -> Int
sumatoriaDoble n m r    | n == 0 = sumatoriaInterna n m r
                        | otherwise = sumatoriaInterna n m r + sumatoriaDoble (n-1) m r

sumatoriaInterna :: Int -> Int -> Int -> Int
sumatoriaInterna n m r  | m == 0 = if n^2 <= r^2 then 1 else 0
                        | n^2 + m^2 <= r^2 = 1 + sumatoriaInterna n (m-1) r
                        | otherwise = sumatoriaInterna n (m-1) r