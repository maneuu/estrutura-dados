class No:
    """Classe para representar um nó na pilha encadeada"""
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class PilhaEncadeada:
    """Implementação de uma pilha (LIFO) usando lista encadeada"""
    
    def __init__(self):
        self.topo = None  # Referência para o topo da pilha
        self.tamanho = 0  # Tamanho da pilha
    
    def esta_vazia(self):
        """Verifica se a pilha está vazia"""
        return self.topo is None
    
    def empilhar(self, item):
        """Adiciona um item no topo da pilha (O(1))"""
        novo_no = No(item)
        novo_no.proximo = self.topo  # O novo nó aponta para o antigo topo
        self.topo = novo_no           # Atualiza o topo para o novo nó
        self.tamanho += 1
    
    def desempilhar(self):
        """Remove e retorna o item do topo da pilha (O(1))"""
        if self.esta_vazia():
            return None
        
        item_removido = self.topo.dado
        self.topo = self.topo.proximo  # Atualiza o topo para o próximo nó
        self.tamanho -= 1
        return item_removido
    
    def topo_pilha(self):
        """Retorna o item do topo da pilha sem remover"""
        if self.esta_vazia():
            return None
        return self.topo.dado
    
    def obter_tamanho(self):
        """Retorna o tamanho da pilha"""
        return self.tamanho
    
    def __str__(self):
        """Representação em string da pilha"""
        elementos = []
        atual = self.topo
        while atual:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        return "Pilha: [" + ", ".join(elementos) + "]"

# Exemplo de uso

if __name__ == "__main__":
    pilha = PilhaEncadeada()
    
    # Empilhando elementos
    pilha.empilhar(1)
    pilha.empilhar(2)
    pilha.empilhar(3)
    
    print(pilha)  # Saída: Pilha: [3, 2, 1]
    
    # Verificando o topo
    print("Topo da pilha:", pilha.topo_pilha())  # Saída: Topo da pilha: 3
    
    # Desempilhando um elemento
    print("Desempilhado:", pilha.desempilhar())  # Saída: Desempilhado: 3
    print(pilha)  # Saída: Pilha: [2, 1]

    
    # Verificando o tamanho da pilha
    print("Tamanho da pilha:", pilha.obter_tamanho())  # Saída: Tamanho da pilha: 2


    # Desempilhando todos os elementos
    while not pilha.esta_vazia():
        print("Desempilhado:", pilha.desempilhar())
        # Saída: Desempilhado: 2, Desempilhado: 1
    print(pilha)
        # Saída: Pilha: []  