import Data.Char (intToDigit)

-- A
nat2bin :: Integer -> [Integer]
nat2bin n   | n <= 0 = []
            | n == 1 = [1]
            | otherwise = nat2bin (div n 2) ++ [mod n 2]

-- B
bin2nat :: [Integer] -> Integer
bin2nat [] = 0
bin2nat lista = bin2nat' (revertir lista)

bin2nat' :: [Integer] -> Integer
bin2nat' (x:xs) = (2 * (bin2nat' xs)) + x

-- C
nat2hex :: Int -> [Char]
nat2hex x = reverse (nat2hex' x)
   where
      nat2hex' 0 = "0"
      nat2hex' n = let (q, r) = n `divMod` 16
         in if q == 0
            then [intToDigit r]
            else intToDigit r : nat2hex' q

-- D
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada (x:xs) = (x : [sumatoria xs]) ++ sumaAcumulada xs 


sumatoria :: (Num a) => [a] -> a
sumatoria (x:xs)| longitud xs == 0 = x
                | otherwise = x + sumatoria xs

-- E
descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = factoresPrimos x : descomponerEnPrimos (tail xs)

factoresPrimos :: Integer -> [Integer]
factoresPrimos 1 = []
factoresPrimos n =
  case factors of
    [] -> [n]
    _  -> factors ++ factoresPrimos (n `div` head factors)
  where factors = take 1 $ filter (\x -> (n `mod` x) == 0) [2 .. n-1]

-- Helper Functions --

longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

revertir :: [a] -> [a] 
revertir []  = [] 
revertir (x:xs) = revertir xs ++ [x]

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece x lista   | lista == [] = False
                    | head lista == x = True
                    | otherwise = pertenece x (tail lista) 

todosIguales :: (Eq t) => [t] -> Bool
todosIguales lista  | lista == [] = False
                    | head lista == head (tail lista) = True
                    | otherwise = todosIguales (tail lista)