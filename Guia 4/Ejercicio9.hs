esCapicua :: Int -> Bool
esCapicua x = (darVuelta x) == x

darVuelta :: Int -> Int
darVuelta = go 0
    where   go a 0 = a
            go a b = let (q,r) = b `quotRem` 10 in go (a*10 + r) q