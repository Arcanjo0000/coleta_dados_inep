import os
import pandas as pd
from itertools import islice

def pegando_arquivos_com_dados():
    #lista com os arquivo
    arquivos_com_dados = os.listdir("informacoes/data")

    for arquivo in arquivos_com_dados:
        ano = "".join(filter(str.isdigit, arquivo))
        ano = int(ano)
        estrutura_antiga = ano < 2021
        estrutura_nova = ano >= 2021
        estrutura_bem_antiga = ano == 2009
        lista_com_7 = []
        lista_sem_7 = []
        lista_publica = []
        lista_privada = []
        
        caminho_arquivo = os.path.join("informacoes/data", arquivo)
        #abre os arquivos
        with open(str(caminho_arquivo), "r") as file:
            dados_do_arquivo = []
            for linha in file:
                linha_limpa = linha.split()
                #tira os espaços das linhas
                if linha_limpa:
                    dados_do_arquivo.append(linha_limpa)
        lista_com_dados_como_numero = []
        for idx, dado_list in enumerate(dados_do_arquivo):
            dado_str = dado_list[0]
            dado_int = int(dado_str.replace(".",""))
            lista_com_dados_como_numero.append(dado_int)


        if estrutura_nova:
            # tenho que separar por curso ano pub.pre pub.ead priv.pre priv.ead
            iterador = iter(lista_com_dados_como_numero)
            presencial = list(islice(iterador, 84))
            ead = list(iterador)
            print()
            print(f"ano = {ano}")
            print()
            print(f"dados presenciais: \n{presencial}")
            print()
            print(f"dados ead: \n{ead}")
            # deu certo 🥳🤓
            




            # aqui tem que ter uma loop para cada curso, mas como eu faço isso?
            # for curso in cursos:
            #     print()
            #     print(f"curso = {curso}")
            #     # separa os dados dos arquivos em duas listas 
            #     for idx, dado in enumerate(dados_do_arquivo):
            #         print(f"dado = {idx}")
            #         dado_com_ponto = dado[0]
            #         dado_sem_ponto = dado_com_ponto.replace(".", "")
            #         dado = int(dado_sem_ponto)
            #         print(dado)

            #         if (idx + 1) % 7 == 0:
            #             lista_com_7.append(int(dado))
            #         else:
                        
            #             lista_sem_7.append(int(dado))
                

            #     for idx, dado in enumerate(lista_sem_7):
            #         if (idx + 1) % 2 == 0:
            #             # total e priavda estão sendo tratados como lista. por que?

            #             total = lista_sem_7[idx - 1]
            #             privada = lista_sem_7[idx]
            #             publica = total - privada
            #             lista_publica.append(publica)
            #             lista_privada.append(privada)
            #         elif (idx + 1) % 7 == 0:
            #             posicao = idx + 1
            #             match posicao:
            #                 case 7:
            #                     lista_publica.append(lista_com_7[0])
            #                 case 14:
            #                     lista_publica.append(lista_com_7[1])
            #                 case 21:
            #                     lista_publica.append(lista_com_7[2])
                    
                    
                

            




        # if estrutura_antiga:
        #     caminho_arquivo = os.path.join("informacoes/data", arquivo)
        #     with open(str(caminho_arquivo), "r") as file:
        #         dados_do_arquivo = []
        #         for linha in file:
        #             linha_limpa = linha.strip()
        #             dados_do_arquivo.append(linha_limpa)
        #         tratar_dados_antigos(dados_do_arquivo)
        # elif estrutura_nova:
        #     caminho_arquivo = os.path.join("informacoes/data", arquivo)
        #     with open(str(caminho_arquivo), "r") as file:
        #         dados_do_arquivo = []
        #         for linha in file:
        #             linha_limpa = linha.strip()
        #             dados_do_arquivo.append(linha_limpa)
        #         tratar_dados_novos(dados_do_arquivo)
        # elif estrutura_bem_antiga:

        # else:
        #     print("invalido")
            

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
    #df.to_excel("dados_tratados.xlsx", index=False)


def adicionar_na_tabela(dados_tratados):
    tabela_existente = pd.read_excel("informacoes/data/dados_tratados.xlsx")
    nova_linha = {}
    df_novo = pd.DataFrame(nova_linha)
    df_atualizado = pd.concat([tabela_existente, df_novo], ignore_index=True)

    df_atualizado.to_excel("informacoes/data/dados_tratados.xlsx")




            
            



