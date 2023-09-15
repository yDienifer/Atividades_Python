# Contagem de Vogais: Crie uma função que conte o número de vogais em uma string.

from colorama import Fore, init

init()


def RecebeString():
    while True:
        string_inserida = input(Fore.WHITE + "Digite a sua string aqui: ")

        if string_inserida.isalpha():
            print(Fore.LIGHTBLUE_EX + f"Verificando a string '{string_inserida}'")
            return string_inserida
        else:
            print(Fore.RED + "Tá querendo me trollar ou você nunca foi pra escola?")


def ContaAsVogais(string_a_ser_avaliada):
    quantidade_da_vogal_a = string_a_ser_avaliada.lower().count("a")
    quantidade_da_vogal_e = string_a_ser_avaliada.lower().count("e")
    quantidade_da_vogal_i = string_a_ser_avaliada.lower().count("i")
    quantidade_da_vogal_o = string_a_ser_avaliada.lower().count("o")
    quantidade_da_vogal_u = string_a_ser_avaliada.lower().count("u")

    print(
        Fore.LIGHTGREEN_EX
        + f"Na string inserida, foi encontrado A: {quantidade_da_vogal_a}, E: {quantidade_da_vogal_e}, I: {quantidade_da_vogal_i}, O: {quantidade_da_vogal_o}, U: {quantidade_da_vogal_u}"
    )


string_inserida = RecebeString()
ContaAsVogais(string_inserida)
