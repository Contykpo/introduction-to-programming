-- A
eAprox -> Int -> Float
eAprox n    | n <= 0 = undefined
            | otherwise = 1 / (factorial (n)) + 1 / (factorial (n -1))

factorial :: Int -> Int
factorial n | n == 0 = 1
            | otherwise = n * factorial (n - 1)

-- B
e :: Float
e = eAprox 10