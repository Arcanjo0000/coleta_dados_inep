import os
from typing import Dict
from tkinter import filedialog, Tk, Button
import customtkinter as ctk
from re import search
import json


def pegar_caminho(janela_pricipal, janela_secundaria) -> Dict:
    diretorio = filedialog.askdirectory()
    if diretorio:
        arquivos = os.listdir(diretorio)
        caminho_arquivos = [os.path.join(diretorio, arquivo) for arquivo in arquivos]
        sequencia_de_numeros = [2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009]
        dicionario = {}
        for caminho in caminho_arquivos:
            for sequencia in sequencia_de_numeros:
                if search(str(sequencia), caminho):
                    chave = f"tabela_{sequencia}"
                    if chave not in dicionario:
                        dicionario[chave] = caminho
                    else:
                        pass
            print(dicionario)
        fechar_janela(janela_pricipal, janela_secundaria)
        criar_json(dicionario)


def criar_json(dicionario: Dict) -> None:
    with open("informacoes\\caminho_tabelas.json", "w") as arquivo:
        json.dump(dicionario, arquivo)


def abrir_janela(janela_pricipal) -> None:
    janela_secundaria = ctk.CTk()
    janela_secundaria.title("listar arquivos")
    janela_secundaria.geometry("780x480")

    botao_selecionar = ctk.CTkButton(janela_secundaria, text="selecionar diretorio", command=lambda: pegar_caminho(janela_pricipal,janela_secundaria))
    botao_selecionar.pack(padx = 20, pady = 20)
    
    janela_secundaria.mainloop()

def fechar_janela(janela_pricipal, janela_secundaria=None) -> None:
    janela_pricipal.destroy()
    if janela_secundaria != None:
        janela_secundaria.destroy()

def passar(janela_principal):
    fechar_janela(janela_principal)


def pergunta():
    janela_pricipal = ctk.CTk()
    janela_pricipal.title("caminho dos arquivos")
    janela_pricipal.geometry("780x480")

    texto = ctk.CTkLabel(janela_pricipal, text="já escolheu a pasta com os arquivos?")
    texto.pack(padx = 20, pady = 20)
    
    botao_sim = ctk.CTkButton(janela_pricipal, text="sim", command=lambda:passar(janela_pricipal))
    botao_sim.pack(pady=20, padx = 20)
    
    botao_nao = ctk.CTkButton(janela_pricipal, text="não", command=lambda:abrir_janela(janela_pricipal))
    botao_nao.pack(padx = 20, pady=10)

    janela_pricipal.mainloop()



