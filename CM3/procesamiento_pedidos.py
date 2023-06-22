from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json

# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"
def procesamiento_pedidos(pedidos: Queue,
                          stock_productos: Dict[str, int],
                          precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
  resultado = []
  while not pedidos.empty():
    pedido = pedidos.get()
    pedidoFinal = {
      "id": pedido["id"],
      "cliente": pedido["cliente"],
      "productos": {},
      "precio_total": 0.0,
      "estado": "completo"
    }
    for producto, cantidad in pedido["productos"].items():
      if producto not in stock_productos or stock_productos[producto] < cantidad:
        pedidoFinal["estado"] = "incompleto"
        cantidad_disponible = stock_productos.get(producto)
        pedidoFinal["productos"][producto] = min(cantidad_disponible, cantidad)
        pedidoFinal["precio_total"] += min(cantidad_disponible, cantidad) * precios_productos[producto]
        stock_productos[producto] -= min(cantidad_disponible, cantidad)
      else:
        stock_productos[producto] -= cantidad
        pedidoFinal["productos"][producto] = cantidad
        pedidoFinal["precio_total"] += cantidad * precios_productos[producto]
    resultado.append(pedidoFinal)
  return resultado


if __name__ == '__main__':
  pedidos: Queue = Queue()
  list_pedidos = json.loads(input())
  [pedidos.put(p) for p in list_pedidos]
  stock_productos = json.loads(input())
  precios_productos = json.loads(input())
  print("{} {}".format(procesamiento_pedidos(pedidos, stock_productos, precios_productos), stock_productos))


# Ejemplo input  
# pedidos: [{"id":21,"cliente":"Gabriela", "productos":{"Manzana":2}}, {"id":1,"cliente":"Juan","productos":{"Manzana":2,"Pan":4,"Factura":6}}]
# stock_productos: {"Manzana":10, "Leche":5, "Pan":3, "Factura":0}
# precios_productos: {"Manzana":3.5, "Leche":5.5, "Pan":3.5, "Factura":5}