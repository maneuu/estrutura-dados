# passagem por referencia so funciona com objetos mutaveis como lista e dict , não com strings int float tuplas 


def adicionar_elementos(lista):
    lista.append(10)

valores = [1,2,3]
adicionar_elementos(valores)
print(valores)


def aumentar_numero(x):
    x += 1

n = 1
aumentar_numero(n)
print(n)