from classe.linhastabela import LinhasTabela
class MatriculasSheet(LinhasTabela):
    lista_de_instancias_modificadas = []

    def __init__(self, curso, ano, pub_pre, priv_pre):
        super().__init__(curso, ano, pub_pre, priv_pre)
    
    def __str__(self):
        return f"tipo de dado: matricula | curso: {self.curso} | ano: {self.ano} | pub_pre: {self.pub_pre} | pub_ead: {self.pub_ead} | priv_pre: {self.priv_pre} | priv_ead: {self.priv_ead}"
    
    def colocar_atributos_ead(self, pub_ead, priv_ead):
        self.pub_ead = pub_ead
        self.priv_ead = priv_ead
        MatriculasSheet.lista_de_instancias_modificadas.append(self)