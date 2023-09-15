# Crie um programa que peça ao usuário para digitar um número e, em seguida, determine se ele é positivo, negativo ou zero.


def ColetaNumero():
    while True:
        numero_fornecido = input("Digite um número aqui: ")
        if numero_fornecido[0] == "-":
            print("Número negativo")
            break

        if numero_fornecido.isnumeric():
            if int(numero_fornecido) == 0:
                print("Número zero!")
                break

            elif int(numero_fornecido) > 0:
                print("Número positivo!")
                break

        else:
            print("Número inválido!")


ColetaNumero()
