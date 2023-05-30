import sqlite3

# # conectando-se ao banco de dados
# conexao = sqlite3.connect('estoque.db')
#
# # criando um objeto cursor
# cursor = conexao.cursor()
#
# # executando um comando SQL CREATE TABLE
# cursor.execute('''CREATE TABLE entrada_materias_primas
#                   (id INTEGER PRIMARY KEY,
#                    fornecedor TEXT,
#                    produto TEXT,
#                    quantidade INTEGER,
#                    data TEXT,
#                    lote TEXT)''')
#
# # comitando as alterações
# conexao.commit()
#
# # fechando a conexão com o banco de dados
# conexao.close()





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
                   lote_1 TEXT,
                   lote_2 TEXT,
                   lote_3 TEXT,
                   lote_4 TEXT,
                   data TEXT)''')

# comitando as alterações
conexao.commit()

# fechando a conexão com o banco de dados
conexao.close()