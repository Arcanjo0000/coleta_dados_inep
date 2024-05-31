from typing import Any


class LinhasTabela:
    lista_de_linhas = []
    def __init__(self, curso, ano):
        self.curso = curso
        self.ano = ano
        self.pub_pre = None
        self.pub_ead = None
        self.priv_pre = None
        self.priv_ead = None
        LinhasTabela.lista_de_colunas.append(self)

    def get_atributos(self, atributo):
        match atributo:
            case "ano":
                return self.ano
            case "curso":
                return self.curso
            case "pub_pre":
                return self.pub_pre
            case "pub_ead":
                return self.pub_ead
            case "priv_pre":
                return self.priv_pre
            case "priv_ead":
                return self.priv_ead
    
    @classmethod
    def criarlinha(cls, ano, codigo_curso, modalidade, publica, privada, tipo_dado):
        pass


#sugestão de manipulação da classe pelo gemini

# class LinhasTabela:
#   lista_de_linhas = []

#   def __init__(self, curso, ano):
#     self.curso = curso
#     self.ano = ano
#     self.pub_pre = None
#     self.pub_ead = None
#     self.priv_pre = None
#     self.priv_ead = None
#     LinhasTabela.lista_de_linhas.append(self)

# # Criando algumas linhas de exemplo
# linha1 = LinhasTabela("Informática", 2023)
# linha1.pub_pre = 8.5
# linha1.pub_ead = 7.0
# linha1.priv_pre = 9.0
# linha1.priv_ead = 8.5

# linha2 = LinhasTabela("Administração", 2022)
# linha2.pub_pre = 7.8
# linha2.pub_ead = 6.5
# linha2.priv_pre = 8.2
# linha2.priv_ead = 7.8

# # Percorrendo as linhas e calculando a média do pub_pre
# soma_pub_pre = 0
# numero_linhas = len(LinhasTabela.lista_de_linhas)

# for linha in LinhasTabela.lista_de_linhas:
#   pub_pre_linha = linha.pub_pre
#   if pub_pre_linha is not None:
#     soma_pub_pre += pub_pre_linha

# media_pub_pre = soma_pub_pre / numero_linhas

# # Filtrando linhas por curso
# linhas_informatica = []

# for linha in LinhasTabela.lista_de_linhas:
#   if linha.curso == "Informática":
#     linhas_informatica.append(linha)

# # Manipulando dados em massa com Pandas (opcional)
# import pandas as pd

# # Criando um DataFrame a partir da lista de linhas
# df_linhas = pd.DataFrame([linha.__dict__ for linha in LinhasTabela.lista_de_linhas])

# # Calculando a média do pub_pre por curso
# media_pub_pre_por_curso = df_linhas.groupby('curso')['pub_pre'].mean()

# # Imprimindo os resultados
# print("Média do pub_pre para todas as linhas:", media_pub_pre)
        

