from pine import Pine
from typing import List

class Base:
    def __init__(self, name: str, pines: List[Pine]):
        self.name = name
        self.pines = pines
    
    def addPine(self, pine: Pine):
        if pine not in self.pines:
            self.pines.append(pine)
    
    def removePine(self, pine: Pine):
        if pine in self.pines:
            self.pines.remove(pine)  

    def getPine(self, name: str):
        for pine in self.pines:
            if pine.name == name:
                return pine
        return None

    def __str__(self):
        resultado = f"\nBase {self.name}\n"
        for pine in self.pines:
            resultado += f"{pine}\n"
        return resultado