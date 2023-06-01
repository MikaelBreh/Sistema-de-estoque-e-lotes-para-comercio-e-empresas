import sqlite3
from Banco_de_dados.consultar_tabela import transLoteEmNome
from Validar_lote import verificarCategoriaMatPrima, verificar_produto_lote
from Banco_de_dados.consultar_tabela import transLoteEmNome

def insertEntradaMateriaPrima(nome_tabela, fornecedor, produto, categoria, quantidade, lote, data):
    banco = sqlite3.connect('Banco_de_dados/estoque.db')
    cursor = banco.cursor()
    cursor.execute(
        f"INSERT INTO {nome_tabela} (fornecedor, produto, categoria, quantidade, lote, data) VALUES ( ?, ?, ?, ?, ?, ?)",
        (fornecedor, produto, categoria, quantidade, lote, data))
    banco.commit()
    banco.close()

def insertSaidaMateriaPrima(lotes_QuantidadesEmLista, produto, numero_Ordem, categoria, quantidade, mat_prima1,
                            mat_prima2, mat_prima3, mat_prima4, mat_prima5, mat_prima6, data):

    print(produto, numero_Ordem, categoria, quantidade, mat_prima1,
                            mat_prima2, mat_prima3, mat_prima4, mat_prima5, mat_prima6, data)

    banco = sqlite3.connect('Banco_de_dados/estoque.db')
    cursor = banco.cursor()

    print(produto, numero_Ordem, quantidade, transLoteEmNome(mat_prima1), transLoteEmNome(mat_prima2),
         transLoteEmNome(mat_prima3), transLoteEmNome(mat_prima4), transLoteEmNome(mat_prima5),
         transLoteEmNome(mat_prima6), data)

    cursor.execute(
        f"INSERT INTO criar_ordem_producao (produto, numero_Ordem, quantidade, mat_prima1, mat_prima2,"
        f" mat_prima3, mat_prima4, mat_prima5, mat_prima6, data) "
        f"VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (produto, numero_Ordem, quantidade, transLoteEmNome(mat_prima1), transLoteEmNome(mat_prima2),
         transLoteEmNome(mat_prima3), transLoteEmNome(mat_prima4), transLoteEmNome(mat_prima5),
         transLoteEmNome(mat_prima6), data))

    lotes = lotes_QuantidadesEmLista[0]
    quant = lotes_QuantidadesEmLista[1]

    for lotes_preenchidos in range(len(lotes_QuantidadesEmLista[0])):

        print(verificar_produto_lote(lotes[lotes_preenchidos]),
              verificarCategoriaMatPrima(transLoteEmNome(lotes[lotes_preenchidos])),
              quant[lotes_preenchidos],
              numero_Ordem,
              lotes[lotes_preenchidos],
              data)

        cursor.execute(
            f"INSERT INTO saida_materias_primas (produto, categoria, quantidade, numeroOrdem, lote, data) "
            f"VALUES (?, ?, ?, ?, ?, ?)",
            (verificar_produto_lote(lotes[lotes_preenchidos]),
             verificarCategoriaMatPrima(transLoteEmNome(lotes[lotes_preenchidos])),
             quant[lotes_preenchidos],
             numero_Ordem,
             lotes[lotes_preenchidos],
             data))

    banco.commit()
    banco.close()



