-- A
prodInt :: (Float, Float) -> (Float, Float) -> Float
prodInt (ax, ay) (bx, by) = bx * ax + ay * by

-- B 
todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor (ax, ay) (bx, by) | ax < bx && ay < by = True
                            | otherwise = False

-- C
distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos (ax, ay) (bx, by) = sqrt(ax**2 + ay**2) - sqrt(bx**2 + by**2)

-- D
sumaTerna :: (Int, Int, Int) -> Int
sumaTerna (ax, ay, az) = ax + ay + az

-- E
sumarSoloMultiplos :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos (ax, ay, az) n = divisible ax n + divisible ay n + divisible az n

divisible :: Int -> Int -> Int
divisible x n   | x `mod` n == 0 = x
                | otherwise = 0

-- F
posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (ax, ay, az)   | even ax = 0
                            | even ay = 1
                            | even az = 2
                            | otherwise = - 1

-- G
crearPar :: t -> t' -> (t, t')
crearPar a b = (a, b)

-- F
invertir :: (t, t') -> (t', t)
invertir (a, b) = (b, a)