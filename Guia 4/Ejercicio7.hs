todoosDigitosIguales :: Integer -> Bool
todoosDigitosIguales numero | numero <= 0 = False
                            | (mod numero 10) + sumaDigitos (div numero 10) == 2 * numero = True

sumaDigitos :: Integer -> Integer
sumaDigitos numero  | numero <= 0 = 0
                    | otherwise = (mod numero 10) + sumaDigitos (div numero 10)
