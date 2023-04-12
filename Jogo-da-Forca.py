import random
from os import system, name

# Pseudocódigo

# 1. Definir uma lista de palavras possíveis
# 2. Escolher uma palavra aleatoriamente da lista
# 3. Definir o número máximo de tentativas
# 4. Enquanto o número de tentativas não for atingido (6):
#  4.1. Mostrar a palavra como uma série de underlines, com as lestras adivinhadas preechidas
#  4.2. Pedir ao jogador que adivinhe uma letra (input)
#  4.3. Verificar se a letra está na palavra
#  4.4. Se a letra está na palavra, adicionar na lista de palavras adivinhadas e atualizar na exibição da palavra
#  4.5. Se a letra nao esta na palavra diminuir número máximo de tentativas restantes e exibir a mensagem "Letra incorreta. Tentativas restantes: [número]"
#  4.6. Verificar se todas as letras foram adivinhadas
#  4.7. Se sim, exibir a mensagem "Você venceu!"
#  4.8. Se o número de tentativas chegar a zero, exibir a mensagem "Você perdeu. A palavra era [palavra]" e encerrar o jogo.

# Limpar a tela a cada execução
def limpar_tela():
    if name == 'nt':      #Windowns
        _ = system('cls')
    else:                 # Linux e Mac
        _ = system('clear')

# Estrutura da Forca:

def hangman(chance):
    forma = [
        """
        -------
        |     |
        O     |
       \|/    |
        |     |
       / \    |
             --- """,

        """
        -------
        |     |
        O     |
       \|/    |
        |     |
       /      |
             --- """,
        """
        -------
        |     |
        O     |
       \|/    |
        |     |
              |
             --- """,
        """
        -------
        |     |
        O     |
       \|     |
        |     |
              |
             --- """,
        """
        -------
        |     |
        O     |
        |     |
        |     |
              |
             --- """,
        """
        -------
        |     |
        O     |
              |
              |
              |
             --- """,

        """
        -------
        |     |
              |
              |
              |
              |
             --- """
    ]
    return forma[chance]


def jogo():
    limpar_tela()

    print("\nBem-vindo ao jogo. O tema é: Frutas")
    print("Adivinhe a palavra abaixo\n")

    frutas = ["maça", "uva", "banana", "laranja", "melancia", "melão", "morango", "abacate", "abacaxi"]
    fruta_selecionada = random.choice(frutas)

    # Número de chance antes de formar o boneco completo
    N_chance = 6

    # Display do tabuleiro
    display = ["_"] * len(fruta_selecionada)

    # Lista com as letras da palavra
    letras_palavra = []
    for letra in fruta_selecionada:
        letras_palavra.append(letra)

        # Input de letras corretas
    letras_corretas = []

    # Input de letras erradas
    letras_erradas = []

    #  Looping para estruturar o jogo
    while N_chance > 0:

        print(hangman(N_chance))
        print("Palavra: ", display)
        print("\n")

        tentativa = input("\nDigite uma letra: ")

        if tentativa in letras_corretas or tentativa in letras_erradas:
            print("\nVocê já tentou essa letra. Tente outra.")
            continue

        if tentativa in letras_palavra:
            print("Você acertou uma letra.")
            print("Letras erradas: ", letras_erradas)

            letras_corretas.append(tentativa)

            for i in range(len(letras_palavra)):
                if letras_palavra[i] == tentativa:
                    display[i] = tentativa

            # Se "-" não aparece mais na palavra, significa que todas letras foram adivinhadas
            if "_" not in display:
                print("\nVocê venceu! A palavra era:", fruta_selecionada)
                break

        else:
            print("Essa letra não está na palavra!")
            letras_erradas.append(tentativa)
            print("Letras erradas: ", letras_erradas)
            N_chance = N_chance - 1

    if "_" in display:
        print("\nVocê perdeu! A palavra era:", fruta_selecionada)

if __name__ == "__main__":
    jogo()