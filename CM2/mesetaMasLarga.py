from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def mesetaMasLarga(l: List[int]) -> int :
  if len(l) <= 0:
    return 0
  plataforma: int = l[0]
  metrica: int = 0
  metricas: List[int] = []
  for meseta in l:
    if plataforma == meseta:
      plataforma = meseta
      metrica += 1
    else:
      plataforma = meseta
      metricas.append(metrica)
      metrica = 1
  metricas.append(metrica)
  return max(metricas)


if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))