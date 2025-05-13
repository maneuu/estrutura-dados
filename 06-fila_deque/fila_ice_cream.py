import time
from fila import Fila


def menu():
    print("\n🍦 BEM-VINDO À SORVETERIA VIRTUAL 🍦")
    print("1. Adicionar cliente à fila")
    print("2. Atender próximo cliente")
    print("3. Ver próximo da fila")
    print("4. Ver fila atual")
    print("5. Sair")

def carregando(texto="Processando", pontos=3, tempo=0.5):
    for _ in range(pontos):
        print(texto + "." * (_ + 1))
        time.sleep(tempo)

def main():
    fila = Fila()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do cliente: ").strip()
            print(f"{nome} está entrando na fila...")
            time.sleep(1)
            fila.enfileirar(nome)
            print(f"✅ {nome} entrou na fila!")
        elif opcao == "2":
            if fila.esta_vazia():
                print("Nenhum cliente na fila.")
            else:
                cliente = fila.frente()
                print(f"Chamando {cliente} para atendimento...")
                carregando("🍦 Preparando o sorvete", 4, 0.6)
                atendido = fila.desenfileirar()
                print(f"✅ {atendido} foi atendido! Aproveite o sorvete 😋")
        elif opcao == "3":
            proximo = fila.frente()
            if proximo:
                print(f"👀 Próximo a ser atendido: {proximo}")
            else:
                print("A fila está vazia.")
        elif opcao == "4":
            print(fila)
        elif opcao == "5":
            print("Encerrando o sistema...")
            carregando("Finalizando", 3, 0.7)
            print("Até a próxima! 👋")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
