import sqlite3
from link_tabela import link

def excluir_banco_dados(nome_tabela):
    # Conectar ao banco de dados
    banco = sqlite3.connect(link)
    cursor = banco.cursor()

    # Deletar todos os registros da tabela 'produtos'
    cursor.execute(f'DELETE FROM {nome_tabela};')

    # Salvar as alterações e fechar a conexão
    banco.commit()
    banco.close()

#use com muito cuidado essa funcao
#ela ira excluir todos os registros dentro da tabela que voce selecionar
excluir_banco_dados('')