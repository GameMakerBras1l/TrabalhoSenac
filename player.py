from pine import Pine

class Player:
    def __init__(self, name, age=18, avgScore=0, avgSolutionTime=0):
        self.name = name
        self.age = age
        self.avgScore = avgScore
        self.avgSolutionTime = avgSolutionTime

    def update_score(self, points):
        self.avgScore += points

    def moveDisk(self, fromPine: Pine, toPine: Pine):
        fromDisk = fromPine.top()

        if fromDisk is None:
            print("Torre de origem vazia!")
            return False

        toDisk = toPine.top()

        # valida regra da Torre de Hanoi
        if toDisk is None or fromDisk.tamanho < toDisk.tamanho:
            toPine.push(fromPine.pop())
            return True
        else:
            print("Movimento inválido!")
            return False
        
    def __str__(self):
        return f"{self.name}: {self.avgScore} points"