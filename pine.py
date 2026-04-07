from disk import Disk
from typing import List

class Pine:
    def __init__(self, stackedDisks: List[Disk]:
        self.stackedDisks = stackedDisks

    def __str__(self):
        return f"Pine with {len(self.stackedDisks)} disks"
    
    def pushDisk(self, disk: Disk):
        self.stackedDisks.append(disk)
    
    def popDisk(self):
        return self.stackedDisks.pop()

