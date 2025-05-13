class Fila:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if self.esta_vazia():
            return None
        return self.itens.pop(0)

    def frente(self):
        if self.esta_vazia():
            return None
        return self.itens[0]

    def tamanho(self):
        return len(self.itens)

    def __str__(self):
        return "Fila: " + " -> ".join(str(item) for item in self.itens)

fila = Fila()

fila.enfileirar("A")
fila.enfileirar("B")
fila.enfileirar("C")

print(fila)  # Fila: A -> B -> C

fila.desenfileirar()

print(fila)  # Fila: B -> C
