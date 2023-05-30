import sqlite3

# Conectando ao banco de dados SQLite
conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()

# Executando uma consulta para recuperar os dados
cursor.execute('SELECT * FROM criar_ordem_producao')

# Obtendo os nomes das colunas da tabela
colunas = [description[0] for description in cursor.description]

# Obtendo os dados retornados pela consulta
dados = cursor.fetchall()

# Imprimindo os dados como uma tabela
print('|'.join(colunas))  # Imprime os nomes das colunas separados por '|'

for linha in dados:
    print('|'.join(str(valor) for valor in linha))  # Imprime cada linha separada por '|'

# Fechando a conexão com o banco de dados
conn.close()
