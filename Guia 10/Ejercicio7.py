from typing import List

def promedioEstudiante(lu:str) -> float:
    archivo = open("HistorialNotas.txt", "r")
    notas: List[float] = []
    for linea in archivo:
        if lu in linea:
            datos: List[str] = linea.split(',')
            nota: str = datos[3].replace(" ", "")
            notas.append(float(nota))
    sumaNotas: int = 0
    for notaFlotante in notas:
        sumaNotas += notaFlotante
    archivo.close()
    return sumaNotas / len(notas)

print(str(promedioEstudiante("123")))
