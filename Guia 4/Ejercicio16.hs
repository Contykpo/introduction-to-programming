-- A
menorDivisor :: Int -> Int
menorDivisor n  | n <= 0 = 1
                | otherwise = esDivisor n 2

-- FUNCIONES AUXILIARES
esDivisor :: Int -> Int -> Int
esDivisor x y   | y <= 0 = 1
                | otherwise = if x `mod` y == 0 then y else esDivisor x (y+1)

-- B
esPrimo :: Int -> Bool
esPrimo n   | n <= 1 = False
            | n == 2 = True
            | otherwise = esPrimo' n 2

esPrimo' :: Int -> Int -> Bool
esPrimo' n d    | d > (n `div` 2) = True
                | n `mod` d == 0  = False
                | otherwise = esPrimo' n (d + 1)

-- C
sonCoprimos :: Int -> Int -> Bool
sonCoprimos x y = sonCoprimos' x y y

sonCoprimos' :: Int -> Int -> Int -> Bool
sonCoprimos' a b c  | c <= 0 = False
                    | a `mod` c == 0 && b `mod` c == 0 = True
                    | otherwise = sonCoprimos' a b (c - 1)

-- C
nEsimoPrimo :: Int -> Int
nEsimoPrimo n   | n <= 1 = 2
                | otherwise = nEsimoPrimo' n 1

nEsimoPrimo' :: Int -> Int -> Int
nEsimoPrimo' n m| n <= 1 = 2
                | otherwise = if esPrimo m && n == m then m else nEsimoPrimo' n (m+1)

