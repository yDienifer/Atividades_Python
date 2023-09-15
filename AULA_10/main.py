import re
import requests

# Códigos de cores ANSI
ROXO = "\033[0;35m"
VERDE = "\033[0;32m"
VERMELHO = "\033[0;31m"
TREME = "\033[5m"
BRANCO_CLARO = "\033[1;37m"

def ObterURLAlvo():
    while True:
        url_alvo = input("Qual a URL site você deseja escanear?: ")

        padrao = r"https?://[a-zA-Z0-9.-]+"
        teste = re.match(padrao, url_alvo)

        if teste and requests.get(url_alvo):
            break

        elif not url_alvo.startswith("http://"):
            try:
                url_alvo = "http://" + url_alvo
                requests.get(url_alvo)
                break
            except:
                pass

        elif not url_alvo.startswith("https://"):
            try:
                url_alvo = "https://" + url_alvo
                requests.get(url_alvo)
                break
            except:
                pass

        else:
            print("Este site não existe.")

url_alvo = ObterURLAlvo()

def EscanearSubdominios(url):
    with open("arquivo.txt") as arquivo:
        for palavra in arquivo:
            if not url.endswith("/"):
                url = url + "/"

                if (
                    requests.get(url + palavra).status_code >= 200
                    and requests.get(url + palavra).status_code < 300
                ):
                    print(f"{VERDE} Site disponível | {BRANCO_CLARO}{url}")

                elif requests.get(url + palavra).status_code == 402:
                    print(f"{TREME} Acesso não autorizado | {BRANCO_CLARO}{url}")

                elif requests.get(url + palavra).status_code == 403:
                    print(f"{TREME} Acesso proibido | {BRANCO_CLARO}{url}")

                elif requests.get(url + palavra).status_code == 403:
                    pass

                elif requests.get(url + palavra).status_code == 405:
                    print(f"{TREME} Método HTTP não permitido | {BRANCO_CLARO}{url}")

                elif (
                    requests.get(url + palavra).status_code >= 500
                    and requests.get(url + palavra).status_code < 600
                ):
                    print(f"{TREME} Erro de servidor | {BRANCO_CLARO}{url}")

            else:
                pass
