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
  resultado:List[Dict[str, Union[int, str, Dict[str, int]]]] = []
  for iterador in range(0,pedidos.qsize(),1):
      pedido: Dict[str, Union[int, str, Dict[str, int]]] = pedidos.get()
      pedidoId:str = ""
      pedidoCliente:str = ""
      pedidoProductos: Dict[str,int] = {}
      pedidoPrecioTotal: float = 0.0
      pedidoEstado:str = ""
      for key in pedido.keys():
          if key == 'id':
              pedidoId = pedido.get(key)
          elif key == 'cliente':
              pedidoCliente = pedido.get(key)
          elif key == 'productos':
              pedidoProductos = pedido.get(key)
          if len(pedidoProductos) > 0:
              for keyProducto in pedidoProductos.keys():
                  if keyProducto in stock_productos.keys() and keyProducto in precios_productos.keys():
                      stockProducto:int = stock_productos.get(keyProducto)
                      precioProducto:float = precios_productos.get(keyProducto)
                      cantidadProductos:int = pedidoProductos.get(keyProducto)
                      if pedidoProductos.get(keyProducto) <= stockProducto:
                          pedidoPrecioTotal += cantidadProductos * precioProducto
                          stockProducto -= pedidoProductos.get(keyProducto)
                          stock_productos.update({keyProducto:stockProducto})
                          pedidoEstado = "completo"
                      else:
                          pedidoPrecioTotal += stockProducto * precioProducto
                          pedidoProductos.update({keyProducto: stockProducto})
                          stock_productos.update({keyProducto:0})
                          pedidoEstado = "incompleto"
      pedidoFinal: Dict[str, Union[int, str, Dict[str, int]]] = {
          'id': pedidoId,
          'cliente': pedidoCliente,
          'productos': pedidoProductos,
          'precio_total': pedidoPrecioTotal,
          'estado': pedidoEstado}
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