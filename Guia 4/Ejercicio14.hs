sumaPotencias :: Int -> Int -> Int -> Int
sumaPotencias q n m = (sumaPotenciasN q n) * (sumaPotenciasM q m)

sumaPotenciasN :: Int -> Int -> Int
sumaPotenciasN q n  | n <= 0 = 1
                    | otherwise = q^n + q^(n - 1)

sumaPotenciasM :: Int -> Int -> Int
sumaPotenciasM q m  | m <= 0 = 1
                    | otherwise = q^m + q^(m - 1)