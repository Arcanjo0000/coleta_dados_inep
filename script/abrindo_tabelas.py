from classe.tabela import Tabela
from tkinter import Tk, Button, Label
import customtkinter as ctk
import os
import pygetwindow as gw
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

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    abriu = ctk.CTk()
    abriu.title("situação da tabela")
    abriu.geometry("780x480")

    pergunta = ctk.CTkLabel(abriu, text="a tabela abrui?")
    pergunta.pack(padx = 20, pady = 20)

    botao_abriu = ctk.CTkButton(abriu, text="Sim", command=lambda:prosseguir(abriu, caminho))
    botao_abriu.pack(padx = 20, pady= 20)
    
    botao_nao_abriu = ctk.CTkButton(abriu, text="Não", command=lambda:deu_erro(abriu))
    botao_nao_abriu.pack(padx = 20, pady = 20)

    abriu.mainloop()


def prosseguir(janela, caminho):
    fechar_janela(janela)
    trasicao_excel()
    coleta(caminho)

def trasicao_excel():
    janela_excel = [w for w in gw.getWindowsWithTitle("Excel") if "Excel" in w.title]
    if janela_excel:
        janela_excel = janela_excel[0]
        janela_excel.activate()

def fechar_excel():
    excel = Dispatch("Excel.application")
    excel.Quit()
    del excel

def deu_erro(janela):
    fechar_excel()
    fechar_programa(janela)

def fechar_programa(janela):
    fechar_janela(janela)
    exit()

def proxima_tabela(janela):
    fechar_janela(janela)

def acessando_tabelas(caminhos):
    arquivos_data = os.listdir("informacoes/data") # é uma lista animal
    
    for item_path in caminhos:
            caminho = item_path
            nome_do_arquivo = os.path.basename(caminho)
            mensagem = f"deseja abrir a tabela localizada em {nome_do_arquivo}"
            ano_do_arquivo = "".join(filter(str.isdigit, nome_do_arquivo))
            pular = False

            if any(ano_do_arquivo in arquivo_data for arquivo_data in arquivos_data):
                continue

            #janela
            ctk.set_appearance_mode("System")
            ctk.set_default_color_theme("blue")

            janela = ctk.CTk()
            janela.geometry("780x480")
            janela.title("perguntinha rápida")


            texto = ctk.CTkLabel(janela, text=mensagem)
            texto.pack(padx = 20, pady = 20)
            

            botao_confirmar = ctk.CTkButton(janela, text="Sim", command=lambda: abrir_tabela(caminho, janela))
            botao_confirmar.pack(padx= 20, pady = 20)

            botao_passar = ctk.CTkButton(janela, text="pular", command=lambda:proxima_tabela(janela))
            botao_passar.pack(padx= 20, pady = 20)

            botao_fechar = ctk.CTkButton(janela, text="fechar", command=lambda:fechar_programa(janela))
            botao_fechar.pack(padx = 20, pady = 20)

            janela.mainloop()
