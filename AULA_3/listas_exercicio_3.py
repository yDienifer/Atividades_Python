# Exercício 3: Iteração e Operações

# a) Crie uma lista de nomes de frutas (frutas) contendo pelo menos 5 frutas diferentes.
frutas = ["Abacate", "Abacaxi", "Açai", "Acerola", "Amora", "Banana"]

# b) Usando um loop for, imprima cada nome de fruta em uma linha.
for fruta in frutas:
    print(fruta)

# c) Crie uma lista chamada frutas_maiusculas contendo as frutas em letras maiúsculas.
frutas_minusculas = [fruta.upper() for fruta in frutas]
print(frutas_minusculas)

# d) Crie uma lista chamada frutas_tamanho contendo o tamanho de cada nome de fruta na lista original.
frutas_tamanho = [len(fruta) for fruta in frutas]
print(frutas_tamanho)
