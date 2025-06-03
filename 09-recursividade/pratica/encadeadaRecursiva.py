class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def adicionar(self, valor):
        novo_no = Node(valor)
        if not self.cabeca:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def imprimir_recursivo(self, no=None):
        if no is None:
            no = self.cabeca
        if no is not None:
            print(no.valor)
            self.imprimir_recursivo(no.proximo)

# Exemplo de uso:
lista = ListaEncadeada()
lista.adicionar(10)
lista.adicionar(20)
lista.adicionar(30)

lista.imprimir_recursivo()