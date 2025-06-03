class No:
    """Classe que representa um nó da fila encadeada"""
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class FilaEncadeada:
    """Implementação de uma fila (FIFO) usando lista encadeada"""
    
    def __init__(self):
        self.frente = None  # Primeiro nó (onde remove)
        self.fim = None     # Último nó (onde adiciona)
        self.tamanho = 0
    
    def esta_vazia(self):
        """Verifica se a fila está vazia"""
        return self.frente is None
    
    def enfileirar(self, item):
        """Adiciona um item no final da fila (O(1))"""
        novo_no = No(item)
        
        if self.esta_vazia():
            # Se a fila está vazia, frente e fim apontam para o mesmo nó
            self.frente = novo_no
            self.fim = novo_no
        else:
            # Conecta o novo nó ao final da fila
            self.fim.proximo = novo_no
            self.fim = novo_no
        
        self.tamanho += 1
    
    def desenfileirar(self):
        """Remove e retorna o primeiro item da fila (O(1))"""
        if self.esta_vazia():
            return None
        
        item_removido = self.frente.dado
        self.frente = self.frente.proximo
        
        # Se a fila ficou vazia, atualiza o fim também
        if self.frente is None:
            self.fim = None
        
        self.tamanho -= 1
        return item_removido
    
    def primeiro(self):
        """Retorna o primeiro item da fila sem remover"""
        if self.esta_vazia():
            return None
        return self.frente.dado
    
    def obter_tamanho(self):
        """Retorna o tamanho da fila"""
        return self.tamanho
    
    def __str__(self):
        """Representação em string da fila"""
        if self.esta_vazia():
            return "Fila: []"
        
        elementos = []
        atual = self.frente
        while atual:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        
        return f"Fila: [{' -> '.join(elementos)}] (frente -> fim)"
    
    def __len__(self):
        """Permite usar len() na fila"""
        return self.tamanho


# Exemplo de uso
if __name__ == "__main__":
    print("=== FILA ENCADEADA ===")
    fila = FilaEncadeada()
    
    # Testando fila vazia
    print(f"Fila está vazia: {fila.esta_vazia()}")
    print(f"Tamanho: {len(fila)}")
    print(fila)
    
    # Enfileirando elementos
    print("\n--- Enfileirando elementos ---")
    elementos = [10, 20, 30, 40, 50]
    for elemento in elementos:
        fila.enfileirar(elemento)
        print(f"Enfileirou {elemento}: {fila}")
    
    # Verificando o primeiro elemento
    print(f"\nPrimeiro elemento: {fila.primeiro()}")
    print(f"Tamanho atual: {len(fila)}")
    
    # Desenfileirando elementos
    print("\n--- Desenfileirando elementos ---")
    while not fila.esta_vazia():
        elemento = fila.desenfileirar()
        print(f"Desenfileirou {elemento}: {fila}")
    
    # Testando fila vazia novamente
    print(f"\nApós esvaziar - está vazia: {fila.esta_vazia()}")
    print(f"Desenfileirar de fila vazia: {fila.desenfileirar()}")
    
    # Exemplo prático: Sistema de impressão
