from typing import List

def estaBienBalanceada(formula: str) -> bool:
    formulaSinEspacios: str = formula.replace(" ", "")
    parentesisAbiertos: int = 0
    parentesisCerrados: int = 0
    caracterOperando: str = ""
    operadores: List[str] = ["+", "-", "*","/"]
    for iterador in range(0,len(formulaSinEspacios),1):
        if formulaSinEspacios[iterador] in operadores:
            caracterOperando = formulaSinEspacios[iterador]
        if formulaSinEspacios[iterador] == "(":
            parentesisAbiertos += 1
            if caracterOperando == "" and formulaSinEspacios[iterador] == formulaSinEspacios[0]:
                return False
        if formulaSinEspacios[iterador] == ")":
            parentesisCerrados += 1
        if parentesisCerrados >= 1 and caracterOperando == "" and formulaSinEspacios[iterador] == formulaSinEspacios[len(formulaSinEspacios)-1]:
            return False
        if parentesisAbiertos < parentesisCerrados:
            return False
    return parentesisAbiertos == parentesisCerrados


print(str(estaBienBalanceada("1 + )2 * 3(")))