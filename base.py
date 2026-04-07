from pine import Pine
from disk import Disk
from typing import List

class Base:
    def __init__(self, name, pine: List[Pine]):
        self.name = name
        self.pine = pine
    
    def addPine(self, pine: Pine):
        self.pine.append(pine)
    
    def removePine(self, pine: Pine):
        self.pine.remove(pine)  

    def __str__(self):
        return f"Base {self.name} with {self.pine}"