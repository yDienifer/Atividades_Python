# Exercício 4: Escreva um programa que peça ao usuário para adivinhar um número secreto (por exemplo, 42). O programa deve continuar pedindo ao usuário para adivinhar até que ele acerte o número secreto. Quando o usuário acertar, o programa deve imprimir "Parabéns, você acertou!".

numero_secreto = 42


def ColetaNumeroFornecido():
    numero_sugerido = input("fala ai")
    if numero_sugerido.isnumeric() == True:
        print("ok")
        return numero_sugerido
    else:
        print("Por favor, digite apenas números")
        numero_sugerido = ColetaNumeroFornecido()


numero_sugerido = ColetaNumeroFornecido()


def VerificaNumeroSecreto(numero):
    if numero == numero_secreto:
        print("Acertou")
    else:
        print("Errou")
        numero = ColetaNumeroFornecido()


VerificaNumeroSecreto(numero_sugerido)
