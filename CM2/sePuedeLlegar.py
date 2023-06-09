from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
    ciudadActual: str = origen
    vuelosNecesarios: int = 0
    vuelosActuales: List[Tuple[str, str]] = vuelos
    while ciudadActual != destino and len(vuelosActuales) > 0:
      for iterador in range(0,len(vuelosActuales),1):
        if ciudadActual == vuelosActuales[iterador][0]:
          ciudadActual = vuelosActuales[iterador][1]
          vuelosNecesarios += 1
          vuelosActuales.remove(vuelosActuales[iterador])
          break
        if iterador == (len(vuelosActuales)-1):
          return -1
    if ciudadActual != destino:
      return -1
    else:
      return vuelosNecesarios


if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))