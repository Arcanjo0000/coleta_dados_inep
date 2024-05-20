import os
import pandas as pd


def pegando_arquivos_com_dados():
    
    arquivos_com_dados = os.listdir("informacoes/data")
    for ano in range(2022, 2008, -1):
        for arquivo in arquivos_com_dados:
            estrutura_antiga = ano < 2021
            estrutura_nova = ano >+ 2021
            if str(arquivo) in str(ano):
                if estrutura_antiga:
                    caminho_arquivo = os.path.join("informacoes/data", arquivo)
                    with open(str(caminho_arquivo), "r") as file:
                        dados_do_arquivo = []
                        for linha in file:
                            linha_limpa = linha.strip()
                            dados_do_arquivo.append(linha_limpa)
                        tratar_dados_antigos(dados_do_arquivo)
                elif estrutura_nova:
                    caminho_arquivo = os.path.join("informacoes/data", arquivo)
                    with open(str(caminho_arquivo), "r") as file:
                        dados_do_arquivo = []
                        for linha in file:
                            linha_limpa = linha.strip()
                            dados_do_arquivo.append(linha_limpa)
                        tratar_dados_novos(dados_do_arquivo)
            

def tratar_dados_antigos(lista_de_dados):
    lista_com_dados_tratados = []
    for idx, dado in enumerate(lista_de_dados):
        if idx % 2 == 0:
            total = lista_de_dados[idx-1]
            total_privada = lista_de_dados[idx]
            total_publica = total - total_privada
            lista_com_dados_tratados.extend([total_publica, total_privada])
    adicionar_na_tabela(lista_com_dados_tratados)

def tratar_dados_novos(lista_de_dados):
    lista_com_dados_tratados = []



def criar_tabela():
    dados = {}
    df = pd.DataFrame(dados)
    df.to_excel("dados_tratados.xlsx", index=False)


def adicionar_na_tabela(dados_tratados):
    tabela_existente = pd.read_excel("informacoes/data/dados_tratados.xlsx")
    nova_linha = {}
    df_novo = pd.DataFrame(nova_linha)
    df_atualizado = pd.concat([tabela_existente, df_novo], ignore_index=True)

    df_atualizado.to_excel("informacoes/data/dados_tratados.xlsx")




            
            



