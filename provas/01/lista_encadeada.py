class No:
    """Classe que representa um nó da lista encadeada"""
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    """Classe que implementa uma lista encadeada simples"""
    
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0
    
    def esta_vazia(self):
        """Verifica se a lista está vazia"""
        return self.cabeca is None
    
    def inserir_inicio(self, dado):
        """Insere um elemento no início da lista"""
        novo_no = No(dado)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no
        self.tamanho += 1
    
    def inserir_fim(self, dado):
        """Insere um elemento no final da lista"""
        novo_no = No(dado)
        
        if self.esta_vazia():
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
        
        self.tamanho += 1
    
    def inserir_posicao(self, dado, posicao):
        """Insere um elemento em uma posição específica"""
        if posicao < 0 or posicao > self.tamanho:
            raise IndexError("Posição inválida")
        
        if posicao == 0:
            self.inserir_inicio(dado)
            return
        
        if posicao == self.tamanho:
            self.inserir_fim(dado)
            return
        
        novo_no = No(dado)
        atual = self.cabeca
        
        for i in range(posicao - 1):
            atual = atual.proximo
        
        novo_no.proximo = atual.proximo
        atual.proximo = novo_no
        self.tamanho += 1
    
    def remover_inicio(self):
        """Remove o primeiro elemento da lista"""
        if self.esta_vazia():
            raise ValueError("Lista vazia")
        
        dado_removido = self.cabeca.dado
        self.cabeca = self.cabeca.proximo
        self.tamanho -= 1
        return dado_removido
    
    def remover_fim(self):
        """Remove o último elemento da lista"""
        if self.esta_vazia():
            raise ValueError("Lista vazia")
        
        if self.cabeca.proximo is None:
            return self.remover_inicio()
        
        atual = self.cabeca
        while atual.proximo.proximo:
            atual = atual.proximo
        
        dado_removido = atual.proximo.dado
        atual.proximo = None
        self.tamanho -= 1
        return dado_removido
    
    def remover_valor(self, valor):
        """Remove a primeira ocorrência de um valor específico"""
        if self.esta_vazia():
            raise ValueError("Lista vazia")
        
        if self.cabeca.dado == valor:
            return self.remover_inicio()
        
        atual = self.cabeca
        while atual.proximo:
            if atual.proximo.dado == valor:
                dado_removido = atual.proximo.dado
                atual.proximo = atual.proximo.proximo
                self.tamanho -= 1
                return dado_removido
            atual = atual.proximo
        
        raise ValueError(f"Valor {valor} não encontrado")
    
    def buscar(self, valor):
        """Busca um valor na lista e retorna sua posição"""
        atual = self.cabeca
        posicao = 0
        
        while atual:
            if atual.dado == valor:
                return posicao
            atual = atual.proximo
            posicao += 1
        
        return -1  # Valor não encontrado
    
    def obter_elemento(self, posicao):
        """Obtém o elemento em uma posição específica"""
        if posicao < 0 or posicao >= self.tamanho:
            raise IndexError("Posição inválida")
        
        atual = self.cabeca
        for i in range(posicao):
            atual = atual.proximo
        
        return atual.dado
    
    def __len__(self):
        """Retorna o tamanho da lista"""
        return self.tamanho
    
    def __str__(self):
        """Representação em string da lista"""
        if self.esta_vazia():
            return "[]"
        
        resultado = "["
        atual = self.cabeca
        
        while atual:
            resultado += str(atual.dado)
            if atual.proximo:
                resultado += " -> "
            atual = atual.proximo
        
        resultado += "]"
        return resultado
    
    def __iter__(self):
        """Permite iteração sobre a lista"""
        atual = self.cabeca
        while atual:
            yield atual.dado
            atual = atual.proximo

# Exemplo de uso
if __name__ == "__main__":
    # Criando uma lista encadeada
    lista = ListaEncadeada()
    
    # Inserindo elementos
    print("Inserindo elementos...")
    lista.inserir_fim(10)
    lista.inserir_fim(20)
    lista.inserir_fim(30)
    lista.inserir_inicio(5)
    print(f"Lista: {lista}")
    print(f"Tamanho: {len(lista)}")
    
    # Inserindo em posição específica
    lista.inserir_posicao(15, 2)
    print(f"Após inserir 15 na posição 2: {lista}")
    
    # Buscando elementos
    print(f"Posição do valor 20: {lista.buscar(20)}")
    print(f"Elemento na posição 1: {lista.obter_elemento(1)}")
    
    # Removendo elementos
    removido = lista.remover_inicio()
    print(f"Removido do início: {removido}")
    print(f"Lista após remoção: {lista}")
    
    removido = lista.remover_fim()
    print(f"Removido do fim: {removido}")
    print(f"Lista após remoção: {lista}")
    
    lista.remover_valor(15)
    print(f"Após remover valor 15: {lista}")
    
    # Iterando sobre a lista
    print("Elementos da lista:")
    for elemento in lista:
        print(f"- {elemento}")