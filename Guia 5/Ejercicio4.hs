import Data.ByteString (elemIndex)
import Text.Read (Lexeme(Char))

-- A
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos (x:xs)| xs == [] = []      
                            | x == ' ' = if head (xs) == ' ' then sacarBlancosRepetidos xs else [x] ++ sacarBlancosRepetidos xs
                            | otherwise =  [x] ++ sacarBlancosRepetidos xs

-- B
contarPalabras :: [Char] -> Integer
contarPalabras lista    | lista == [] = 0
                        | otherwise = 1 + contarCaracteres ' ' lista

contarCaracteres :: Eq a => a -> [a] -> Integer
contarCaracteres x [] = 0
contarCaracteres x (y:ys)   | x==y = 1 + contarCaracteres x ys
                            | otherwise = contarCaracteres x ys

-- C
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga lista   | lista == [] = []
                        | otherwise = masLarga (split [' '] lista)

masLarga :: [[Char]] -> [Char]
masLarga xss = snd $ maximum $ [(length xs, xs) | xs <- xss]

split :: (Eq a) => [a] -> [a] -> [[a]]
split _ [] = [[]]
split sep (list_head:list_tail) =
    if list_head `elem` sep
        then []:splited_tail
        else (list_head:(head splited_tail)):(tail splited_tail)
    where splited_tail = split sep list_tail

-- D
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos (x:xs) = x ++ [' '] ++  aplanarConBlancos xs 

-- E
aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] _ = []
aplanarConNBlancos (x:xs) n = x ++ concatenarBlancos n [] ++  aplanarConBlancos xs 

concatenarBlancos :: Integer -> [Char] -> [Char]
concatenarBlancos n lista   | n == 1 = ' ' : lista 
                            | n <= 0 = [] 
                            | otherwise = ' ' : lista ++ concatenarBlancos (n-1) lista

-- Helper Functions --

longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos x (y:ys)    | x == y = quitarTodos x ys
                        | otherwise = y : quitarTodos x ys

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece x lista   | lista == [] = False
                    | head lista == x = True
                    | otherwise = pertenece x (tail lista)

