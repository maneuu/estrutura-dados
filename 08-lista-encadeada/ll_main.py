from lista_encadeada import *

lista = LinkedList()

lista.append(10)
lista.append(20)
lista.append(30)
lista.display()
# Saída: 10 -> 20 -> 30 -> None

lista.insert_at_beginning(5)
lista.display()
# Saída: 5 -> 10 -> 20 -> 30 -> None

lista.insert_at_position(2, 15)
lista.display()
# Saída: 5 -> 10 -> 15 -> 20 -> 30 -> None

lista.remove(20)
lista.display()
# Saída: 5 -> 10 -> 15 -> 30 -> None

pos = lista.search(15)
print(f"Posição do valor 15: {pos}")
# Saída: Posição do valor 15: 2
