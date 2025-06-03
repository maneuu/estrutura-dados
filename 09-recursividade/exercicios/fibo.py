def fibonacci(n):
    if n <= 1:  # Casos base
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# Outra forma
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
# Testando a função
for i in range(10):
    print(f"Fibonacci de {i} é {fibonacci(i)}")

print("\n")
# Testando a outra forma
for i in range(2,10):
    print(f"Fibonacci de {i} é {fib(i)}")