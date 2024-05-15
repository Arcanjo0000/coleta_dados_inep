import os

def tratando_dados():
    
    arquivos_com_dados = os.listdir("informacoes/data")
    for ano in range(2022, 2008, -1):
        for arquivo in arquivos_com_dados:
            estrutura_antiga = ano < 2021
            if str(arquivo) in str(ano):
                if estrutura_antiga:
                    caminho_arquivo = os.path.join("informacoes/data", arquivo)
                    with open(str(arquivo), "r") as file:
                        dados_do_arquivo = []
                        for linha in file:
                            dados_do_arquivo.append(linha)

                        
                        criar_csv_antigo(dados_do_arquivo)

def criar_csv_antigo():
    pass

            
            



