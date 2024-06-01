from classe.linhastabela import LinhasTabela
class CursosSheet(LinhasTabela):
    def __init__(self, curso, ano, pub_pre = None, pub_ead = None, priv_pre = None, priv_ead = None):
        super().__init__(curso, ano, pub_pre, pub_ead, priv_pre, priv_ead)
    
    def __str__(self):
        
        return f"tipo dado : cursos | curso: {self.curso} | ano: {self.ano} | pub_pre: {self.pub_pre} | pub_ead: {self.pub_ead} | priv_pre: {self.priv_pre} | priv_ead: {self.priv_ead}"
    