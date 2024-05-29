from win32gui import FindWindow, SetForegroundWindow
from pyautogui import hotkey, write, press
from win32com.client import Dispatch
from time import sleep
from pyperclip import paste
from classe.tabela import Tabela
from classe.tabela import Tabela
import json

def fechar_excel():
    excel = Dispatch("Excel.application")
    excel.Quit()
    del excel

def coleta(caminho):
    lista_de_dados_coletados = []
    linhas, colunas, sheets, ano = puxando_dados_estruturais(caminho) # Verificar se os dados foram puxados corretamente
    print(f"Linhas: {linhas}, Colunas: {colunas}, Sheets: {sheets}, Ano: {ano}")
    formatando_estrutura_para_escrever(linhas, colunas, sheets, lista_de_dados_coletados, ano)
    gravando_dados(ano, lista_de_dados_coletados)
    fechar_excel()

def formatando_estrutura_para_escrever(linhas, colunas, sheets, lista_de_dados, ano):

        for modalidade_sheet in sheets:
            sheet = sheets[modalidade_sheet]
            for modalidade_linhas in linhas:
                dict_linhas = linhas[modalidade_linhas]
                if str(modalidade_sheet) == (modalidade_linhas):
                    for chave in dict_linhas:
                        linha = dict_linhas[chave]
                        print(f"o curso é {chave}")
                        
                        if chave == "adm" and ano >= 2021:
                            with open("informacoes/adm.json", "r") as file:
                                estrutura_para_adm = json.load(file)
                                
                                dados_adm = ""
                                match ano:
                                    case 2022:
                                        dados_adm = estrutura_para_adm[0]
                                    case 2021:
                                        dados_adm = estrutura_para_adm[1]
                                colunas_adm = dados_adm.get("colunas")
                                for chave in colunas_adm:
                                    lista_coluna = colunas_adm.get(chave)
                                    for coluna in lista_coluna:
                                        print(f"coordenadas = {sheet}{coluna}{linha}")
                                        movendo(sheet, coluna, linha)
                                        coleta_info(lista_de_dados)
                            #pular adm no loop de linhas
                            continue
                        else:
                            for chave in colunas:
                                if isinstance(colunas, dict):
                                    valores = colunas.get(chave)
                                    for valor in valores:
                                        coluna = valor
                                        print(f"coordenadas = {sheet}{coluna}{linha}")
                                        movendo(sheet, coluna, linha,)
                                        coleta_info(lista_de_dados)
                                else:
                                    coluna = chave
                                    print(f"coordenadas = {sheet}{coluna}{linha}")
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
    local_armazenamento = f"informacoes/data/{ano}.txt"
    with open (local_armazenamento, "w") as file:
        for dado in dados_coletados:
            file.write(dado + "\n")


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


