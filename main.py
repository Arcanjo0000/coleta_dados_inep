from classe.tabela import Tabela
from script.pegando_caminho_tabelas import pergunta
from script.lendo_json import ler_caminhos, ler_estrutura
from script.abrindo_tabelas import acessando_os_caminhos, acessando_tabelas
from script.tratamento_de_dados import tratando_dados


def main():
    pergunta()    
    caminhos = ler_caminhos()
    estrutura = ler_estrutura()
    Tabela.setTabela(caminhos, estrutura)
    caminhos_utilizaveis = acessando_os_caminhos()
    acessando_tabelas(caminhos_utilizaveis)
    
    tratando_dados()


if __name__ == "__main__":
    main()