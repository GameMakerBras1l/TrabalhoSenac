class Disk:
    def __init__(self, color, tamanho):
        self.color = color
        self.tamanho = tamanho
    
    def __str__(self):
        return f"{self.color} disk of size {self.tamanho}"