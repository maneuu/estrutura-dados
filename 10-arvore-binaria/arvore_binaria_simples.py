class Nodo:
    """
    Classe que representa um nó da árvore binária.
    Cada nó possui um valor, uma referência para o filho da esquerda e para o filho da direita.
    """
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    """
    Classe que representa a árvore binária em si.
    Possui métodos para inserir nós e percorrer a árvore em ordem.
    """
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        """
        Insere um novo valor na árvore binária.
        """
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, nodo_atual, valor):
        """
        Função auxiliar recursiva para inserir um novo valor.
        """
        if valor < nodo_atual.valor:
            if nodo_atual.esquerda is None:
                nodo_atual.esquerda = Nodo(valor)
            else:
                self._inserir_recursivo(nodo_atual.esquerda, valor)
        else:
            if nodo_atual.direita is None:
                nodo_atual.direita = Nodo(valor)
            else:
                self._inserir_recursivo(nodo_atual.direita, valor)

    def em_ordem(self):
        """
        Percorre a árvore em ordem crescente (em-ordem).
        """
        self._em_ordem_recursivo(self.raiz)

    def _em_ordem_recursivo(self, nodo):
        """
        Função auxiliar recursiva para o percurso em ordem.
        """
        if nodo:
            self._em_ordem_recursivo(nodo.esquerda)  # Visita filho da esquerda
            print(nodo.valor)  # Visita o nó atual
            self._em_ordem_recursivo(nodo.direita)   # Visita filho da direita

# Exemplo de uso
if __name__ == "__main__":
    arvore = ArvoreBinaria()
    # Inserindo valores na árvore
    arvore.inserir(8)
    arvore.inserir(3)
    arvore.inserir(10)
    arvore.inserir(1)
    arvore.inserir(6)
    arvore.inserir(14)
    arvore.inserir(4)
    arvore.inserir(7)

    # Percorrendo a árvore em ordem
    print("Valores da árvore em ordem:")
    arvore.em_ordem()