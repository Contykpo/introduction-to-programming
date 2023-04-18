tomaValorMax :: Int ->Int -> Int
tomaValorMax x y    | x < 1 || y < x = 0
                    | otherwise = sumaDivisores x y

sumaDivisores :: Int -> Int -> Int
sumaDivisores n m   | n <= 1 || n >= m = 0
                    | (m-n) `mod` m == 0 = n + sumaDivisores (n+1) m
                    | otherwise = m

