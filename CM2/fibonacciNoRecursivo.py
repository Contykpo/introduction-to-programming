import sys

def fibonacciNoRecursivo(n: int) -> int:
  if n >= 0:
    a: int = 0
    b: int = 1
    for i in range(0, n):
      a, b = b, a + b
    return a
  else:
    return 0

if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))