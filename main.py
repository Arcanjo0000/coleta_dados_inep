import tkinter as tk
import customtkinter as ctk
from classe.tabela import Tabela
from script.pegando_caminho_tabelas import pergunta
from script.lendo_json import ler_caminhos, ler_estrutura
from script.abrindo_tabelas import acessando_os_caminhos, acessando_tabelas
from script.tratamento_de_dados import pegando_arquivos_com_dados

def fechar_janela(janela):
    janela.destroy()

def encerrar(janela):
    fechar_janela(janela)
    print("encerrando")
    exit()

def continuar():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    janela = ctk.CTk()
    janela.geometry("780x480")
    janela.title("o que fazer?")

    texto = ctk.CTkLabel(janela, text="deseja continuar para o tratamento de dados?")
    texto.pack(padx = 20, pady = 20)
    
    botao_sim = ctk.CTkButton(janela, text="Sim", command=lambda:tratar_dados(janela))
    botao_sim.pack(padx = 20, pady = 20)

    botao_nao = ctk.CTkButton(janela, text="Não", command=lambda:encerrar(janela))
    botao_nao.pack(padx = 20, pady = 20)

    janela.mainloop()


def coletar_dados(janela):
    fechar_janela(janela)
    pergunta()    
    caminhos = ler_caminhos()
    estrutura = ler_estrutura()
    Tabela.setTabela(caminhos, estrutura)
    caminhos_utilizaveis = acessando_os_caminhos()
    acessando_tabelas(caminhos_utilizaveis)
    continuar()

def tratar_dados(janela):
    fechar_janela(janela)
    pegando_arquivos_com_dados()

def iniciando():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("780x480")
    app.title("passos a seguir...")
    texto = ctk.CTkLabel(app, text="deseja coletar os dados ou tratar os dados?")
    texto.pack(padx = 20, pady = 20)
    botao_coleta = ctk.CTkButton(app, text="coletar", command=lambda:coletar_dados(app))
    botao_coleta.pack(padx = 20, pady = 20)
    botao_tratar = ctk.CTkButton(app, text="tratar dados", command=lambda:tratar_dados(app))
    botao_tratar.pack(padx = 20, pady = 20)

    app.mainloop()




def main():
    iniciando()    


if __name__ == "__main__":
    main()