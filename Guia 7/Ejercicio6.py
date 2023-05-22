def numeros_1_al_100():
    iterador: int = 1
    while (iterador <= 10):
        print(iterador)
        iterador += 1

def numeros_pares_entre_10_y_40():
    iterador: int = 10
    while (iterador <= 40):
        print(iterador)
        iterador += 2

def eco_10_veces():
    iterador: int = 1
    while (iterador <= 10):
        print("eco")
        iterador += 1

def viajar_en_el_tiempo(añoPartida: int, añoLlegada: int):
    iterador: int = (añoPartida-1)
    while (iterador >= añoLlegada):
        print("Viajaste al año:"+str(iterador))
        iterador -= 1

def viajar_hasta_conocer_a_Aristoteles(añoPartida: int):
    iterador: int = añoPartida
    if (añoPartida <= -404):
        print("No llegas a conocer a Aristoteles")
    else:
        while (iterador >= -384):
            print("Kalimera Aristoteles")
            iterador -= 20