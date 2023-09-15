# Verificação de Palíndromo: Crie uma função que verifique se uma string é um palíndromo (ou seja, ela é igual se lida da esquerda para a direita e da direita para a esquerda, como "radar" ou "arara").

from colorama import Fore, init

init()

print(
    Fore.YELLOW
    + "Bem vindo ao nosso verificador de Palíndromo. Aqui você pode descobrir se uma palavra é ou não um palíndromo."
)


def ColetaPalavraFornecida():
    palavra_recebida = input(
        Fore.WHITE + "Por favor, digite a palavra que você deseja verificar aqui: "
    )
    if " " in palavra_recebida:
        print(
            Fore.RED
            + "Então quer dizer que você está tentando quebrar a lógica aqui, meu caro? Pois bem, volte duas casas."
        )
        palavra_recebida = ColetaPalavraFornecida()
    return palavra_recebida


def VerificaUmPalindromo(palavra):
    while True:
        palavra_padronizada = palavra.lower()
        palavra_invertida = palavra_padronizada[::-1]

        if palavra_invertida == palavra_padronizada:
            resultado_da_verificacao = input(
                Fore.GREEN
                + f"A palavra {palavra} é um palíndromo. Deseja tentar novamente?: "
            ).lower()
            if resultado_da_verificacao == "sim":
                palavra = ColetaPalavraFornecida()  # Atualiza a palavra
            elif resultado_da_verificacao == "não":
                print("Tchau!")
                break
            else:
                input("Por favor, digite 'sim' ou 'não'.")
                break

        else:
            resultado_da_verificacao = input(
                Fore.RED
                + f"A palavra {palavra} não é um palíndromo. Deseja tentar novamente?: "
            ).lower()

            if resultado_da_verificacao == "sim":
                palavra = ColetaPalavraFornecida()  # Atualiza a palavra
            elif resultado_da_verificacao == "não":
                print("Tchau!")
                break
            else:
                input("Por favor, digite 'sim' ou 'não'.")
                break


palavraJuao = ColetaPalavraFornecida()
VerificaUmPalindromo(palavraJuao)
