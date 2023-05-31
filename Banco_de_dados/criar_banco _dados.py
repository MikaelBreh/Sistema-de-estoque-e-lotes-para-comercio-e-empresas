import sqlite3


def bancoEntradaMateriaPrima():
    # conectando-se ao banco de dados
    conexao = sqlite3.connect('estoque.db')

    # criando um objeto cursor
    cursor = conexao.cursor()

    # executando um comando SQL CREATE TABLE
    cursor.execute('''CREATE TABLE entrada_materias_primas
                      (id INTEGER PRIMARY KEY,
                       fornecedor TEXT,
                       produto TEXT,
                       categoria TEXT, 
                       quantidade INTEGER,
                       data TEXT,
                       lote TEXT)''')

    # comitando as alterações
    conexao.commit()

    # fechando a conexão com o banco de dados
    conexao.close()




def bancoCriarOrdemProducao():
    #conectando-se ao banco de dados
    conexao = sqlite3.connect('estoque.db')

    # criando um objeto cursor
    cursor = conexao.cursor()

    # executando um comando SQL CREATE TABLE
    cursor.execute('''CREATE TABLE criar_ordem_producao
                      (id INTEGER PRIMARY KEY,
                       produto TEXT,
                       numero_Ordem TEXT,
                       quantidade INTEGER,
                       mat_prima1 TEXT,
                       mat_prima2 TEXT,
                       mat_prima3 TEXT,
                       mat_prima4 TEXT,
                       mat_prima5 TEXT,
                       mat_prima6 TEXT,
                       data TEXT)''')

    # comitando as alterações
    conexao.commit()

    # fechando a conexão com o banco de dados
    conexao.close()




def bancoSaidaMateriasPrimas():
    #conectando-se ao banco de dados
    conexao = sqlite3.connect('estoque.db')

    # criando um objeto cursor
    cursor = conexao.cursor()

    # executando um comando SQL CREATE TABLE
    cursor.execute('''CREATE TABLE saida_materias_primas
                      (id INTEGER PRIMARY KEY,
                       produto TEXT,
                       categoria TEXT,
                       quantidade INTEGER,
                       numeroOrdem TEXT,
                       lote TEXT,
                       data TEXT)''')

    # comitando as alterações
    conexao.commit()

    # fechando a conexão com o banco de dados
    conexao.close()\

