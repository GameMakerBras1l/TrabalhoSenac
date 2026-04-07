from pine import Pine
from disk import Disk
from base import Base

class Game:
    def __init__(self, name, n_discos=3):
        self.name = name
        
        # Criando torres
        self.pineA = Pine("A")
        self.pineB = Pine("B")
        self.pineC = Pine("C")

        # Base contendo as torres
        self.base = Base(name, [self.pineA, self.pineB, self.pineC])

        # Criando discos (do maior pro menor)
        for i in range(n_discos, 0, -1):
            self.pineA.push(Disk(i))

        self.n_discos = n_discos

    # Mostrar estado do jogo
    def mostrar(self):
        print("\nEstado atual:")
        for pine in self.base.pines:
            print(pine)

    # Validar e fazer movimento
    def mover(self, origem_nome, destino_nome):
        origem = self.base.getPine(origem_nome)
        destino = self.base.getPine(destino_nome)

        if origem is None or destino is None:
            print("Torre inválida!")
            return False

        disco = origem.top()

        if disco is None:
            print("Torre de origem vazia!")
            return False

        topo_destino = destino.top()

        if topo_destino and topo_destino.tamanho < disco.tamanho:
            print("Movimento inválido!")
            return False

        destino.push(origem.pop())
        return True

    # Verificar vitória
    def venceu(self):
        return len(self.pineC.discos) == self.n_discos

    # Loop principal
    def jogar(self):
        print(f"=== {self.name} ===")

        while True:
            self.mostrar()

            origem = input("Origem (A/B/C): ").upper()
            destino = input("Destino (A/B/C): ").upper()

            self.mover(origem, destino)

            if self.venceu():
                self.mostrar()
                print("🎉 Você venceu!")
                break