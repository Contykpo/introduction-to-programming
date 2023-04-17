estanRelacionados :: Integer ->Integer ->Bool
estanRelacionados x y | x /= 0 && y /= 0 = (x * x) `mod` (x * y) == 0 