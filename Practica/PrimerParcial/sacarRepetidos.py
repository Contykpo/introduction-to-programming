def sacarRepetidos(l:list) -> list:
    res: list = []
    for i in range(0, len(l)):
        if not pertenece(res, l[i]):
            res.append(l[i])
    return res

def pertenece(l:list, e: int) -> bool:
    for i in range(0, len(l)):
        if l[i] == e:
            return True
        
    return False

if __name__ == '__main__':
  x = [1,1,1,2,3,5,1,2,4]
  print(sacarRepetidos(x))  