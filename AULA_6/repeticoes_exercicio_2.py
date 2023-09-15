# Exercício 3: Escreva um programa que calcule a soma de todos os números ímpares de 1 a 100.

resultado_da_soma = 0

for numero in range(1, 101):
    if numero % 2 != 0:
        resultado_da_soma += numero

print("A soma dos números ímpares de 1 a 100 é:", resultado_da_soma)
