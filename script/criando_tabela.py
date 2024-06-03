import pandas as pd
from classe.linhastabela import LinhasTabela
from classe.linha_sheet_cursos import CursosSheet
from classe.linha_sheet_matriculas import MatriculasSheet
from classe.linhas_sheet_concluintes import ConcluintesSheet

def comecar_criacao():
    organizar_dados()

    

def organizar_dados():
    planilhas = {
        "Cursos": [],
        "Matriculas": [],
        "Concluintes": []
    }
    for linha in LinhasTabela.lista_de_linhas:
        if isinstance(linha, CursosSheet):
            planilhas["Cursos"].append(vars(linha))
        elif isinstance(linha, MatriculasSheet):
            planilhas["Matriculas"].append(vars(linha))
        elif isinstance(linha, ConcluintesSheet):
            planilhas["Concluintes"].append(vars(linha))

    criar_tabela(planilhas)

def criar_tabela(planilhas):
    with pd.ExcelWriter("tabela/dados_tratados.xlsx", engine="openpyxl") as writer:

        for planilha, linhas in planilhas.items():

            df = pd.DataFrame(linhas)

            df.to_excel(writer, sheet_name=planilha, index=False)
