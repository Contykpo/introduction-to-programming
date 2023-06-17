from typing import List
from typing import Dict
import json

def unir_diccionarios(a_unir: List[Dict[str,str]]) -> Dict[str,List[str]]:
  resultado: Dict[str,List[str]] = {}
  for diccionario in a_unir:
    for clave, valor in diccionario.items():
      if clave not in resultado:
        resultado[clave] = [valor]
      else:
        resultado[clave].append(valor)
  return resultado

[{"a":2},{"b":8,"a":5},{"a":7},{"b":3,"a":1},{"c":11,"a":9,"b":1}]

if __name__ == '__main__':
  x = json.loads(input()) # Ejemplo de input: [{"a":2},{"b":3,"a":1}]
  print(unir_diccionarios(x))