import sqlite3


def insert_data_entrada( nome_tabela ,fornecedor, produto, quantidade, lote, data):
    banco = sqlite3.connect('Banco_de_dados/estoque.db')
    cursor = banco.cursor()
    cursor.execute(
        f"INSERT INTO {nome_tabela} (fornecedor, produto, quantidade, lote, data) VALUES ( ?, ?, ?, ?, ?)",
        (fornecedor, produto, quantidade, lote, data))
    banco.commit()
    banco.close()

def insert_data_ordem(produto, numero_Ordem, quantidade, lote_1, lote_2, lote_3, lote_4, data):
    banco = sqlite3.connect('Banco_de_dados/estoque.db')
    cursor = banco.cursor()
    cursor.execute(
        f"INSERT INTO criar_ordem_producao (produto, numero_Ordem, quantidade, lote_1, lote_2, lote_3, lote_4, data) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (produto, numero_Ordem, quantidade, lote_1, lote_2, lote_3, lote_4, data))
    banco.commit()
    banco.close()

