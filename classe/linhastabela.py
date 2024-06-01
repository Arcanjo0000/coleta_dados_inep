from typing import Any


class LinhasTabela:
    sheet_registrados = []
    lista_de_linhas = []
    
    def __init__(self, curso, ano, pub_pre = None, pub_ead = None, priv_pre = None, priv_ead = None):
        self.curso = curso
        self.ano = ano
        self.pub_pre = pub_pre
        self.pub_ead = pub_ead
        self.priv_pre = priv_pre
        self.priv_ead = priv_ead
        self.__class__.lista_de_linhas.append(self)

    

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        LinhasTabela.sheet_registrados.append(cls)

    @classmethod
    def listar_sheets_registrados(cls):
        return cls.sheet_registrados
    
    @classmethod
    def listar_lista_de_linhas(cls):
        return cls.lista_de_linhas
    
    @classmethod
    def buscar_sheet(cls, sheet):
        return [classe for classe in cls.lista_de_linhas if isinstance(classe, sheet)]
    
    def get_atributo(self, atriubuto):
        return getattr(self, atriubuto, None)
        
    def colocar_atributos_ead(self, pub_ead, priv_ead):
        self.pub_ead = pub_ead
        self.priv_ead = priv_ead

