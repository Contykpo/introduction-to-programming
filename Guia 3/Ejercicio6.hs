bisiesto :: Int -> Bool
bisiesto año
    | (año `mod` 100 == 0) && (año `mod` 400 == 0) = True
    | año `mod` 4 == 0 = True
    | otherwise = False