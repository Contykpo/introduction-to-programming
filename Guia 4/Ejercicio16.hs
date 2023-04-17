-- A
menorDivisor :: Int -> Int
menorDivisor n  | n <= 0 = 1
                | otherwise = esDivisor n 2

-- B
esPrimo :: Int -> Bool
esPrimo n   | n == 1 = False
            | n == 2 = True
            | (length [x | x <- [2 .. n-1], mod n x == 0]) > 0 = False
		    | otherwise = True

-- C
sonCoprimos :: Int -> Int -> Bool
sonCoprimos x y | x <= 0 || y <= 0 = False
                | otherwise = if (esDivisor x 1) == (esDivisor y 1) then True else False

-- FUNCIONES AUXILIARES
esDivisor :: Int -> Int -> Int
esDivisor x y   | y <= 0 = 1
                | otherwise = if x `mod` y == 0 then y else (esDivisor x (y+1)) 