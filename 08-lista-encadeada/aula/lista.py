class No:
    def __init__(self, dado, prox=None):
        self.__dado = dado
        self.__prox = prox  # use __prox como o atributo real

    @property
    def dado(self):
        return self.__dado

    @dado.setter
    def dado(self, dado):
        self.__dado = dado

    @property
    def prox(self):
        return self.__prox  # correto: acessa o atributo interno

    @prox.setter
    def prox(self, prox):
        self.__prox = prox  # correto: define o atributo interno

    def __str__(self):
        return f"{self.__dado}"




class Lista:
    def __init__(self):
        self.__inicio = None

    def vazia(self):
        return self.__inicio is None

    def inserir_inicio(self, dado):
        novo_no = No(dado, self.__inicio)
        self.__inicio = novo_no

    def inserir_final(self, dado):
        novo_no = No(dado)
        if self.vazia():
            self.__inicio = novo_no
        else:
            atual = self.__inicio
            while atual.prox is not None:
                atual = atual.prox
            atual.prox = novo_no

    
    def inserir_posicao(self, posicao, dado):
        if posicao < 0 or posicao > self.tamanho():
            # raise IndexError("Posição inválida")
            print("Posição inválida")

        if posicao == 0:
            self.inserir_inicio(dado)
            return

        atual = self.__inicio
        contador = 0

        while contador < posicao - 1:
            atual = atual.prox
            contador += 1

        novo_no = No(dado, atual.prox)
        atual.prox = novo_no



    def tamanho(self):
        atual = self.__inicio
        cont = 0
        while atual is not None:
            cont += 1
            atual = atual.prox
        return cont

    def imprimir(self):
        dado_atual = self.__inicio
        resultado = ''
        while dado_atual is not None:
            resultado += f'{dado_atual} -> '
            dado_atual = dado_atual.prox
        resultado += 'None'
        print(resultado)
