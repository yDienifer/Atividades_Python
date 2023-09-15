# Exercício 5: Escreva um programa que peça ao usuário para digitar um número e determine se ele é um número primo (divisível apenas por 1 e por ele mesmo).


def ColetaNumero():
    numero_inserido = input("Digite um número aqui: ")
    numero_inserido = int(numero_inserido)
    if numero_inserido % 1 and numero_inserido % numero_inserido:
        print("Número primo.")
    else:
        print("Não é um número primo.")


ColetaNumero()
