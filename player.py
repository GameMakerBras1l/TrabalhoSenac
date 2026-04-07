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
        fromDisk = fromPine.popDisk()
        toDisk = toPine.popDisk()
        if (fromDisk.size < toDisk.size) or (toDisk.size == 0):
            toPine.pushDisk(fromDisk)
            fromPine.pushDisk(toDisk)
        else:            
            return False
        
    def __str__(self):
        return f"{self.name}: {self.avgScore} points"