class Dimensao:
    def __init__(self,altura, largura, comprimento):
        self.__altura = altura
        self.__largura = largura
        self.__comprimento = comprimento

    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self,nova_altura):
        self.__altura = nova_altura
    
    @property
    def largura(self):
        return self.__largura 
    
    @largura.setter
    def largura(self,nova_largura):
        self.__largura = nova_largura

    @property
    def comprimento(self):
        return self.__comprimento
    
    @comprimento.setter
    def comprimento(self,novo_comprimento):
        self.__comprimento = novo_comprimento
    
    def __str__(self):
        return f'Altura: {self.__altura}, Largura: {self.__largura}, Comprimento: {self.__comprimento}'
    

dimensao = Dimensao(1.67,1.81,4.37)

        