# Dado o dicionário notas com as notas dos alunos em uma turma, escreva um programa que calcule a média das notas.

alunos = {"Ana": 8.5, "Yuri": 10, "Júlia": 7, "Kauã": 2, "Lucas": 0, "João": 7}


def calculando_media_dos_alunos():
    soma_das_notas = sum(alunos.values())
    quantidade_de_alunos = len(alunos)
    return soma_das_notas / quantidade_de_alunos


media = calculando_media_dos_alunos()
print(f"A média das notas é de: {media}")
