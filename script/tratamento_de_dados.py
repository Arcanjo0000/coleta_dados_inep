import os
import pandas as pd
from itertools import islice
import more_itertools as mit
from classe.linhastabela import LinhasTabela
from classe.linha_sheet_cursos import CursosSheet
from classe.linha_sheet_matriculas import MatriculasSheet
from classe.linhas_sheet_concluintes import ConcluintesSheet
from script.criando_tabela import comecar_criacao

def pegando_arquivos_com_dados():
    #lista com os arquivo
    arquivos_com_dados = os.listdir("informacoes/data")

    for arquivo in arquivos_com_dados:
        ano = "".join(filter(str.isdigit, arquivo))
        ano = int(ano)
        estrutura_antiga = 2021 > ano > 2009
        estrutura_nova = ano >= 2021
        estrutura_especial = ano == 2009
        
        caminho_arquivo = os.path.join("informacoes/data", arquivo)
        #abre os arquivos
        dados_do_arquivo = lendo_arquivo(caminho_arquivo)

        dados_transformados = tranformando_dados(dados_do_arquivo)


        if estrutura_nova:
            separando_modalidades_novo(dados_transformados, ano)
        
        elif estrutura_antiga:
            separando_modalidades_antigo(dados_transformados, ano)

        elif estrutura_especial:
            separando_modalidades_especial(dados_transformados, ano)
        
    # listar_instancias()
    comecar_criacao()




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
    iterador = iter(lista_com_dados_int)
    presencial = list(islice(iterador, 84))
    ead = list(iterador)
    cursos_presenciais = mit.chunked(presencial, 21)
    #o idx é o código do curso
    # presenciais
    for idx, curso in enumerate(cursos_presenciais):
        modalidade = "presencial"
        match idx:
            case 0:
                codigo_curso = idx
                separando_tipos_de_dados_novo(curso, codigo_curso, ano, modalidade)
            case 1:
                codigo_curso = idx
                separando_tipos_de_dados_novo(curso, codigo_curso, ano, modalidade)
            case 2:
                codigo_curso = idx
                separando_tipos_de_dados_novo(curso, codigo_curso, ano, modalidade)
            case 3:
                codigo_curso = idx
                separando_tipos_de_dados_novo(curso, codigo_curso, ano, modalidade)
            case _ :
                print("erro ao tentar separar os cursos presenciais")
    
    cursos_ead = mit.chunked(ead, 21)
    for idx, curso in enumerate(cursos_ead):
        modalidade = "EAD"
        match idx:
            case 0:
                codigo_curso = idx
                separando_tipos_de_dados_novo(curso, codigo_curso, ano, modalidade)
            case 1:
                codigo_curso = idx
                separando_tipos_de_dados_novo(curso, codigo_curso, ano, modalidade)
            case 2:
                codigo_curso = idx
                separando_tipos_de_dados_novo(curso, codigo_curso, ano, modalidade)
            case 3:
                codigo_curso = idx
                separando_tipos_de_dados_novo(curso, codigo_curso, ano, modalidade)
            case _ :
                print("erro ao tentar separar os cursos EAD")

def separando_modalidades_antigo(lista_com_dados_int, ano):

    iterador = iter(lista_com_dados_int)
    presencial = list(islice(iterador, 24))
    ead = list(iterador)
    
    tipo_de_dados_presencial = mit.chunked(presencial, 8)

    for idx, dados in enumerate(tipo_de_dados_presencial):
        # idx é o tipo do dado 0 = curso, 1 = matricula, 2 = concluintes
        
        modalidade = "presencial"
        match idx:
            case 0:
                tipo_de_dado = "cursos"
                tratando_dados_antigo(tipo_de_dado, dados, ano, modalidade)
            case 1:
                tipo_de_dado = "matriculas"
                tratando_dados_antigo(tipo_de_dado, dados, ano, modalidade)
            case 2: 
                tipo_de_dado = "concluintes"
                tratando_dados_antigo(tipo_de_dado, dados, ano, modalidade)

    tipo_de_dados_ead = mit.chunked(ead, 8)
    for idx, dados in enumerate(tipo_de_dados_ead):
        # idx é o tipo do dado 0 = curso, 1 = matricula, 2 = concluintes   
        modalidade = "EAD"
        match idx:
            case 0:
                tipo_de_dado = "cursos"
                tratando_dados_antigo(tipo_de_dado, dados, ano, modalidade)
            case 1:
                tipo_de_dado = "matriculas"
                tratando_dados_antigo(tipo_de_dado, dados, ano, modalidade)
                
            case 2: 
                tipo_de_dado = "concluintes"
                tratando_dados_antigo(tipo_de_dado, dados, ano, modalidade)

