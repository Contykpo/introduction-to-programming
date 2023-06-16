from queue import LifoQueue


# para el tipo pila de enteros, usar: "pila: LifoQueue". La notación "pila: LifoQueue[int]" no funciona.
def calcular_expresion(expr: str) -> float:
    expresion:[str] = expr.split()
    pila: LifoQueue[int] = LifoQueue(maxsize=len(expresion))
    operadores: str = "/*+-"
    for elemeneto in expresion:
        if not elemeneto in operadores:
            pila.put(float(elemeneto))
        elif elemeneto != ' ':
            operadoresDerechos = pila.get()
            operadoresIzquierdos = pila.get()
            if elemeneto == '+':
                pila.put(operadoresIzquierdos + operadoresDerechos)
            elif elemeneto == '-':
                pila.put(operadoresIzquierdos - operadoresDerechos)
            elif elemeneto == '*':
                pila.put(operadoresIzquierdos * operadoresDerechos)
            elif elemeneto == '/':
                pila.put(int(operadoresIzquierdos / operadoresDerechos))
    return pila.get()
    
    
if __name__ == '__main__':
  x = input() # Por ejemplo: 2 5 * 7 +
  print(round(calcular_expresion(x), 5))