class Pilha:
    def __init__(self):
        self.__itens = []

    def vazia(self):
        return len(self.__itens) == 0

    def topo(self):
        if(self.vazia()):
            return None
        return self.__itens[-1]

    def empilhar(self, item):
        self.__itens.append(item)

    def desempilhar(self):
        if(self.vazia()):
            return None
        return self.__itens.pop()

    def __str__(self):
        return self.__itens.__str__()
