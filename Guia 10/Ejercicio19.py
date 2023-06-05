from typing import Dict
from typing import List

def promedioEstudiante(nombreArchivo: str) -> Dict[str, float]:
    archivo = open(nombreArchivo, "r")
    libretas: List[str] = []
    resumen: Dict[str, float] = {}
    for linea in archivo:
        datos: List[str] = linea.split(',')
        if not datos[0] in libretas:
            libretas.append(datos[0])
    archivo.close()
    for libreta in libretas:
        archivo = open(nombreArchivo, "r")
        notas: List[float] = []
        for linea in archivo:
            if libreta in linea:
                datos: List[str] = linea.split(',')
                nota: str = datos[3].replace(" ", "")
                notas.append(float(nota))
        sumaNotas: int = 0
        for notaFlotante in notas:
            sumaNotas += notaFlotante
        archivo.close()
        resumen.update({libreta : round(sumaNotas / len(notas), 2)})
    return resumen


print(str(promedioEstudiante("HistorialNotas.txt")))