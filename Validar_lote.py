import sqlite3
# Deve receber um valor de um lote e verificar se ele existe

def validar_lote(lote=None):
    # cria a conexão com o banco de dados
    conn = sqlite3.connect('Banco_de_dados/estoque.db')

    # cria o cursor
    cursor = conn.cursor()

    # lista de nomes
    nomes = [lote]

    # cria a query SQL usando a cláusula IN e um loop for
    query = "SELECT * FROM entrada_materias_primas WHERE lote IN ({})".format(', '.join(['?'] * len(nomes)))

    # executa a query e obtém os resultados
    resultados = cursor.execute(query, nomes).fetchall()

    # exibe os resultados
    for resultado in resultados:
        return resultado

    # fecha a conexão com o banco de dados
    conn.close()


def validar_ordem_producao(lote=None):
    # cria a conexão com o banco de dados
    conn = sqlite3.connect('Banco_de_dados/estoque.db')

    # cria o cursor
    cursor = conn.cursor()

    # lista de nomes
    nomes = [lote]

    # cria a query SQL usando a cláusula IN e um loop for
    query = "SELECT * FROM criar_ordem_producao WHERE numero_Ordem IN ({})".format(', '.join(['?'] * len(nomes)))

    # executa a query e obtém os resultados
    resultados = cursor.execute(query, nomes).fetchall()

    # exibe os resultados
    for resultado in resultados:
        return resultado

    # fecha a conexão com o banco de dados
    conn.close()


def verificar_produto_lote(lote=None):
    # cria a conexão com o banco de dados
    conn = sqlite3.connect('Banco_de_dados/estoque.db')

    # cria o cursor
    cursor = conn.cursor()

    # lista de nomes
    nomes = [lote]

    # cria a query SQL usando a cláusula IN e um loop for
    query = "SELECT * FROM entrada_materias_primas WHERE lote IN ({})".format(', '.join(['?'] * len(nomes)))

    # executa a query e obtém os resultados
    resultados = cursor.execute(query, nomes).fetchall()

    # exibe os resultados
    for resultado in resultados:
        return resultado[2]

    # fecha a conexão com o banco de dados
    conn.close()



def verificarCategoriaMatPrima(MateriaPrima):
    categoria = str(MateriaPrima).split(' ')[0]
    print(categoria)

    if categoria == 'Válvula':
        categoria = 'Tampa'

    return categoria