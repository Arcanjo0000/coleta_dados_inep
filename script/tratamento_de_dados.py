import os
import pandas as pd
from itertools import islice
import more_itertools as mit

def pegando_arquivos_com_dados():
    #lista com os arquivo
    arquivos_com_dados = os.listdir("informacoes/data")

    for arquivo in arquivos_com_dados:
        ano = "".join(filter(str.isdigit, arquivo))
        ano = int(ano)
        estrutura_antiga = ano < 2021
        estrutura_nova = ano >= 2021
        estrutura_bem_antiga = ano == 2009
        
        caminho_arquivo = os.path.join("informacoes/data", arquivo)
        #abre os arquivos
        dados_do_arquivo = lendo_arquivo(caminho_arquivo)

        dados_transformados = tranformando_dados(dados_do_arquivo)


        if estrutura_nova:
            separando_modalidades_novo(dados_transformados, ano)
            

def tranformando_dados(dados_do_arquivo):
    lista_com_dados_como_numero = []
    for idx, dado_list in enumerate(dados_do_arquivo):
        dado_str = dado_list[0]
        dado_int = int(dado_str.replace(".",""))
        lista_com_dados_como_numero.append(dado_int)
    return lista_com_dados_como_numero

def lendo_arquivo(caminho_arquivo):
    with open(str(caminho_arquivo), "r") as file:
            dados_do_arquivo = []
            for linha in file:
                linha_limpa = linha.split()
                #tira os espaços das linhas
                if linha_limpa:
                    dados_do_arquivo.append(linha_limpa)
            return dados_do_arquivo

def separando_modalidades_novo(lista_com_dados_int, ano):
    print()
    print(f"ano = {ano}")
    struct = 0
    iterador = iter(lista_com_dados_int)
    presencial = list(islice(iterador, 84))
    ead = list(iterador)
    # pegar o presencial e dar um jeito de separar os cursos
    cursos_presenciais = mit.chunked(presencial, 21)
    #o idx é o código do curso
    # presenciais
    for idx, curso in enumerate(cursos_presenciais):
        modalidade = "presencial"
        match idx:
            case 0:
                codigo_curso = idx
                separando_tipos_de_dados(curso, codigo_curso, ano, struct, modalidade)
            case 1:
                codigo_curso = idx
                separando_tipos_de_dados(curso, codigo_curso, ano, struct, modalidade)
            case 2:
                codigo_curso = idx
                separando_tipos_de_dados(curso, codigo_curso, ano, struct, modalidade)
            case 3:
                codigo_curso = idx
                separando_tipos_de_dados(curso, codigo_curso, ano, struct, modalidade)
            case _ :
                print("erro ao tentar separar os cursos presenciais")
    
    cursos_ead = mit.chunked(ead, 21)
    for idx, curso in enumerate(cursos_ead):
        modalidade = "EAD"
        match idx:
            case 0:
                codigo_curso = idx
                separando_tipos_de_dados(curso, codigo_curso, ano, struct, modalidade)
            case 1:
                codigo_curso = idx
                separando_tipos_de_dados(curso, codigo_curso, ano, struct, modalidade)
            case 2:
                codigo_curso = idx
                separando_tipos_de_dados(curso, codigo_curso, ano, struct, modalidade)
            case 3:
                codigo_curso = idx
                separando_tipos_de_dados(curso, codigo_curso, ano, struct, modalidade)
            case _ :
                print("erro ao tentar separar os cursos EAD")


def separando_tipos_de_dados(dados_do_curso, codigo_curso, ano, struct, modalidade):
    if struct == 0:

        dados_separados = mit.chunked(dados_do_curso, 7)
        print()
        print(modalidade)
        print(f"curso = {codigo_curso}")
        for qual_dado, dados in enumerate(dados_separados):
            match qual_dado:
                case 0:
                    tipo_dado = "cursos"
                    tratar_dados_novos(tipo_dado, dados, ano, codigo_curso, modalidade)
                case 1:
                    tipo_dado = "matriculas"
                    tratar_dados_novos(tipo_dado, dados, ano, codigo_curso, modalidade)
                case 2:
                    tipo_dado = "concluintes"
                    tratar_dados_novos(tipo_dado, dados, ano, codigo_curso, modalidade)
                case _:
                    print("erro ao separar os tipos de dados")

def tratar_dados_novos(tipo_dado, dados, ano, codigo_curso, modalidade):
    print()
    print(f"tipo de dado = {tipo_dado}")
    publica = []
    privada = []

    for idx, dado in enumerate(dados):
        posicao = idx + 1

        if posicao % 2 == 0:
            total = dados[idx - 1]
            total_privada = dado
            total_publica = total - total_privada
            publica.append(total_publica)
            privada.append(total_privada)
        elif posicao % 7 == 0:
            publica.append(dado)
    soma_publica = sum(privada)
    soma_privada = sum(publica)
    print(f"privada = {soma_privada}")
    print(f"publica = {soma_publica}")




def criar_tabela():
    dados = {}
    df = pd.DataFrame(dados)
    #df.to_excel("dados_tratados.xlsx", index=False)


def adicionar_na_tabela(dados_tratados):
    tabela_existente = pd.read_excel("informacoes/data/dados_tratados.xlsx")
    nova_linha = {}
    df_novo = pd.DataFrame(nova_linha)
    df_atualizado = pd.concat([tabela_existente, df_novo], ignore_index=True)

    df_atualizado.to_excel("informacoes/data/dados_tratados.xlsx")




            
            



