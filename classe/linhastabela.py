from typing import Any


class LinhasTabela:
    sheet_registrados = []
    lista_de_linhas = []
    
    def __init__(self, curso, ano, pub_pre, priv_pre):
        self.curso = curso
        self.ano = ano
        self.pub_pre = pub_pre
        self.pub_ead = None
        self.priv_pre = priv_pre
        self.priv_ead = None
        self.__class__.lista_de_linhas.append(self)



    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        LinhasTabela.sheet_registrados.append(cls)

    @classmethod
    def listar_sheets_registrados(cls):
        return cls.sheet_registrados
    
    @classmethod
    def listar_linhas(cls):
        lista_de_representação = []

        for planilha in cls.lista_de_linhas:
            nome_planilha = type(planilha).__name__
            try:
                atributos_publicos = {chave: valor for chave, valor in planilha.__dict__.items() if chave in ["curso", "ano", "pub_pre", "pub_ead", "priv_pre", "priv_ead"]}
                atributos_separados = ", ".join(f"{chave}={valor}" for chave, valor in atributos_publicos.items())
                lista_de_representação.append(f"{nome_planilha}({atributos_separados})")
            except TypeError:
                lista_de_representação.append(f"{nome_planilha}(não pode ser instanciada)")

        return lista_de_representação
        
    
    @classmethod
    def buscar_sheet(cls, sheet):
        return [classe for classe in cls.lista_de_linhas if isinstance(classe, sheet)]
    
    def get_atributo(self, atriubuto):
        return getattr(self, atriubuto, None)
        
    
        

