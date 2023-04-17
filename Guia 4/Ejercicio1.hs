fibonacci :: Int -> Int
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | otherwise = if n > 1 then fibonacci (n - 1) + fibonacci (n - 2) else undefined