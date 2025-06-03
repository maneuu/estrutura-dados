# def potencia(base, n):
#     if n == 0:
#         return 1.0
#     return (base ** n) *  potencia(base,n-1)

# print(potencia(2,2))


def pot(x,n):
    if n == 0:
        return 1
    return x * pot(x,n-1)