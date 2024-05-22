from win32gui import FindWindow, SetForegroundWindow
from pyautogui import hotkey, write, press
from win32com.client import Dispatch
from time import sleep
from pyperclip import paste
from classe.tabela import Tabela

def fechar_excel():
    excel = Dispatch("Excel.application")
    excel.Quit()
    del excel

def coleta(caminho):
    lista_de_dados_coletados = []
    linhas, colunas, sheets, ano = puxando_dados_estruturais(caminho)
    #linhas: dict  colunas: lista  sheets: dict
    formatando_estrutura_para_escrever(linhas, colunas, sheets, lista_de_dados_coletados)
    lista_de_dados_coletados.split()
    gravando_dados(ano, lista_de_dados_coletados)
    fechar_excel()

def formatando_estrutura_para_escrever(linhas, colunas, sheets, lista_de_dados):
    
    # for modalidade_sheet in sheets:
    #     sheet = sheets[modalidade_sheet]
    #     for modalidade_linhas in linhas:
    #         dicionario_linhas = linhas[modalidade_linhas]
    #         if str(modalidade_sheet) == str(modalidade_linhas):
    #             for curso in dicionario_linhas:
    #                 linha = dicionario_linhas[curso]
    #                 for coluna in colunas:
    #                     if coluna == "cursos" or coluna == "matriculas" or coluna == "concluintes":
    #                         for item in coluna:
    #                             coluna = item
    #                     print(f"coordenadas : {sheet} {coluna} {linha}")
    #                     movendo(sheet, coluna, linha,)
    #                     coleta_info(lista_de_dados)  

    for modalidade_sheet in sheets:
        sheet = sheets[modalidade_sheet]
        for modalidade_linhas in linhas:
            dicionario_linhas = linhas[modalidade_linhas]
            if str(modalidade_sheet) == str(modalidade_linhas):
                for curso in dicionario_linhas:
                    linha = dicionario_linhas[curso]
                    for coluna in colunas:
                        if coluna == "cursos" or coluna == "matriculas" or coluna == "concluintes":
                            for item in coluna:
                                coluna = item
                                print(f"coordenadas : {sheet} {coluna} {linha}")
                                movendo(sheet, coluna, linha,)
                                coleta_info(lista_de_dados)
                        else:
                            print(f"coordenadas : {sheet} {coluna} {linha}")
                            movendo(sheet, coluna, linha,)
                            coleta_info(lista_de_dados)

def coleta_info(lista):
    hotkey("ctrl", "c")
    texto_copiado = paste()
    lista.append(texto_copiado)

def tempo_espera(tempo):
    sleep(tempo)

def movendo(sheet, coluna, linha):
    hotkey("ctrl", "g")
    tempo_espera(0.8)
    write(f"{sheet}{coluna}{linha}")
    tempo_espera(0.5)
    press("enter")
    tempo_espera(1)

def gravando_dados(ano, dados_coletados):
    
    with open (f"informacoes/data/{ano}.txt") as file:
        for dado in dados_coletados:
            file.write(dado + "\n")

    # for chave in linhas:
    #     lista_chave = linhas[chave]
    #     print(f"chave: {chave}")
    #     for linha in lista_chave:
    #         print(f"linha: {linha}")
    #         for coluna in colunas:
    #             print(f"coluna: {coluna}")

def focando_na_tabela():
    excel_title = "Microsoft Excel"
    identeficador = FindWindow(None, excel_title)
    if identeficador != 0:
        SetForegroundWindow(identeficador)
    else:
        print("Erro: não foi possível focar a tabela")
        exit()

def puxando_dados_estruturais(caminho):
    tabelas = Tabela.lista_tabela
    for tabela in tabelas:
        if str(tabela.get("ano")) in str(caminho):
            return tabela.get("linhas"), tabela.get("colunas"), tabela.get("sheet"), tabela.get("ano")
