from typing import List
from typing import Dict
import json

def unir_diccionarios(a_unir: List[Dict[str,str]]) -> Dict[str,List[str]]:
  resultado: Dict[str, str] = {}
  for diccionario in a_unir:
    listaValores: List[str] = []
    for key in diccionario.keys():
      if key in resultado.keys():
        listaValores.append(diccionario.get(key))
        for elemento in resultado.get(key):
          if elemento not in listaValores:
            listaValores.append(elemento)
        resultado.update({key: listaValores[::-1]})
      else:
        resultado.update({key: diccionario.get(key)})
  return resultado


if __name__ == '__main__':
  x = json.loads(input()) # Ejemplo de input: [{"a":2},{"b":3,"a":1}]
  print(unir_diccionarios(x))