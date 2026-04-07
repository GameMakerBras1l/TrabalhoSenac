from disk import Disk
from typing import List

class Pine:
    def __init__(self, name: str):
        self.name = name
        self.discos: List[Disk] = []

    def __str__(self):
        return f"{self.name}: {[d.tamanho for d in self.discos]}"
    
    def push(self, disk: Disk):
        self.discos.append(disk)
    
    def pop(self):
        if self.discos:
            return self.discos.pop()
        return None

    def top(self):
        if self.discos:
            return self.discos[-1]
        return None