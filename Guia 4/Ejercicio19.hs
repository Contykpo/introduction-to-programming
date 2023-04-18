esSumaInicialDePrimos :: Int -> Bool
esSumaInicialDePrimos n | n <= 1 = False
                        | otherwise = esSumaInicialDePrimos' n 1

esSumaInicialDePrimos' :: Int -> Int -> Bool
esSumaInicialDePrimos' n m  | n <= 1 || m >= n = False
                            | otherwise = if (sumarPrimosHasta m) == n then True else esSumaInicialDePrimos' n (m + 1) 

-- Funciones Auxiliares

sumarPrimosHasta :: Int->Int
sumarPrimosHasta n  | n <= 0 = 0
                    | otherwise = if esPrimo n then n + sumarPrimosHasta (n-1) else sumarPrimosHasta (n-1)

esPrimo :: Int -> Bool
esPrimo n   | n <= 1 = False
            | n == 2 = True
            | otherwise = esPrimo' n 2

esPrimo' :: Int -> Int -> Bool
esPrimo' n d    | d > (n `div` 2) = True
                | n `mod` d == 0  = False
                | otherwise = esPrimo' n (d + 1)