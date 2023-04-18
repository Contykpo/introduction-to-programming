sumaPotencias :: Int -> Int -> Int -> Int
sumaPotencias q n m | n == 0 && m == 0 = q
                    | n /= 0 && n /= 0 = q^(n+m) + q^(n+m-1) + sumaPotencias q (n-1) (m-1)
                    | n == 0 = q^m + q^(m-1) + sumaPotencias q 0 (m-1)
                    | m == 0 = q^n + q^(n-1) + sumaPotencias q 0 (n-1)