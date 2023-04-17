distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (ax, ay, az) (bx, by, bz) = sqrt((bx - ax)^2 + (by - ay)^2 + (bz - az)^2)