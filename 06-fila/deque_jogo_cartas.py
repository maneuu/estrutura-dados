import os
import random
import time
from deque import Deque

# Função para limpar a tela
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para embaralhar o baralho
def criar_baralho():
    naipes = ['♥', '♦', '♣', '♠']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baralho = [f"{valor} {naipe}" for naipe in naipes for valor in valores]
    random.shuffle(baralho)
    return baralho

# Função para exibir o menu
def menu():
    print("\n🎴 Jogo de Cartas no Terminal 🎴")
    print("1. Pegar carta do baralho")
    print("2. Descartar carta")
    print("3. Ver sua mão")
    print("4. Ver monte de descarte")
    print("5. Sair do jogo")

# Função principal do jogo
def main():
    # Inicializando o baralho e os deques
    baralho = criar_baralho()
    monte_descartar = Deque()  # Monte de descarte
    mao = Deque()  # Mão do jogador

    while True:
        clear()
        menu()

        opcao = input("Escolha uma opção (1-5): ")

        if opcao == "1":
            if len(baralho) == 0:
                print("O baralho acabou! Não há mais cartas.")
                time.sleep(2)
                continue
            carta = baralho.pop()
            mao.adicionar_direita(carta)
            print(f"\nVocê pegou a carta: {carta}")
            time.sleep(2)

        elif opcao == "2":
            if mao.esta_vazia():
                print("Sua mão está vazia. Não há cartas para descartar.")
                time.sleep(2)
                continue
            print("Sua mão atual:", mao)
            carta_descartada = input("Qual carta você deseja descartar? (Digite o número ou nome da carta): ")

            # Verificando se a carta está na mão
            carta_encontrada = False
            for carta in mao.itens:
                if carta_descartada in carta:
                    monte_descartar.adicionar_direita(carta)
                    mao.itens.remove(carta)
                    carta_encontrada = True
                    print(f"Carta descartada: {carta}")
                    break
            
            if not carta_encontrada:
                print("Carta não encontrada em sua mão.")
            time.sleep(2)

        elif opcao == "3":
            if mao.esta_vazia():
                print("Sua mão está vazia!")
            else:
                print("Sua mão atual:", mao)
            time.sleep(2)

        elif opcao == "4":
            if monte_descartar.esta_vazia():
                print("O monte de descarte está vazio.")
            else:
                print("Monte de descarte:", monte_descartar)
            time.sleep(2)

        elif opcao == "5":
            print("Saindo do jogo... Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)

if __name__ == "__main__":
    main()