def separando_modalidades_especial(lista_com_dados_int, ano):
    iterador = iter(lista_com_dados_int)
    presencial = list(islice(iterador, 36))
    ead = list(iterador)
    
    tipo_de_dados_presencial = mit.chunked(presencial, 12)

    for idx, dados in enumerate(tipo_de_dados_presencial):
        modalidade = "presencial"    
        match idx:
            case 0:
                tipo_de_dado = "cursos"
                tratar_dados_especial(tipo_de_dado, dados, ano, modalidade)
            case 1:
                tipo_de_dado = "matriculas"
                tratar_dados_especial(tipo_de_dado, dados, ano, modalidade)
            case 2:
                tipo_de_dado = "concluintes"
                tratar_dados_especial(tipo_de_dado, dados, ano, modalidade)
    
    tipo_de_dados_ead = mit.chunked(ead, 12)

    for idx, dados in enumerate(tipo_de_dados_ead):
        modalidade = "EAD"    
        match idx:
            case 0:
                tipo_de_dado = "cursos"
                tratar_dados_especial(tipo_de_dado, dados, ano, modalidade)
            case 1:
                tipo_de_dado = "matriculas"
                tratar_dados_especial(tipo_de_dado, dados, ano, modalidade)
            case 2:
                tipo_de_dado = "concluintes"
                tratar_dados_especial(tipo_de_dado, dados, ano, modalidade)


def separando_tipos_de_dados_novo(dados_do_curso, codigo_curso, ano, modalidade):

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
        formatar_para_passar_dados_para_tabela(ano, codigo_curso, tipo_dado, soma_publica, soma_privada, modalidade)

def tratando_dados_antigo(tipo_de_dado, dados, ano, modalidade):
    publica = None
    privada = None
    dados_por_curso = mit.chunked(dados, 2)
    for idx, dado in enumerate(dados_por_curso):

        codigo_do_curso = idx
        total = dado[0]
        total_privada = dado[1]
        total_publica = total - total_privada
        publica = total_publica
        privada = total_privada
        
        formatar_para_passar_dados_para_tabela(ano, codigo_do_curso, tipo_de_dado, publica, privada, modalidade)

def tratar_dados_especial(tipo_de_dado, dados, ano, modalidade):
    publica = None
    privada = None
    dados_por_curso = mit.chunked(dados, 3)

    for idx, dado in enumerate(dados_por_curso):

        codigo_do_curso = idx
        total = dado[0]
        total_privada = dado[1] + dado[2]
        total_publica = total - total_privada
        privada = total_privada
        publica = total_publica    
        formatar_para_passar_dados_para_tabela(ano, codigo_do_curso, tipo_de_dado, publica, privada, modalidade)
    



def formatar_para_passar_dados_para_tabela(ano, codigo_curso, tipo_dado, publica, privada, modalidade):
    
    if modalidade == "presencial":
        match tipo_dado:
            case "cursos":
                CursosSheet(codigo_curso, ano, publica, privada)
            case "matriculas":
                MatriculasSheet(codigo_curso, ano, publica, privada)
            case "concluintes":
                ConcluintesSheet(codigo_curso, ano, publica, privada)
            case _:
                print("erro ao tentar criar o tipo da instância")

    elif modalidade == "EAD":
        
        for instancia in LinhasTabela.lista_de_linhas:

            if isinstance(instancia, CursosSheet):
                if instancia.get_atributo("ano") == ano and instancia.get_atributo("curso") == codigo_curso and instancia not in CursosSheet.lista_de_instancias_modificadas:
                    instancia.colocar_atributos_ead(publica, privada)
                    break
                else:
                    pass

            elif isinstance(instancia, MatriculasSheet):
                
                if instancia.get_atributo("ano") == ano and instancia.get_atributo("curso") == codigo_curso and instancia not in MatriculasSheet.lista_de_instancias_modificadas:
                    instancia.colocar_atributos_ead(publica, privada)
                    break
                else:
                    pass

            elif isinstance(instancia, ConcluintesSheet):
                if instancia.get_atributo("ano") == ano and instancia.get_atributo("curso") == codigo_curso and instancia not in ConcluintesSheet.lista_de_instancias_modificadas:
                    instancia.colocar_atributos_ead(publica, privada)
                    break
                else:
                    pass
    else:
        print("erro ao criar as instâcias")


def adicionar_na_tabela(dados_tratados):
    tabela_existente = pd.read_excel("informacoes/data/dados_tratados.xlsx")
    nova_linha = {}
    df_novo = pd.DataFrame(nova_linha)
    df_atualizado = pd.concat([tabela_existente, df_novo], ignore_index=True)

    df_atualizado.to_excel("informacoes/data/dados_tratados.xlsx")

def listar_instancias():
    lista_das_linhas = LinhasTabela.listar_linhas()
    print(len(lista_das_linhas))
    for item in lista_das_linhas:
        print()
        print(item)



