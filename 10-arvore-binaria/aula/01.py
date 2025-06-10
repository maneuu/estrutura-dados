class No:
    def __init__(self, dado):
        """ Classe que representa um nó da árvore binária.
        """
        self.__dado = dado
        self.__esq = None
        self.__dir = None
    
    @property
    def dado(self):
        """ Retorna o dado do nó.
        """
        return self.__dado
    @dado.setter
    def dado(self, valor):
        """ Define o dado do nó.
        """
        self.__dado = valor
    @property
    def esq(self):
        """ Retorna o filho da esquerda do nó.
        """
        return self.__esq
    @esq.setter
    def esq(self, valor):
        """ Define o filho da esquerda do nó.
        """
        self.__esq = valor

    @property
    def dir(self):
        """ Retorna o filho da direita do nó.
        """
        return self.__dir

    @dir.setter
    def dir(self, valor):
        """ Define o filho da direita do nó.
        """
        self.__dir = valor
    
    def pre_ordem(self,no):
        """ Percorre a árvore em pré-ordem (raiz, esquerda, direita).
        """
         # Se o nó for None, não faz nada
         # Caso contrário, imprime o dado do nó e chama recursivamente os filhos
         # da esquerda e da direita.
        if no == None:
            return
        print(no.dado, end=" ")
        self.pre_ordem(no.esq)
        self.pre_ordem(no.dir)
    
    # usa a logica de pré-ordem para visualizar a árvore
    def visualizar(self,no, n): # n o numero de espaços
        if no == None:
            print('_' * n + 'None')
            return
        print('_' * n + str(no.dado) )
        self.visualizar(no.esq, n + 5)
        self.visualizar(no.dir, n + 5)
    
    def em_ordem(self, no):
        """ Percorre a árvore em ordem (esquerda, raiz, direita).
        """
        if no == None:
            return
        self.em_ordem(no.esq)
        print(no.dado, end=" ")
        self.em_ordem(no.dir)
    
    def pos_ordem(self, no):
        """ Percorre a árvore em pós-ordem (esquerda, direita, raiz).
        """
        if no == None:
            return
        self.pos_ordem(no.esq)
        self.pos_ordem(no.dir)
        print(no.dado, end=" ")


a = No("A")
b = No("B")
c = No("C")
d = No("D")
e = No("E")
f = No("F")
g = No("G")

# Construindo a árvore binária
# A estrutura da árvore será:
#         A
#        / \
#       B   C
#      / \ / \
#     D  E F  G

a.esq = b
a.dir = c

b.esq = d
# b.dir = e

c.esq = f
c.dir = g

print("Pré-ordem:") # Temos certeza que o primeiro a ser impresso é a raiz
# Exemplo de uso
a.pre_ordem(a)

print()  # Para nova linha após a travessia

# Visualizando a árvore e seus níveis
a.visualizar(a, 0)

print("\n\nEm ordem:")
a.em_ordem(a)
print()  # Para nova linha após a travessia

print("\n\nPós-ordem:") # Temos certeza que o ultimo a ser impresso é a raiz
a.pos_ordem(a)
print()  # Para nova linha após a travessia


