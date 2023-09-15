# Exercício 2: Escreva um programa que peça ao usuário um número e imprima a tabuada desse número de 1 a 10.

from colorama import Fore, init

init()


def ColetaNumeroFornecido():
    numero_inserido = input(Fore.WHITE + "Insira um número: ")
    if numero_inserido.isnumeric() == False:
        print(Fore.RED + "Por favor, insira apenas números.")
        numero_inserido = ColetaNumeroFornecido()
    else:
        return numero_inserido


numer_inserido = ColetaNumeroFornecido()


def FazTabuadaDoNumero(numero):
    multiplicador = 1

    while multiplicador <= 10:
        resultado = int(numero) * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")
        multiplicador += 1


FazTabuadaDoNumero(numer_inserido)
