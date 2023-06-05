from queue import Queue

def cantidadElementos(cola: Queue) -> int:
    return cola.qsize()

colita: Queue = Queue(maxsize=3)

colita.put("AA")
colita.put("BB")
colita.put("CC")

print(str(cantidadElementos(colita)))