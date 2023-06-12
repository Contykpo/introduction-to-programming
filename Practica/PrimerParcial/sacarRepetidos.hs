sacarRepetidos :: [Int] -> ([Int], [(Int, Int)])
sacarRepetidos [] = ([],[])
sacarRepetidos (x:xs) | elem x (fst sinRepeXS) = (fst sinRepeXS, agregar x (snd sinRepeXS))
                      | otherwise = (x:(fst sinRepeXS), snd sinRepeXS)
                      where sinRepeXS = sacarRepetidos xs

agregar :: Int -> [(Int, Int)] -> [(Int, Int)]
agregar x [] = [(x,1)]
agregar x ((e,cant):ys) | x == e = (x, cant+1):ys
                        | otherwise = (e,cant):(agregar x ys)