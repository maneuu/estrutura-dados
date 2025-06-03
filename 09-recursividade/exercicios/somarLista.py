def soma(lista):
    if len(lista) == 0:
        return 0
    ultimo = lista.pop()
    return ultimo + soma(lista)

print(soma([1, 2, 3, 4, 5]))  # Output: 15

print("\n")
# Outra forma de implementar a soma recursiva
def soma2(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + soma2(lista[1:])

print(soma2([1, 2, 3, 4, 5, 6]))  # Output: 21