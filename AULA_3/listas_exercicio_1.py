# Exercício 1: Manipulação de Listas

# a) Crie uma lista chamada numeros contendo os números de 1 a 10.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# b) Adicione o número 11 ao final da lista.
numeros.append(11)

# c) Insira o número 0 no início da lista.
numeros.insert(0, 0)

# d) Remova o número 5 da lista.
numeros.remove(5)

# e) Ordene a lista em ordem crescente.
numeros.sort()

# f) Crie uma cópia da lista ordenada e inverta a ordem dos elementos nessa cópia.
numeros_invertidos = numeros.copy()
numeros_invertidos.reverse()

print(numeros)
print(numeros_invertidos)