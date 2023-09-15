# Exercício 2: Compreensões de Lista

# a) Crie uma lista chamada quadrados contendo os quadrados dos números de 1 a 10 usando uma compreensão de lista.
quadrados = [numero**2 for numero in range(1, 11)]  # x ** 2 = x²
print(quadrados)

# b) Crie uma lista chamada numeros_pares contendo apenas os números pares de 1 a 20 usando uma compreensão de lista.
numeros_pares = [numero for numero in range(1, 21) if numero % 2 == 0]

print(numeros_pares)

# c) Crie uma lista chamada cubos contendo os cubos dos números ímpares de 1 a 15 usando uma compreensão de lista.
cubos = [numero for numero in range(1, 16) if numero % 2 == 1]
print(cubos)