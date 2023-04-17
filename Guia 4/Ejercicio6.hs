sumaDigitos :: Int -> Int
sumaDigitos n   | n <= 0 = 0
                | otherwise = (n `mod` 10) + sumaDigitos (n `div` 10)