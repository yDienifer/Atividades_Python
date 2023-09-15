# Exercício 5: Escreva um programa que gere os primeiros 20 números da sequência de Fibonacci.

# f0 = 0
# f1 = 1


def formandoOs20NumerosDeFibonacci():
    f0 = 0
    f1 = 1
    contador = 0

    while contador <= 20:
        print(f0)  # Imprime o número atual da sequência
        f0, f1 = f1, f0 + f1  # Atualiza f0 e f1 para os próximos números da sequência
        contador += 1


formandoOs20NumerosDeFibonacci()
