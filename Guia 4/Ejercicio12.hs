raizDe2Aproximada :: Int -> Float
raizDe2Aproximada n  | n <= 1 = 1
                | otherwise = 2 + (1 / raizDe2Aproximada (n-1))