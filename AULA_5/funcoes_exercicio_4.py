# Fatorial: Crie uma função que calcule o fatorial de um número.

def ColetaNumero():
    while True:
        numero_fornecido = input("Digite um número aqui: ")
        if numero_fornecido.isnumeric() and int(numero_fornecido) > 0:
            return int(numero_fornecido)
        else:
            print("Por favor, digite um número inteiro maior que zero.")

def CalculaFatorial(numero_inserido_pelo_usuario):
    resultado = 1
    for i in range(1, numero_inserido_pelo_usuario + 1):
        resultado *= i
    return resultado

numero_fornecido = ColetaNumero()
resultado_fatorial = CalculaFatorial(numero_fornecido)
print(f'O fatorial de {numero_fornecido} é {resultado_fatorial}')
