
class Disk:
    def __init__(self, color, size):
        self.color = color
        self.size = size
    
    def __str__(self):
        return f"{self.color} disk of size {self.size}"
    
