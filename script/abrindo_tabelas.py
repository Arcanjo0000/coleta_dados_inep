from classe.tabela import Tabela
from tkinter import Tk, Button
import os
from win32com.client import Dispatch
from script.coleta_dados import coleta


def fechar_janela(janela):
    janela.destroy()

def acessando_os_caminhos():
    tabelas = Tabela.lista_tabela
    lista_caminhos = []
    for tabela in tabelas:
        caminho = tabela.get("caminho")
        lista_caminhos.append(caminho)
    return lista_caminhos

def abrir_tabela(caminho, janela):
    fechar_janela(janela)
    os.startfile(caminho)
    coleta(caminho)

def fechar_tabela(janela):
    try:
        fechar_janela(janela)
        excel = Dispatch("Excel.application")
        excel.Quit()
        del excel
        print("excel foi fechado com sucesso")
    except Exception as e:
        print("erro ao fechar o excel:", str(e))

def acessando_tabelas(caminhos):
    arquivos_data = os.listdir("informacoes/data") # é uma lista animal

    for item_data in arquivos_data:
        for item_path in caminhos:
            if str(item_data) in str(item_path):
                pass
            else:
                caminho = item_path
                #janela
                janela = Tk()
                janela.geometry("400x300")
                janela.title("perguntinha rápida")
                botao_comfirmar = Button(janela, text="OK", command=lambda: abrir_tabela(caminho, janela))
                botao_cancelar = Button(janela, text="CANCELAR", command=lambda: fechar_tabela(janela))
                botao_comfirmar.pack(pady=10)
                botao_cancelar.pack(pady=10)
                janela.mainloop()
        
