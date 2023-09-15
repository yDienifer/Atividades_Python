import re
import requests
from colorama import Fore, init

init()


def ObterURLDoAlvo():
    while True:
        url_alvo = input("Qual a URL site você deseja escanear?: ")
        padrao = r"https?://[a-zA-Z0-9.-]+"
        corresponde = re.match(padrao, url_alvo)

        if corresponde and requests.get(url_alvo):
            break
        elif not url_alvo.startswith("http://"):
            try:
                url_alvo = "http://" + url_alvo
                requisicao = requests.get(url_alvo)
                requisicao.raise_for_status()  # Gera uma exceção para solicitações ruins
                break
            except:
                pass

        elif not url_alvo.startswith("https://"):
            try:
                url_alvo = "https://" + url_alvo
                requisicao = requests.get(url_alvo)
                requisicao.raise_for_status()
                break
            except:
                pass

        else:
            print("Algo deu errado")

    return url_alvo


url_alvo = ObterURLDoAlvo()


def ProcurarDiretorios(url):
    with open("arquivo.txt") as arquivo:
        for palavra in arquivo:

            if not url.endswith("/"):
                alvo = f"{url}/{palavra.strip()}"  # strip = remove espaços em branco

                if (
                    requests.get(alvo).status_code >= 200
                    and requests.get(alvo).status_code < 300
                ):
                    print(Fore.LIGHTGREEN_EX + f"O diretório {alvo} existe!")

                elif requests.get(alvo).status_code == 400:
                    print(Fore.LIGHTRED_EX + f"O diretório {alvo} deu bad request!")

                elif requests.get(alvo).status_code == 401:
                    print(
                        Fore.LIGHTRED_EX
                        + f"O diretório {alvo} deu acesso não autorizado!"
                    )

                elif requests.get(alvo).status_code == 403:
                    print(
                        Fore.LIGHTYELLOW_EX + f"O diretório {alvo} deu acesso negado!"
                    )

                elif requests.get(alvo).status_code == 404:
                    print(Fore.LIGHTRED_EX + f"O diretório {alvo} não existe!")

                elif requests.get(alvo).status_code == 409:
                    print(Fore.LIGHTRED_EX + f"O diretório {alvo} deu conflito!")

                elif (
                    requests.get(alvo).status_code >= 500
                    and requests.get(alvo).status_code < 600
                ):
                    print(Fore.LIGHTRED_EX + f"Erro no servidor do {alvo}")

                else:
                    print(Fore.LIGHTRED_EX + f"Erro no servidor: {alvo}")

            else:
                alvo = url


ProcurarDiretorios(url_alvo)
