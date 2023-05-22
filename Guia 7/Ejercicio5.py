def evolver_el_doble_si_es_par(numero: int) -> int:
    if (numero % 2 == 0):
        return 2*numero
    else:
        return numero
    
def devolver_valor_si_es_par_sino_el_que_sigue(numero: int) -> int:
    if (numero % 2 == 0):
        return numero
    else:
        return numero + 1

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int:
    if (numero % 3 == 0 and numero % 9 != 0):
        return 2*numero
    elif (numero % 9 == 0):
        return 3*numero
    else:
        return numero

def analizar_de_nombre(nombre: str) -> str:
    if (len(nombre) >= 5):
        return "Tu nombre tiene muchas letras!"
    else:
        return "Tu nombre tiene menos de 5 letras..."
    
def analizar_situacion_argentina(sexo: str, edad: int):
    if (sexo == "F" and edad >= 65):
        print("Anda de vacaciones")
    elif (sexo == "M" and edad >= 60):
        print("Anda de vacaciones")
    else:
        print("Toca laburar")
