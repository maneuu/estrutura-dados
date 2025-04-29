class ContaCorrente:
    def __init__(self,numero,nome_titular):
        self.__numero = numero
        self.__saldo= 0
        self.__nome_titular = nome_titular
    
    def depositar(self,depositado):
        self.__saldo += depositado

    def sacar(self,sacado):
        if (self.__saldo - sacado) >= 0:
            self.__saldo -= sacado
            return True
        return False 
