from pilha import Pilha

valor = input('String: ')

pilha = Pilha()
valores = []
for char in valor:
    if char.isalpha():
        valores.append(char)

resultado_1 = ''.join(valores).lower()

while len(valores) != 0:
    pilha.empilhar(valores.pop())

valores = []
while not pilha.vazia():
    valores.append(pilha.desempilhar())

resultado_2 = ''.join(valores).lower()

def eh_palindromo(a,b):
    if a == b:
        print('Eh palindromo')
    else:
        print('Não eh palindromo')