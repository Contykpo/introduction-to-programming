{-
mayorDigitoPar :: Int -> Int
mayorDigitoPar n    | n <= 0 = 0
                    | (iesimoDigito n (cantidadDigitos n)) `mod` 8 == 0 = (iesimoDigito n (cantidadDigitos n))
                    | (iesimoDigito n (cantidadDigitos n)) `mod` 6 == 0 = (iesimoDigito n (cantidadDigitos n))
                    | (iesimoDigito n (cantidadDigitos n)) `mod` 4 == 0 = (iesimoDigito n (cantidadDigitos n))
                    | (iesimoDigito n (cantidadDigitos n)) `mod` 2 == 0 = (iesimoDigito n (cantidadDigitos n))
                    | otherwise = mayorDigitoPar (n-1)

iesimoDigito :: Int -> Int -> Int
iesimoDigito n i | n >= 0 && i >= 1 && i <= cantidadDigitos n = n `div` 10^(cantidadDigitos n - i) `mod` 10

cantidadDigitos :: Int -> Int
cantidadDigitos n = if n > 0 then 1 + cantidadDigitos (div n 10) else 0 
-}

mayorDigitoPar :: Int -> Int
mayorDigitoPar n    | n < 10 && even n = n
                    | n < 10 = - 1
                    | even (n `mod` 10) = max (n `mod` 10) (mayorDigitoPar (n `div` 10))
                    | otherwise = mayorDigitoPar (n `div` 10)
{-}                where 
                    ultimoDigito = 
                    par = even
                    recurrenciaSiguiente a = 
-}