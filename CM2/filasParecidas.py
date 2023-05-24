from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def filasParecidas(matriz: List[List[int]]) -> bool :
  if esMatriz(matriz):
    nDiferencia: int = 0
    alerta: int = 0
    for fila in range(0,len(matriz),1):
      for columna in range(0,len(matriz[fila]),1):
        if columna == 1:
          nDiferencia = matriz[fila][columna] - matriz[fila-1][columna]
        if matriz[fila][columna] != (matriz[fila-1][columna] + nDiferencia):
          alerta += 1
    return alerta == 0

def esMatriz(listaDeListas: List[List[int]]) -> bool:
  alarma: int = 0
  if len(listaDeListas) > 0 and len(listaDeListas[0]) > 0:
    for iterator in range(0, len(listaDeListas), 1):
      if len(listaDeListas[iterator]) != len(listaDeListas[0]):
        alarma += 1
  else:
    return False
  return alarma == 0

if __name__ == '__main__':
  filas = int(input())
  columnas = int(input())
 
  matriz = []
 
  for i in range(filas):         
    fila = input()
    if len(fila.split()) != columnas:
      print("Fila " + str(i) + " no contiene la cantidad adecuada de columnas")
    matriz.append([int(j) for j in fila.split()])
  
  print(filasParecidas(matriz))