from pilha import Pilha

opcoes = """\n
EDITOR DE PILHA
[1] EMPILHAR
[2] DESEMPILHAR
[3] EXIBIR ELEMENTO DO TOPO
[4] EXIBIR A PILHA
[5] TAMANHO DA PILHA
[6] ESVAZIAR A PILHA
[0] SAIR

"""
pilha = Pilha()
print(opcoes)
while True:
    
    valor = input('\nDIGITE SUA OPÇÃO: ')
    if valor == '1':
        pilha.empilhar(int(input('VALOR PARA EMPILHAR: ')))
    elif valor == '2':
        removido = pilha.desempilhar()
        if removido:
            print(f'Desempilhado o valor {removido}')
        else:
            print('Não há elemento para desempilhar')
    elif valor == '3':
        topo = pilha.topo()
        if topo:
            print(f'O topo da pilha e o valor {pilha.topo()}')
        else:
            print(f'A pilha esta vazia')
    elif valor == '4':
        print(f'Valores da pilha atual: {pilha}')
        
    elif valor == '5':
        
        valores = []

        while not pilha.vazia():
            valores.append(pilha.desempilhar())
        
        print(f'O tamanho da pilha é {len(valores)}')

        while len(valores) != 0:
            pilha.empilhar(valores.pop())

    elif valor == '6':
        while not pilha.vazia():
            pilha.desempilhar()
        print('Pilha foi esvaziada')
    elif valor == '0':
        print('Encerrado o programa......')
        break
    else:
        print('Digite um valor valido')