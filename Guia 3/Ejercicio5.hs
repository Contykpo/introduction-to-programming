todosMenores :: (Int, Int, Int) -> Bool
todosMenores (ax, ay, az) = f ax > g ax && f ay > g ay && f az > g az

f :: Int -> Int
f n | n <= 7 = n^2
    | n > 7 = 2*n - 1

g :: Int -> Int
g n = if even n then n `div` 2 else 3*n + 1 