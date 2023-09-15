# Exercício 7: Crie um programa que determine se um ano é bissexto. O programa deve pedir ao usuário para inserir um ano e, em seguida, informar se ele é bissexto ou não.

# O número deve atender aos seguintes critérios:
# Ser divisível por 4.
# NÃO ser divisível por 100.
# Ser divisível por 400.


def ColetaAnoFornecido():
    ano_fornecido = input("Digite o número aqui: ")

    if ano_fornecido.isnumeric:
        ano_fornecido = int(ano_fornecido)
        return ano_fornecido
    else:
        print("Não é um número válido!")


def DeterminaAnoBissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("É bissexto!")
    else:
        print("Não é bissexto!")


ano_fornecido = ColetaAnoFornecido()
DeterminaAnoBissexto(ano_fornecido)
