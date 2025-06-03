class Fila:
    def __init__(self):
        self.items = []
    
    def enfileirar(self, item):
        """Adiciona item no final da fila"""
        self.items.append(item)
    
    def desenfileirar(self):
        """Remove e retorna o primeiro item da fila"""
        if len(self.items) == 0:
            return None
        return self.items.pop(0)
    
    def esta_vazia(self):
        """Verifica se a fila está vazia"""
        return len(self.items) == 0
    
    def tamanho(self):
        """Retorna o tamanho da fila"""
        return len(self.items)
    
    def __str__(self):
        return f"Fila: {self.items}"


# Exemplo de uso
fila = Fila()

# Adicionando elementos
fila.enfileirar("A")
fila.enfileirar("B")
fila.enfileirar("C")
print(fila)  # Fila: ['A', 'B', 'C']

# Removendo elementos
print(fila.desenfileirar())  # A
print(fila.desenfileirar())  # B
print(fila)  # Fila: ['C']

print(f"Está vazia: {fila.esta_vazia()}")  # False
print(f"Tamanho: {fila.tamanho()}")  # 1