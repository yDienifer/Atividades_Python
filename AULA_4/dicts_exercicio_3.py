# Crie um dicionário chamado estoque com alguns itens e suas quantidades em estoque. Em seguida, escreva um programa que calcule o total de itens em estoque.

# Dicionário de estoque de livros
estoque_de_livros = {
    "Torto arado (Itamar Vieira Junior)": 200,
    "O poder da cura (Padre Reginaldo Manzotti)": 150,
    "Histórias lindas de morrer (Ana Cláudia Quintana Arantes)": 300,
    "A hora da estrela – Edição comemorativa (Clarice Lispector)": 250,
    "A raiva não educa. A calma educa (Maya Eigenmann)": 100,
}

# Calcular o total de itens em estoque
total_itens_em_estoque = sum(estoque_de_livros.values())

# O sum é uma função embutida do Python que é usada para calcular a soma de elementos em uma sequência, como uma lista, tupla ou dicionário. Neste contexto específico, estamos usando o sum para calcular a soma das quantidades de itens em estoque, que são os valores do dicionário estoque_de_livros.

# Imprimir o resultado
print(f"O total de itens em estoque é: {total_itens_em_estoque}")