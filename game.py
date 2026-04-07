from pine import Pine
from disk import Disk
from base import Base
from player import Player

class Game:
    def __init__(self, name, n_discos=3):
        self.name = name
        
        # Criar jogador
        nome = input("Digite seu nome: ")
        self.player = Player(nome)

        # Criando torres
        self.pineA = Pine("A")
        self.pineB = Pine("B")
        self.pineC = Pine("C")

        # Base com torres
        self.base = Base(name, [self.pineA, self.pineB, self.pineC])

        # Criando discos (maior embaixo → menor em cima)
        for i in range(n_discos, 0, -1):
            self.pineA.push(Disk("azul", i))

        self.n_discos = n_discos

    # Mostrar estado do jogo
    def mostrar(self):
        print("\nEstado atual:")
        for pine in self.base.pines:
            print(pine)

    # Verificar vitória
    def venceu(self):
        return len(self.pineC.discos) == self.n_discos

    # Loop principal
    def jogar(self):
        print(f"\n=== {self.name} ===")

        while True:
            self.mostrar()

            origem = input("Origem (A/B/C): ").upper()
            destino = input("Destino (A/B/C): ").upper()

            origem_pine = self.base.getPine(origem)
            destino_pine = self.base.getPine(destino)

            if origem_pine is None or destino_pine is None:
                print("Torre inválida!")
                continue

            # Movimento usando Player
            if self.player.moveDisk(origem_pine, destino_pine):
                self.player.update_score(1)

            # Verifica vitória
            if self.venceu():
                self.mostrar()
                print(f"\n🎉 {self.player.name} venceu!")
                print(f"Movimentos: {self.player.avgScore}")
                break