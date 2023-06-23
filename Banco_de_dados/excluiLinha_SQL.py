import sqlite3

def Excluir_linha_SQL(nomeTabela, Condicao, valor, excluirSaida=False):
    # Conectar ao banco de dados
    conexao = sqlite3.connect('Banco_de_dados/estoque.db')
    cursor = conexao.cursor()

    # Executar a consulta SQL para excluir uma linha
    consulta = f"DELETE FROM '{nomeTabela}' WHERE {Condicao}='{valor}' "
    # Substitua 'nome_da_tabela' pelo nome da tabela em que você deseja excluir a linha
    # Substitua 'condicao' pela condição que identifica a linha que você deseja excluir
    # Por exemplo, se a linha que você deseja excluir tem um ID igual a 1, a condição seria 'id = 1'

    cursor.execute(consulta)

    if excluirSaida:
        # Executar a consulta SQL para excluir uma linha
        consulta2 = f"DELETE FROM 'saida_materias_primas' WHERE numeroOrdem='{valor}' "
        # Substitua 'nome_da_tabela' pelo nome da tabela em que você deseja excluir a linha
        # Substitua 'condicao' pela condição que identifica a linha que você deseja excluir
        # Por exemplo, se a linha que você deseja excluir tem um ID igual a 1, a condição seria 'id = 1'

        cursor.execute(consulta2)


    # Confirmar a exclusão
    conexao.commit()

    # Fechar a conexão com o banco de dados
    conexao.close()