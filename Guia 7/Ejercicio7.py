def numeros_1_al_100():
    for iterador in range(1,11,1):
        print(iterador)

def numeros_pares_entre_10_y_40():
    for iterador in range(10,41,2):
        print(iterador)

def eco_10_veces():
    for iterador in range(1,11,1):
        print("eco")

def viajar_en_el_tiempo(añoPartida: int, añoLlegada: int):
    for iterador in range(añoPartida,añoLlegada-1,-1):
        print("Viajaste al año:"+str(iterador))

def viajar_hasta_conocer_a_Aristoteles(añoPartida: int):
    if (añoPartida <= -404):
        print("No llegas a conocer a Aristoteles")
    else:
        for iterador in range(añoPartida,-384-1,-20):
            print("Kalimera Aristoteles")