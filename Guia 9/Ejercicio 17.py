from typing import List

# input list
list1 = ['apple', 'banana', 'watermelon', 'orange']

def calcular_fragmento_mas_largo(fragmentos: List[str]) -> int:
  resultado:int = 0
  longitudMaxima = -1
  for fragmento in fragmentos:
    if (len(fragmento) > longitudMaxima):
      longitudMaxima = len(fragmento)
      resultado = longitudMaxima
  return resultado

print("Longest String is : "+str(calcular_fragmento_mas_largo(list1)))