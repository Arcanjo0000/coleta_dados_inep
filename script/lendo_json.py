import json


def ler_caminhos():
    with open("informacoes\\caminho_tabelas.json", "r") as arquivo:
        caminhos = json.load(arquivo)
        return caminhos

def ler_estrutura():
    with open("informacoes\\estrutura_tabela.json", "r") as arquivo:
        estrutura = json.load(arquivo)
        return estrutura
