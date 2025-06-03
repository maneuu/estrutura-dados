class Pilha:
    def __init__(self):
        self.items = []
    
    def empilhar(self, item):
        """Adiciona item no topo da pilha"""
        self.items.append(item)
    
    def desempilhar(self):
        """Remove e retorna o item do topo da pilha"""
        if len(self.items) == 0:
            return None
        return self.items.pop()
    
    def topo(self):
        """Retorna o item do topo sem remover"""
        if len(self.items) == 0:
            return None
        return self.items[-1]
    
    def esta_vazia(self):
        """Verifica se a pilha está vazia"""
        return len(self.items) == 0
    
    def tamanho(self):
        """Retorna o tamanho da pilha"""
        return len(self.items)
    
    def __str__(self):
        return f"Pilha: {self.items}"


# Exemplo de uso
pilha = Pilha()

# Empilhando elementos
pilha.empilhar("A")
pilha.empilhar("B")
pilha.empilhar("C")
print(pilha)  # Pilha: ['A', 'B', 'C']

# Vendo o topo
print(f"Topo: {pilha.topo()}")  # Topo: C

# Desempilhando elementos
print(pilha.desempilhar())  # C
print(pilha.desempilhar())  # B
print(pilha)  # Pilha: ['A']

print(f"Está vazia: {pilha.esta_vazia()}")  # False
print(f"Tamanho: {pilha.tamanho()}")  # 1