import os
import time

# Função para limpar a tela
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

from fila import Fila

# Função para exibir o menu
def menu():
    print("\n💼 GUICHÊ DE ATENDIMENTO 💼")
    print("1. Adicionar cliente à fila")
    print("2. Atender próximo cliente")
    print("3. Ver próximo cliente")
    print("4. Ver fila atual")
    print("5. Sair")


# Função principal do sistema de guichê
def main():
    fila = Fila()  # Inicializa a fila

    while True:
        clear()
        menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cliente = input("Digite o nome do cliente: ").strip()
            print(f"{cliente} está entrando na fila...")
            fila.enfileirar(cliente)
            print(f"✅ {cliente} entrou na fila!")
            time.sleep(2)

        elif opcao == "2":
            if fila.esta_vazia():
                print("Nenhum cliente na fila para ser atendido.")
            else:
                cliente_atendido = fila.desenfileirar()
                print(f"🎉 {cliente_atendido} foi atendido com sucesso!")
            time.sleep(2)

        elif opcao == "3":
            proximo_cliente = fila.frente()
            if proximo_cliente:
                print(f"👀 Próximo a ser atendido: {proximo_cliente}")
            else:
                print("A fila está vazia.")
            time.sleep(2)

        elif opcao == "4":
            print("Fila atual:")
            print(fila)
            time.sleep(3)

        elif opcao == "5":
            print("Finalizando o atendimento... Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)


if __name__ == "__main__":
    main()
