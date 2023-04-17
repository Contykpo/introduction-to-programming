esDivisible :: Int -> Int -> Bool
esDivisible x y | restarHasta0 x y < 0 || restarHasta0 x y < 0 = False
                | restarHasta0 x y == 0 = True

restarHasta0 :: Int -> Int -> Int
restarHasta0 x y    | x <= 0 = x
                    | otherwise = restarHasta0 (x - y) y