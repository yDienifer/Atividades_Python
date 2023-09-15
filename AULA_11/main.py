# api: https://pokeapi.co/api/v2/pokemon/ditto

import requests
import json

YELLOW = "\033[1;33m"
LIGHT_WHITE = "\033[1;37m"


def MostraLogoDoPrograma():
    try:
        with open("art.txt") as arquivo:
            arte_ascii = arquivo.read()
            print(arte_ascii)
    except FileNotFoundError:
        print("Arquivo de arte ASCII não encontrado.")


MostraLogoDoPrograma()

pokemon_escolhido = input(
    f"{YELLOW}[⚡] {LIGHT_WHITE}Qual pokemon você quer visualizar as habilidades?: "
)

try:
    requisicao = json.loads(
        requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{pokemon_escolhido.lower()}"
        ).text
    )
    abilities = requisicao["abilities"]
    second_ability = print(
        "O nome da habilidade de "
        + pokemon_escolhido
        + f" é: {YELLOW}"
        + abilities[1]["ability"]["name"]
    )
except:
    print("Nome incorreto ou pokemon inexistente")
