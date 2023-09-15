# Crie um dicionário chamado agenda que armazene informações de contato (nome, telefone, e-mail) de algumas pessoas. Em seguida, permita que o usuário adicione uma nova pessoa à agenda.

agenda = {
    "Ana": {
        "nome": "Alice",
        "telefone": "123-456-7890",
        "e-mail": "example1@gmail.com",
    },
    "Júlia": {
        "nome": "Júlia",
        "telefone": "123-456-7890",
        "e-mail": "example2@gmail.com",
    },
    "João": {
        "nome": "João",
        "telefone": "123-456-7890",
        "e-mail": "example3@gmail.com",
    },
}


def adicionar_novo_contato():
    while True:
        adicionar = input(
            "Deseja adicionar mais uma pessoa na agenda (Digite 'sim' ou 'não')? "
        )

        if adicionar.lower() == "sim":
            adicionar_novo_nome = input("Adicione o nome da nova pessoa: ")

            if adicionar_novo_nome in agenda:
                print("Essa pessoa já está na agenda. Use um nome diferente.")
            else:
                adicionar_novo_telefone = input("Agora, o telefone: ")
                adicionar_novo_email = input("Por último, adicione o e-mail: ")

                agenda[adicionar_novo_nome] = {
                    "nome": adicionar_novo_nome,
                    "telefone": adicionar_novo_telefone,
                    "e-mail": adicionar_novo_email,
                }

        elif adicionar == "não":
            print(f"Sendo assim, a sua agenda é essa: {agenda}")
            break

        else:
            print("Por favor, responda com 'sim' ou 'não'.")


adicionar_novo_contato()
