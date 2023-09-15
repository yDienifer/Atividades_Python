# Exercício 2: Iteração e Análise de Dicionários

# a) Crie um dicionário com nomes de frutas como chaves e suas quantidades como valores.
frutas = {"Banana": 9, "Maça": 14, "Açai": 12}

# b) Use um loop for para imprimir cada nome de fruta e sua quantidade.
for fruta, quantidade in frutas.items():
    print(f"{fruta}: {quantidade}")

# c) Calcule a quantidade total de frutas no dicionário.
print(len(frutas))

# d) Crie uma lista contendo as frutas que têm uma quantidade maior que 10.
frutas_com_mais_de_10_quantidades = [fruta for fruta, quantidade in frutas.items() if quantidade > 10]

print(frutas_com_mais_de_10_quantidades)