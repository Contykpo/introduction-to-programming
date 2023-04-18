iesimoDigito :: Int -> Int -> Int
iesimoDigito n i | n >= 0 && i >= 1 && i <= cantidadDigitos n = n `div` 10^(cantidadDigitos n - i) `mod` 10

cantidadDigitos :: Int -> Int
cantidadDigitos n = if n > 0 then 1 + cantidadDigitos (div n 10) else 0