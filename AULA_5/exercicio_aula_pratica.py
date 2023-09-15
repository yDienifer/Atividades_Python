usuario_correto = "juao"
senha_correta = "1234"


def PedeCrecidenciais():
    nome_de_usuario = input("Digite o nome de usuário: ")
    senha_do_usuario = input("Digite a senha do usuário: ")

    def FazLogin(nome, senha):
        if nome == usuario_correto and senha == senha_correta:
            print(f"O login foi feito pelo {nome} com a senha {senha}")
        else:
            while nome != usuario_correto and senha != senha_correta:
                print("Usuário ou senha incorreto. Tente novamente")
                PedeCrecidenciais()
                break

    FazLogin(nome_de_usuario, senha_do_usuario)


PedeCrecidenciais()
