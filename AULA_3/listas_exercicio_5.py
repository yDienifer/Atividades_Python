# Exercício 5: Fatiamento e Sublistas

# a) Crie uma lista chamada numeros contendo os números de 1 a 20.
numeros = list(range(1, 21))
print(numeros)

# b) Use fatiamento para criar uma nova lista chamada primeira_metade contendo os primeiros 10 números.
primeira_metade = numeros[0:10]
print(primeira_metade)

# c) Use fatiamento para criar uma nova lista chamada segunda_metade contendo os últimos 10 números.
segunda_metade = numeros[9:20]
print(segunda_metade)

# d) Use fatiamento para criar uma nova lista chamada pares contendo os números pares da lista original.
numeros_pares = [numero for numero in numeros if numero % 2 == 0]
print(numeros_pares)