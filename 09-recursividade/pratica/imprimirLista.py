# Linked list in a nutshell
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def imprimir_lista_recursivo(no):
    if no is not None:
        print(no.valor)
        imprimir_lista_recursivo(no.proximo)

# outra forma de imprimir a lista
def imprimir_lista2(no):
    if no is None:
        return
    print(no.valor)
    imprimir_lista2(no.proximo)
    

# Exemplo de uso:
# Criando a lista: 1 -> 2 -> 3
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
# Ligando os nós
n1.proximo = n2
n2.proximo = n3
n3.proximo = n4

# Imprimindo a lista recursivamente
imprimir_lista_recursivo(n1)

# Imprimindo a lista usando a segunda função
imprimir_lista2(n1)