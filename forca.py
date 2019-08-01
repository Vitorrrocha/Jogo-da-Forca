from random import randrange
from time import sleep
import os


def jogar():

    mensagem_abertura()

    palavra_secreta = leitura_palavra_secreta()



    letras_acertadas = ["_" for letra in palavra_secreta]     #Imprime o caracter '_' para cada letra na palavra_secreta
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0


    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute,palavra_secreta,letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    print("Fim do jogo")


def mensagem_abertura():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    print()

def leitura_palavra_secreta():

    escolha = int(input('''!!MODO DE JOGO!!\n[1] - Escolha a palavra secreta\n[2] - Palavra aleatoria\n\n'''))
    print()
    print()


    if escolha == 1:
        print('Atenção, quem ira adivinhar não podera ver voce escrevendo a palavra que sera adivinhada')

        palavra_secreta = input("Digite a palavra que ira ser adivinhada: ").upper().strip()

        os.system('clear')

        return palavra_secreta

    if escolha == 2: 
        arquivo = open('palavras.txt')

        palavras = []

        for linha in arquivo:
            palavras.append(linha.strip())

        arquivo.close()

        num = randrange(0, len(palavras))

        palavra_secreta = palavras[num].upper()

        return palavra_secreta

        print(palavra_secreta)


def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute,palavra_secreta,letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
        
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    sleep(6)
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    sleep(6)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if(__name__ == "__main__"):
    jogar()
