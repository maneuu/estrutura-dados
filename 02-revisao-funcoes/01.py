def menor(n1,n2,n3):
    menor_n = n1
    for i in [n2,n3]:
        if i < menor_n:
            menor_n = i
    return menor_n

def fatorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def vertical(s):
    for letra in s:
        print(letra)

print("1 - Teste da função menor()\n")
print(menor(12,10,1))
print(menor(0,-10,1))

print("=" * 20)
print("\n2 - Teste da função fatorial()\n")

print(fatorial(4))
print(fatorial(0))
print(fatorial(1))
print(fatorial(2))

print("=" * 20)
print("\n3 - Teste da função vertical()\n")
vertical("python")
