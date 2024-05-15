import os
from typing import Dict
from tkinter import filedialog, Tk, Button
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
    janela_secundaria = Tk()
    janela_secundaria.title("listar arquivos")
    janela_secundaria.configure(pady=30, padx=100)

    botao_selecionar = Button(janela_secundaria, text="selecionar diretorio", command=lambda: pegar_caminho(janela_pricipal,janela_secundaria))
    botao_selecionar.pack(pady=10)
    janela_secundaria.mainloop()

def fechar_janela(janela_pricipal, janela_secundaria=None) -> None:
    janela_pricipal.destroy()
    if janela_secundaria != None:
        janela_secundaria.destroy()

def passar(janela_principal):
    fechar_janela(janela_principal)


def pergunta():
    janela_pricipal = Tk()
    janela_pricipal.title("ja escolheu a pasta com os arquivos?")
    janela_pricipal.configure(padx=300,pady=100)
    botao_sim = Button(janela_pricipal, text="sim", command=lambda:passar(janela_pricipal))
    botao_sim.pack(pady=10)
    botao_nao = Button(janela_pricipal, text="não", command=lambda:abrir_janela(janela_pricipal))
    botao_nao.pack(pady=10)
    janela_pricipal.mainloop()



