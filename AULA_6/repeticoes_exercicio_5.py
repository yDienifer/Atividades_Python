# Exercício 6: Escreva um programa que peça ao usuário para digitar uma série de números positivos e, em seguida, calcule e imprima a média desses números. O programa deve continuar pedindo números até que o usuário digite um número negativo.

from colorama import Fore, init

init()


def ColetaNumeros():
    lista_de_numeros_fornecidos = []

    while True:
        numero_positivo = input(
            Fore.WHITE
            + "Digite um número positivo aqui (ou digite um número negativo para sair): "
        )

        if numero_positivo.isalpha() == False:
            numero_positivo = int(numero_positivo)
            if numero_positivo >= 0 or numero_positivo == 0:
                lista_de_numeros_fornecidos.append(numero_positivo)
                print(Fore.GREEN + f"Números na lista: {lista_de_numeros_fornecidos}")

            elif numero_positivo <= -1 or numero_positivo == -1:
                print(
                    Fore.MAGENTA
                    + "Você interrompeu o programa. Estamos verificando os números fornecidos até o momento e calculando a média..."
                )
                break

        else:
            print(Fore.RED + "Número inválido")

    return lista_de_numeros_fornecidos


def CalculaMediaDosNumeros(lista_com_os_numeros):
    resultado_do_calculo = sum(lista_com_os_numeros) / len(lista_com_os_numeros)
    print(f"> A média dos números fornecidos é: {resultado_do_calculo}")


lista_de_numeros_fornecidos = ColetaNumeros()
CalculaMediaDosNumeros(lista_de_numeros_fornecidos)
