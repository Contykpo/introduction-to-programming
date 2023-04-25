-- A
longitud :: [Integer] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

-- B
ultimo :: [t] -> t
ultimo a    | longitud a < 1 = 0
            | longitud a == 1 = a[0]
            | otherwise = ultimo (tail a)

-- C
principio :: [T] -> [T]
principio [] = []
principio (cabezal : cola) = cabezal : revertir cola

-- D
revertir :: [a] -> [a] 
revertir []  = [] 
revertir (x:xs) = revertir xs ++ [x]