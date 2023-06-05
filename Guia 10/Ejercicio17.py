from queue import Queue
from typing import Tuple

def numeroDePacientesUrgentes(cola: Queue[Tuple[int,str,str]]) -> int:
    pacientesPrioritarios: int = 0
    for iterador in range(0, cola.qsize(),1):
        paciente: Tuple[int,str,str] = cola.get()
        if paciente[0] >= 1 and paciente[0] <= 3:
            pacientesPrioritarios += 1
    return pacientesPrioritarios

pacientes: Queue[Tuple[int,str,str]] = Queue(maxsize=4)

pacientes.put((1,"Juanes","Le duele todo"))
pacientes.put((2,"Juanes","Le duele el pecho"))
pacientes.put((6,"Juanes","Le duele el traste"))
pacientes.put((7,"Juanes","Le duele el pelo"))

print((str(numeroDePacientesUrgentes(pacientes))))