import sqlite3
# Deve receber um valor de um lote e verificar se ele existe

def validarEntradaLote(value_lote, value_quantidade, preenchimento_obrigatorio=True):
    if preenchimento_obrigatorio == True:
        if value_lote != '':
            if validar_lote(value_lote) is not None:
                if value_quantidade != '':
                    try:
                        if int(value_quantidade) > 0:
                            return True
                    # Se ao tentar comparar a quantidade com um int gerar um erro, nao executará
                    except ValueError:
                        return False
                else:
                    # Se o valor do lote nao for maior que 0 ele nao vai aceitar
                    return False
                    print('obrigatorio -  quantidade é inferior a zero ou nula - False')
            else:
                # Se a funcao validar lote nao encontrar um lote, não será aceito
                return False
                print('obrigatorio - lote nao encontrado - False')
        else:
            # Se o 'input' lote igualar nada, não será aceito
            return False
            print('obrigatorio - lote nulo - False')

    if preenchimento_obrigatorio == False:
        # Se valor e quantidade nao forem preenchidos, executa
        if value_lote == '' and value_quantidade == '':
            return True

        # Se preenchimento nao for obrigatorio e valor ou quantidade estiverem preenchidos, validar:
        else:
            # Se o lote for encontrado, validar:
            if validar_lote(value_lote) is not None:
                if value_quantidade != '':
                    try:
                        # Se quantidade estiver correta, executa:
                        if int(value_quantidade) > 0:
                            return True
                    # Se ao tentar comparar quantidade com int resultar em erro, não será aceito
                    except ValueError:
                        return False
            else:
                # Se for preenchido, mas com lote invalido, não será aceito
                return False
                print('nao obrigatorio, prebchdio, lote nao encontrado')

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


def validarOrdem(numeroOrdem=None):
    # cria a conexão com o banco de dados
    conn = sqlite3.connect('Banco_de_dados/estoque.db')

    # cria o cursor
    cursor = conn.cursor()

    # lista de nomes
    nomes = [numeroOrdem]

    # cria a query SQL usando a cláusula IN e um loop for
    query = "SELECT * FROM criar_ordem_producao WHERE numero_Ordem IN ({})".format(', '.join(['?'] * len(nomes)))

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

    if categoria == 'Válvula':
        categoria = 'Tampa'

    return categoria