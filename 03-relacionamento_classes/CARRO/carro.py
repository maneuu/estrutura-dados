class Carro:
    def __init__(self,cor,placa,motor,dimensao):
        self.__cor = cor
        self.__placa = placa
        self.__motor = motor
        self.__dimensao = dimensao

    @property
    def cor(self):
        return self.__cor
    
    @property
    def placa(self):
        return self.__placa
    @placa.setter
    def placa(self,nova_placa):
        self.__placa = nova_placa

    @property
    def motor(self):
        return self.__motor

    @property
    def dimensao(self):
        return self.__dimensao
    
    
    def __str__(self):
        return f'Cor: {self.__cor}, Placa: {self.__placa}\nMotor: {self.__motor}\nDimensão:{self.__dimensao}'
    