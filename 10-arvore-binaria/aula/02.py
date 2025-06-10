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

class ArvoreBinaria:
    def __init__(self):
        """ Classe que representa a árvore binária.
        """
        self.__raiz = None

    @property
    def raiz(self):
        """ Retorna a raiz da árvore.
        """
        return self.__raiz
    
    def vazia(self):
        """ Verifica se a árvore está vazia.
        """
        return self.__raiz is None
    def inserir_raiz(self, dado):
        """ Insere um novo nó na raiz da árvore.
        """
        self.__raiz = No(dado)
    
    def visualizar(self,no,n):
        """ Visualiza a árvore.
        """
        if no == None:
            print('_' * n + 'None')
            return
        print('_' * n + str(no.dado))
        self.visualizar(no.esq, n + 5)
        self.visualizar(no.dir, n + 5)


    def buscar(self, no,valor):
        """ Busca um valor na árvore.
        Retorna o nó se encontrado, caso contrário retorna None.
        """
        if no == None:
            return None
        if no.dado == valor:
            return no
        achou = self.buscar(no.esq, valor)
        if not achou:
            return self.buscar(no.dir, valor)
        return achou
    
    def ins_esq(self,pai,filho):
        """ Insere um filho à esquerda de um nó pai.
        """
        no_pai = self.buscar(self.__raiz, pai)
        if no_pai is None:
            print(f"Nó pai '{pai}' não encontrado.")
            return False
        if no_pai.esq is not None:
            print(f"Nó pai '{pai}' já possui um filho à esquerda.")
            return False
        no_filho = No(filho)
        no_pai.esq = no_filho
        return True
    
    def ins_dir(self,pai,filho):
        """ Insere um filho à direita de um nó pai.
        """
        no_pai = self.buscar(self.__raiz, pai)
        if no_pai is None:
            print(f"Nó pai '{pai}' não encontrado.")
            return False
        if no_pai.dir is not None:
            print(f"Nó pai '{pai}' já possui um filho à direita.")
            return False
        no_filho = No(filho)
        no_pai.dir = no_filho
        return True
    
    def esvaziar(self):
        """ Esvazia a árvore, removendo todos os nós.
        """
        self.__raiz = None

        
a = ArvoreBinaria()
a.inserir_raiz("A")

a.ins_esq("A", "B")
a.ins_dir("A", "C")

a.ins_esq("B", "D")
a.ins_dir("B", "E")
a.ins_esq("C", "F")
a.ins_dir("C", "G")
a.visualizar(a.raiz, 0)