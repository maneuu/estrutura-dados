def fat(n):
    if n == 0:
        return 1
    return fat(n-1) * n

# Exemplo de uso:
print(fat(0)) # Saída: 1
print(fat(1)) # Saída: 1
print(fat(2)) # Saída: 2
print(fat(3)) # Saída: 6
print(fat(4)) # Saída: 24
print(fat(5)) # Saída: 120
print(fat(6)) # Saída: 720
print(fat(7)) # Saída: 5040