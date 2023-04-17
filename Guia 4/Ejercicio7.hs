todosDigitosIguales :: Int ->Bool
todosDigitosIguales n   | n <= 0 = False
                        | (n `mod` 10) + sumaDigitos (n `div` 10) == 2 * n = True

sumaDigitos :: Int -> Int
sumaDigitos n   | n <= 0 = 0
                | otherwise = (n `mod` 10) + sumaDigitos (n `div` 10)