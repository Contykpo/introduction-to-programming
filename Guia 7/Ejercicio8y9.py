def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g

print(str(rt(1,2)))

g: int = 0

print(str(g))

def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g

print(str(ro(1)))
print(str(g))

