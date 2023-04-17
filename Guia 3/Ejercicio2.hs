-- A
{--}
absoluto :: Integer -> Integer
absoluto = abs

-- B
{--}
maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto n m = max (abs n) (abs m)

-- C
{--}
maximo3 ::Integer -> Integer -> Integer  -> Integer
maximo3 x y z = max (max (abs x) (abs y)) (abs z)

-- D
{--}
algunoes0 :: (Floating f, Eq f) => f -> f -> Bool
algunoes0 x y | (x * y) == 0 = True

algunoes01 :: (Floating f, Eq f) => f -> f -> Bool
algunoes01 0 x = True

algunoes02 :: (Floating f, Eq f) => f -> f -> Bool
algunoes02 0 y = True

-- E
{--}
ambosSon0 :: (Floating f, Eq f) => f -> f -> Bool
ambosSon0 x y | x == 0 && y == 0 = True

ambosSon01 :: (Floating f, Eq f) => f -> f -> Bool
ambosSon01 0 0 = True

-- F
{--}
estanRelacionados :: (Num a, Ord a) => a -> a -> Bool
estanRelacionados x y | x <= 3 && y <= 3 = True
                        | (x > 3 && x <= 7) && (y > 3 && y <= 7) = True
                        | x > 7 && y > 7 = True

-- G
{--}
sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z = if x /= y && x /= z && y /= z then x + z + y else undefined

-- H
{--}
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y| y `mod` x == 0 = True 
                | otherwise = False

-- I
{--}
digitoUnidades :: Int -> Int
digitoUnidades x| x >= 10 = x - (x `div` 10) * 10
                | x > 0 && x <= 10 = x
                | x <= 0 = undefined

-- J
{--}
digitoDecenas :: Int -> Int
digitoDecenas x | x >= 100 = (x - (x `div` 100) * 100) `div` 10
                | x >= 10 && x < 100 = x `div` 10
                | x < 10 = undefined