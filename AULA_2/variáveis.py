# dict
individuo = {"nome": "Ana", "idade": 15}
print(individuo)

# lendo a variável

# perguntando_uma_cor_de_led_para_o_usuário = input("Que cor de led você quer, meu nobre? ")

#cor_de_led_escolhida_pelo_usuário = print("A cor escolhida foi: " + perguntando_uma_cor_de_led_para_o_usuário + ". Cor ativada com sucesso!")

# Atividade: Faça uma mini calculadora em Python

# Mensagem apresentando o programa
print("Seja bem-vindo à Mini Calculadora em Python. Aqui, é possível verificar o resultado da divisão inteira de dois números de sua escolha.")

# Pegando os dois números ditos pelo usuário
primeiro_numero = input("Por favor, digite o primeiro número: ")
segundo_numero = input("Agora digite o segundo número: ")

# Calculando o resto da divisão das dois números
resultado_do_resto_da_divisão = int(primeiro_numero) % int(segundo_numero)

# Imprimindo uma mensagem que diz o resultado do resto da divisão
imprimindo_resultado = print(f"O resto da divisão de {primeiro_numero} e {segundo_numero} é: {str(resultado_do_resto_da_divisão)}")