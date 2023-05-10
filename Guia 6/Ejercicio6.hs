module Ejercicio6 where

multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs)   | n==0 && x==0  = x:multiplosDeN n xs
                        | n==0          = multiplosDeN n xs
                        | mod x n==0    = x:multiplosDeN n xs 
                        | otherwise     = multiplosDeN n xs