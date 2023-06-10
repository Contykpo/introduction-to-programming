pitagoras :: Int -> Int -> Int -> Int
pitagoras m n r | m <= 0 || n <= 0 = 0
                | otherwise = sumatoriaExterna m r r

sumatoriaExterna :: Int -> Int -> Int -> Int
sumatoriaExterna m n r  | m == 0 = sumatoriaInterna m n r
                        | otherwise = sumatoriaInterna m n r + sumatoriaExterna (m-1) n r

sumatoriaInterna :: Int -> Int -> Int -> Int
sumatoriaInterna m n r  | n == 0 = if m^2 <= r^2 then 1 else 0
                        | m^2 + n^2 <= r^2 = 1 + sumatoriaInterna m (n-1) r
                        | otherwise = sumatoriaInterna m (n-1) r