def menu():
    print("\n🧭 MENU DO DEQUE:")
    print("1. Adicionar à direita")
    print("2. Adicionar à esquerda")
    print("3. Remover da direita")
    print("4. Remover da esquerda")
    print("5. Ver item na frente")
    print("6. Ver item no final")
    print("7. Ver tamanho do deque")
    print("8. Mostrar deque")
    print("9. Ver representação interna (repr)")
    print("0. Sair")

class Deque:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def adicionar_direita(self, item):
        self.itens.append(item)

    def adicionar_esquerda(self, item):
        self.itens.insert(0, item)

    def remover_direita(self):
        if self.esta_vazia():
            return None
        return self.itens.pop()

    def remover_esquerda(self):
        if self.esta_vazia():
            return None
        return self.itens.pop(0)

    def frente(self):
        if self.esta_vazia():
            return None
        return self.itens[0]

    def final(self):
        if self.esta_vazia():
            return None
        return self.itens[-1]

    def tamanho(self):
        return len(self.itens)

    def __len__(self):
        return len(self.itens)

    def __str__(self):
        if self.esta_vazia():
            return "Deque vazia!"
        return "Deque: " + " <-> ".join(str(item) for item in self.itens)

    def __repr__(self):
        return f"Deque({self.itens})"

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    deque = Deque()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = input("Digite o valor para adicionar à direita: ")
            deque.adicionar_direita(valor)
            print("✅ Adicionado à direita!")
        elif opcao == "2":
            valor = input("Digite o valor para adicionar à esquerda: ")
            deque.adicionar_esquerda(valor)
            print("✅ Adicionado à esquerda!")
        elif opcao == "3":
            removido = deque.remover_direita()
            print(f"🗑️ Removido da direita: {removido}" if removido is not None else "⚠️ Deque está vazio!")
        elif opcao == "4":
            removido = deque.remover_esquerda()
            print(f"🗑️ Removido da esquerda: {removido}" if removido is not None else "⚠️ Deque está vazio!")
        elif opcao == "5":
            print(f"👁️ Frente do deque: {deque.frente()}")
        elif opcao == "6":
            print(f"🔚 Final do deque: {deque.final()}")
        elif opcao == "7":
            print(f"📏 Tamanho do deque: {len(deque)}")
        elif opcao == "8":
            print(deque)
        elif opcao == "9":
            print(f"📦 Representação interna: {repr(deque)}")
        elif opcao == "0":
            print("Encerrando o programa. 👋")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")
        
        input()
        clear()

if __name__ == "__main__":
    main()
