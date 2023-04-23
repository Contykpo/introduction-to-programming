-- A
f1 :: Int -> Int
f1 n    | n <= 0 = 1
        | otherwise = 2^n + f1 (n - 1)

-- B
f2 :: Int -> Float -> Float
f2 n q  | n <= 0 = 1
        | otherwise = q^n + f2 (n - 1)

-- C
f3 :: Int -> Float -> Float
f3 n q  | n <= 1 = q
        | otherwise = q^(2 * n) + q^((2 * n) -1) + f3 (n - 1) q

-- D
f4 :: Int -> Float -> Float
f4 n q  | n <= 1 = q
        | otherwise = q^n + f4 (n - 1)
 