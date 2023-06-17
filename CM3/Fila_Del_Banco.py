from queue import Queue

# El tipo de fila debería ser Queue[int], pero la versión de python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"
def avanzarFila(fila: Queue, min: int):
  cronometro_caja_1: int = 0
  cronometro_caja_2: int = 0
  cronometro_caja_3: int = 0
  cronometro_atendido_3: int = 0
  atendido1: int = 0
  atendido2: int = 0
  atendido3: int = 0
  atendidos: [int] = []
  contadorMinutos: int = 0
  while contadorMinutos <= min:
    if contadorMinutos % 4 == 0:
      fila.put(nueva_persona_n(fila,atendidos))
    # Caja 1
    if contadorMinutos >= 1 and not fila.empty():
      if cronometro_caja_1 == 0:
        if atendido1 in atendidos:
          atendidos.remove(atendido1)
        atendido1 = fila.get()
        atendidos.append(atendido1)
        cronometro_caja_1 = 10
      else:
        cronometro_caja_1 -= 1
    # Caja 2
    if contadorMinutos >= 3 and not fila.empty():
      if cronometro_caja_2 == 0:
        if atendido2 in atendidos:
          atendidos.remove(atendido2)
        atendido2 = fila.get()
        atendidos.append(atendido2)
        cronometro_caja_2 = 4
      else:
        cronometro_caja_2 -= 1
    # Caja 3
    if contadorMinutos >= 2 and not fila.empty():
      if cronometro_caja_3 == 0:
        atendido3 = fila.get()
        atendidos.append(atendido3)
        cronometro_caja_3 = 4
        cronometro_atendido_3 = 3
      else:
        cronometro_caja_3 -= 1
        cronometro_atendido_3 -= 1
    if contadorMinutos >= 2 and cronometro_atendido_3 == 0 and atendido3 in atendidos:
      fila.put(atendido3)
      atendidos.remove(atendido3)
      atendido3 = 0
    contadorMinutos += 1


# Funcion auxiliar para determinar el entero que debe representar la nueva persona que se suma a la fila del banco cada 4 minutos.
def nueva_persona_n(fila: Queue, atendidos: [int]) -> int:
  if fila.qsize() > 0:
    personas: [int] = []
    for iterador in range(0, fila.qsize(), 1):
      personas.append(fila.get())
    maximoPersona: int = personas[0]
    for persona in personas:
      fila.put(persona)
      if persona > maximoPersona:
        maximoPersona = persona
    return maximoPersona + 1
  elif len(atendidos) > 0:
    maximoAtendido: int = atendidos[0]
    for atendido in atendidos:
      if atendido > maximoAtendido:
        maximoAtendido = atendido
    return maximoAtendido + 1
  else:
    return 1


if __name__ == '__main__':
  fila: Queue = Queue()
  fila_inicial: int = int(input())
  for numero in range(1, fila_inicial+1):
    fila.put(numero)
  min: int = int(input())
  avanzarFila(fila, min)
  res = []
  for i in range(0, fila.qsize()):
    res.append(fila.get())
  print(res)


# Caja1: Empieza a atender 10:01, y atiende a una persona cada 10 minutos
# Caja2: Empieza a atender 10:03, atiende a una persona cada 4 minutos
# Caja3: Empieza a atender 10:02, y atiende una persona cada 4 minutos, pero no le resuelve el problema y la persona debe volver a la fila (se va al final y tarda 3 min en llegar. Es decir, la persona que fue atendida 10:02 vuelve a entrar a la fila a las 10:05)
# La fila empieza con las n personas que llegaron antes de que abra el banco. Cuando abre (a las 10), cada 4 minutos llega una nueva persona a la fila (la primera entra a las 10:00)

