medioFactorial :: Int -> Int
medioFactorial n    | n <= 0 = 1
                    | otherwise = n * medioFactorial (n - 2)