from typing import List

# Guia 7 - Ejercicio 6.5 - Monitorear tiempo:

def monitoreo_temporal(anoPartida: int, anoLlegada) -> List[int]:
    anosRetrocedidos: List[int] = []
    for iterador in range(0,(anoPartida-anoLlegada),1):
        anosRetrocedidos.append(anoLlegada+iterador)
    return anosRetrocedidos[::-1]

print(str(monitoreo_temporal(2023, 2012)))