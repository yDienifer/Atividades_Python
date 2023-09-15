# Calculadora Simples: Crie uma função que realize operações simples de matemática, como adição, subtração, multiplicação e divisão. A função deve receber dois números e um operador como argumentos.

from colorama import Fore, init

init()

def ColetaNumerosParaCalculo():
    while True:
        try:
            primeiro_numero_fornecido = float(input(Fore.WHITE + "Digite um número: "))
            segundo_numero_fornecido = float(input(Fore.WHITE + "Digite o segundo número: "))
            return primeiro_numero_fornecido, segundo_numero_fornecido
        except ValueError:
            print(Fore.RED + "Número inválido. Tente novamente.")


def ColetaOperadorParaCalcular():
    while True:
        operador = input(
            Fore.CYAN
            + "Digite o operador (adição, subtração, multiplicação ou divisão): "
        ).lower()
        if operador in ("adição", "subtração", "multiplicação", "divisão"):
            return operador
        else:
            print(Fore.RED + "Operador inválido. Tente novamente.")


def CalculandoValores(PrimeiroNumero, SegundoNumero, Operador):
    if Operador == "adição":
        resultado = PrimeiroNumero + SegundoNumero
        print(
            Fore.LIGHTGREEN_EX
            + f"O resultado da soma de {PrimeiroNumero} + {SegundoNumero} é: {resultado}"
        )
    elif Operador == "subtração":
        resultado = PrimeiroNumero - SegundoNumero
        print(
            Fore.LIGHTGREEN_EX
            + f"O resultado da subtração de {PrimeiroNumero} - {SegundoNumero} é: {resultado}"
        )
    elif Operador == "multiplicação":
        resultado = PrimeiroNumero * SegundoNumero
        print(
            Fore.LIGHTGREEN_EX
            + f"O resultado da multiplicação de {PrimeiroNumero} x {SegundoNumero} é: {resultado}"
        )
    elif Operador == "divisão":
        if SegundoNumero == 0:
            print(
                Fore.RED + "Erro: Não é possível fazer divisão com divisor de valor 0."
            )
        else:
            resultado = PrimeiroNumero / SegundoNumero
            print(
                Fore.LIGHTGREEN_EX
                + f"O resultado da divisão de {PrimeiroNumero} / {SegundoNumero} é: {resultado}"
            )


# Solicitar números e operador do usuário
primeiro_numero, segundo_numero = ColetaNumerosParaCalculo()
operador = ColetaOperadorParaCalcular()

# Realizar o cálculo
CalculandoValores(primeiro_numero, segundo_numero, operador)
