# Exercício 1: Manipulação de Dicionários

# a) Crie um dicionário chamado usuarios com informações sobre três usuários: nome, idade e cargo.
usuarios = {
    "Yuri": {"idade": 18, "cargo": "Programador"},
    "João": {"idade": 15, "cargo": "Estudante"},
    "Ana": {"idade": 24, "cargo": "Pintora"},
}

# b) Adicione um quarto usuário ao dicionário.
usuarios["Carlos"] = {"idade": 18, "cargo": "Analista de Segurança"}

# c) Modifique a idade de um dos usuários existentes.
usuarios["João"]["idade"] = 22

# d) Remova um dos usuários do dicionário.
del usuarios["Carlos"]

# e) Imprima o número total de usuários no dicionário.
total_de_usuarios = len(usuarios)
print(f"O dict conta atualmente com: {total_de_usuarios} usuários!")
print(usuarios)