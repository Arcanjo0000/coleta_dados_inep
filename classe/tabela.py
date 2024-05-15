class Tabela():
    lista_tabela = []
    def __init__(self, colunas, linhas, ano, caminho, sheet):
        self.colunas = colunas
        self.linhas = linhas
        self.ano = ano
        self.caminho = caminho
        self.sheet = sheet
        Tabela.lista_tabela.append(self)

    def __str__(self):
        return f"ano : {self.ano} | colunas: {self.colunas} | linhas: {self.linhas} | sheet: {self.sheet} | caminho: {self.caminho}"

    @classmethod
    def listar_objetos(cls):
        for tabela in cls.lista_tabela:
            print()
            print(tabela)

    def get(self, atributo):
        match atributo:
            case "caminho":
                return self.caminho
            case "ano":
                return self.ano
            case "colunas":
                return self.colunas
            case "linhas":
                return self.linhas
            case "sheet":
                return self.sheet
            case _:
                print(f"Erro: atributo {atributo} invalido")
                exit()



    @classmethod
    def setTabela(cls, caminhos, estrutura):
        for ano in range(2022, 2008, -1):
            for item_struct in estrutura:
                chave_caminho = f"tabela_{ano}"
                if str(item_struct["ano"]) in str(chave_caminho):
                    ano = item_struct.get("ano")
                    linhas = item_struct.get("linhas")
                    colunas = item_struct.get("colunas")
                    sheet = item_struct.get("sheet")
                    caminho = caminhos.get(chave_caminho)
                    cls(colunas, linhas, ano, caminho, sheet)
                    break
