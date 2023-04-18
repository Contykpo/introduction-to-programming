import GHC.Float (sqrtFloat, int2Double)
esFibonacci :: Int -> Bool
esFibonacci n   | n <= 0 = False
                | otherwise = esRectanguloPerfecto ((5*(int2Double n ^2)) + 4) || esRectanguloPerfecto ((5*(int2Double n ^ 2)) - 4)

esRectanguloPerfecto :: Double -> Bool
esRectanguloPerfecto n = (sqrt n * sqrt n) == n