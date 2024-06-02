import os
import pandas as pd
from itertools import islice
import more_itertools as mit
from classe.linhastabela import LinhasTabela
from classe.linha_sheet_cursos import CursosSheet
from classe.linha_sheet_matriculas import MatriculasSheet
from classe.linhas_sheet_concluintes import ConcluintesSheet

def pegando_arquivos_com_dados():
    #lista com os arquivo
    arquivos_com_dados = os.listdir("informacoes/data")

    for arquivo in arquivos_com_dados:
        ano = "".join(filter(str.isdigit, arquivo))
        ano = int(ano)
        estrutura_antiga = ano < 2021
        estrutura_nova = ano >= 2021
        estrutura_especial = ano == 2009
        
        caminho_arquivo = os.path.join("informacoes/data", arquivo)
        #abre os arquivos
        dados_do_arquivo = lendo_arquivo(caminho_arquivo)

        dados_transformados = tranformando_dados(dados_do_arquivo)


        if estrutura_nova:
            separando_modalidades_novo(dados_transformados, ano)
        # elif estrutura_antiga:
        #     separando_modalidades_antiga(dados_transformados, ano)
        
    listar_instancias()
    




def tranformando_dados(dados_do_arquivo):
    lista_com_dados_como_numero = []
    for dado_list in dados_do_arquivo:
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

def eparando_modalidades_antiga(lista_com_dados_int, ano):
    pass



def separando_tipos_de_dados(dados_do_curso, codigo_curso, ano, struct, modalidade):
    if struct == 0:

        dados_separados = mit.chunked(dados_do_curso, 7)
        
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
                    continue
            

def tratar_dados_novos(tipo_dado, dados, ano, codigo_curso, modalidade):
        
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
        soma_publica = sum(publica)
        soma_privada = sum(privada)
        # print(f"ano = {ano} curso = {codigo_curso}, tipo do dado = {tipo_dado} modalidade = {modalidade} publica = {soma_publica} privada = {soma_privada}")
        passar_dados_para_tabela(ano, codigo_curso, tipo_dado, soma_publica, soma_privada, modalidade)

    



def passar_dados_para_tabela(ano, codigo_curso, tipo_dado, publica, privada, modalidade):
    
    # aqui é onde eu crio as instâncias

    if modalidade == "presencial":
        match tipo_dado:
            case "cursos":
                CursosSheet(codigo_curso, ano, pub_pre=publica, priv_pre=privada)
            case "matriculas":
                MatriculasSheet(codigo_curso, ano, pub_pre=publica, priv_pre=privada)
            case "concluintes":
                ConcluintesSheet(codigo_curso, ano, pub_pre=publica, priv_pre=privada)
            case _:
                print("erro ao tentar criar o tipo da instância")

    elif modalidade == "EAD":
        
        for instancia in LinhasTabela.lista_de_linhas:
            if isinstance(instancia, CursosSheet):
                if instancia.get_atributo("ano") == ano and instancia.get_atributo("curso") == codigo_curso and instancia not in CursosSheet.lista_de_instancias_modificadas:
                    instancia.colocar_atributos_ead(publica, privada)
                else:
                    pass

            elif isinstance(instancia, MatriculasSheet):
                
                if instancia.get_atributo("ano") == ano and instancia.get_atributo("curso") == codigo_curso and instancia not in MatriculasSheet.lista_de_instancias_modificadas:
                    instancia.colocar_atributos_ead(publica, privada)
                else:
                    pass

            elif isinstance(instancia, ConcluintesSheet):
                if instancia.get_atributo("ano") == ano and instancia.get_atributo("curso") == codigo_curso and instancia not in ConcluintesSheet.lista_de_instancias_modificadas:
                    instancia.colocar_atributos_ead(publica, privada)
                else:
                    pass


    else:
        print("erro ao criar as instâcias")
    







def criar_tabela():
    colunas_da_tabela = ["curso","ano", "tipo.dado", "pub.pre","pub.ead", "priv.pre", "priv.ead"]
    dados = {coluna: [] for coluna in colunas_da_tabela}
    df = pd.DataFrame(dados)
    df.to_excel("tabela/dados_tratados.xlsx", index=False)


def adicionar_na_tabela(dados_tratados):
    tabela_existente = pd.read_excel("informacoes/data/dados_tratados.xlsx")
    nova_linha = {}
    df_novo = pd.DataFrame(nova_linha)
    df_atualizado = pd.concat([tabela_existente, df_novo], ignore_index=True)

    df_atualizado.to_excel("informacoes/data/dados_tratados.xlsx")




def listar_instancias():
    lista_das_linhas = LinhasTabela.listar_linhas()
    
    for item in lista_das_linhas:
        print()
        print(item)



