from carro import Carro
from motor import Motor
from dimensao import Dimensao

dimensao = Dimensao(1.67,1.81,4.37)
motor = Motor('1.6', 'gasolina')
carro = Carro('preto', 'ABC1234', motor, dimensao)
print(carro)

print(f'\nMOTOR ATUAL: {carro.motor.motorizacao}')
carro.motor.motorizacao = '2.0'
print(f"\nNOVO MOTOR: {carro.motor.motorizacao}")