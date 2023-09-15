# Escreva um programa que peça ao usuário para digitar uma nota de 0 a 100 e, em seguida, imprima a seguinte mensagem de acordo com a nota:

# 90-100: "A - Excelente"
# 80-89: "B - Bom"
# 70-79: "C - Regular"
# 60-69: "D - Insuficiente"
# Menos de 60: "F - Reprovado"

import time
from colorama import Fore, init

init()


def ColetaInformacoesDosAlunos():
    alunos_fornecidos = {}

    print(
        Fore.WHITE
        + f"Seja bem-vindo(a) ao nosso gerador de boletim digital. Aqui, você pode otimizar o processo de cálculo de notas e frequência, com resultados automatizados. O nosso sistema de notas opera da seguinte maneira:"
    )

    time.sleep(7)
    print(
        Fore.GREEN
        + "90-100: 'A - Excelente', "
        + Fore.CYAN
        + "80-89: 'B - Bom', "
        + Fore.YELLOW
        + "70-79: 'C - Regular', "
        + Fore.RED
        + "60-69: 'D - Insuficiente', "
        + Fore.LIGHTRED_EX
        + "Menos de 60: 'F - Reprovado'"
    )

    time.sleep(6)
    print(Fore.WHITE + "Antes de iniciar, por gentileza, leia atentamente as regras: ")

    time.sleep(3)
    print(
        Fore.WHITE
        + "1 | É necessário inserir o nome completo do aluno, excluindo quaisquer caracteres numéricos."
    )

    time.sleep(3)
    print(
        Fore.WHITE
        + "2 | A frequência deve estar no formato 'x%', sendo 'x' um número do tipo."
    )

    time.sleep(3)
    print(Fore.WHITE + "3 | A nota deve situar-se no intervalo de 0 a 100.")

    time.sleep(2)
    print(
        Fore.CYAN
        + "Por favor, obedeça às regras para alcançar o resultado desejado! :)"
    )

    while True:
        nome_aluno = input(
            Fore.WHITE + "Insira o nome completo do aluno neste espaço designado: "
        )

        palavras_no_nome = nome_aluno.split()

        if len(palavras_no_nome) >= 2 and all(
            palavra.isalpha() for palavra in palavras_no_nome
        ):
            if nome_aluno not in alunos_fornecidos:
                frequencia_aluno = input(
                    Fore.WHITE
                    + "Informe a frequência de "
                    + Fore.CYAN
                    + f"{nome_aluno}: "
                )

                if frequencia_aluno.endswith("%") and frequencia_aluno[:-1].isdigit():
                    nota_aluno = input(
                        Fore.WHITE
                        + f"Insira a nota de "
                        + Fore.CYAN
                        + f"{nome_aluno}"
                        + Fore.WHITE
                        + " aqui: "
                    )

                    if nota_aluno.isnumeric() and 0 <= int(nota_aluno) <= 100:
                        alunos_fornecidos[nome_aluno] = {
                            "nome_completo": nome_aluno,
                            "nota": int(nota_aluno),
                            "frequencia": frequencia_aluno,
                        }

                        while True:
                            resposta_usuario = input(
                                Fore.GREEN
                                + "Adicionado à lista. Deseja incluir outro aluno? (Digite 'sim' ou 'não'): "
                            ).lower()

                            if resposta_usuario == "sim":
                                print(
                                    Fore.CYAN
                                    + f"Lista atual de alunos: {alunos_fornecidos.items()}"
                                )
                                break
                            elif resposta_usuario == "não":
                                print(Fore.CYAN + f"Verificando... {alunos_fornecidos}")
                                return alunos_fornecidos
                            else:
                                print(
                                    Fore.RED
                                    + "Inserido na lista. Por gentileza, informe 'sim' ou 'não'."
                                )
                    else:
                        print(
                            Fore.RED
                            + "A nota mínima é de 0, enquanto a nota máxima atinge 100. Por favor, tente novamente."
                        )
                else:
                    print(
                        Fore.RED
                        + "Por gentileza, adote o padrão de apresentação da frequência no formato 'x%'."
                    )
            else:
                print(
                    Fore.RED
                    + f"O(A) aluno(a) {nome_aluno} já consta na lista. Por favor, insira um nome diferente."
                )
        else:
            print(
                Fore.RED
                + "Por gentileza, insira o nome e o sobrenome do discente, utilizando exclusivamente caracteres alfabéticos neste procedimento."
            )


alunos_fornecidos = ColetaInformacoesDosAlunos()


def AvaliaAlunos(alunos_a_serem_avaliados):
    for nome_aluno, dados_aluno in alunos_a_serem_avaliados.items():
        nome_completo = dados_aluno["nome_completo"]
        nota = dados_aluno["nota"]
        frequencia = int(dados_aluno["frequencia"].rstrip("%"))

        if frequencia <= 70:
            resultado = Fore.RED + "Reprovado(a) por excesso de faltas"
        else:
            if nota >= 90:
                resultado = Fore.GREEN + "A - Excelente!"
            elif nota >= 80:
                resultado = Fore.CYAN + "B - Bom"
            elif nota >= 70:
                resultado = Fore.YELLOW + "C - Regular"
            elif nota >= 60:
                resultado = Fore.RED + "D - Insuficiente"
            else:
                resultado = Fore.LIGHTRED_EX + "F - Reprovado"

        print(
            Fore.WHITE
            + f"Nome: {nome_completo}, Nota: {nota}, Frequência: {frequencia}%, Resultado Final: {resultado}"
        )


AvaliaAlunos(alunos_fornecidos)
