import sys

def quienGana(j1: str, j2: str) -> str:
    opcionesDisponibles = ["Piedra", "Papel", "Tijera"]
    if (j1 in opcionesDisponibles) and (j2 in opcionesDisponibles):
        if j1 == j2:
            return "Empate"
        elif j1 == "Piedra":
            if j2 == "Tijera":
                return "Jugador1"
            else:
                return "Jugador2"
        elif j1 == "Papel":
            if j2 == "Piedra":
                return "Jugador1"
            else:
                return "Jugador2"
        elif j1 == "Tijera":
            if j2 == "Papel":
                return "Jugador1"
            else:
                return "Jugador2"
    else:
        return ""

if __name__ == '__main__':
  x = input()
  jug = str.split(x)
  print(quienGana(jug[0], jug[1]))