# Exercício 1: Escreva um programa que peça ao usuário para digitar sua idade e, em seguida, determine se a pessoa é maior de idade (18 anos ou mais) ou menor de idade (menos de 18 anos).


def ColetaIdade():
    while True:
        idade_fornecida = input("Digite a sua idade aqui: ")

        if idade_fornecida.isnumeric():
            idade_fornecida = int(idade_fornecida)
            break
        else:
            print("A idade Inválida! Tente novamente.")

    return idade_fornecida


idade_fornecida = ColetaIdade()


def VerificaIdade(idade):
    if idade >= 18:
        print("É maior de idade!")
    else:
        print("É menor de idade!")


VerificaIdade(idade_fornecida)
