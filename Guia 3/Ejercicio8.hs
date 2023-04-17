import Data.Fixed (mod')
comparar :: Int -> Int -> Int
comparar x y    | sumaUltimosDosDigitos x < sumaUltimosDosDigitos y = 1
                | sumaUltimosDosDigitos x > sumaUltimosDosDigitos y = -1
                | sumaUltimosDosDigitos x == sumaUltimosDosDigitos y = 0

sumaUltimosDosDigitos :: Int -> Int
sumaUltimosDosDigitos x | x <= (-10) || x >= 10 = (x - (x `div` 10) * 10) + (x - (x `div` 100) * 100) `div` 10
                        | otherwise = x