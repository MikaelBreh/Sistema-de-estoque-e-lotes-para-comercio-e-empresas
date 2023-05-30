import sqlite3
from prettytable import PrettyTable
import tkinter as tk
import tkinter.ttk as ttk
from Listas import valores


def converterTuplaInt(tupla):
    tuplaConvertida = int(''.join(map(str, tupla)))
    return tuplaConvertida

# Criar uma funcao que vai receber um lote e retornar informacoes de saida dele
def consultar_por_lote(lote):

    # Procurar um lote na tabela de entrada (entrada_materias_primas)
    # Abrir conexao com o sqlite estoque
    banco = sqlite3.connect('Banco_de_dados/estoque.db')
    # Definir o cursor para mexer na tabela entrada_materias_primas
    cursor_entrada_mat_prima = banco.cursor()

    numeroLote = f"'{lote}'"
    # selecionamos a tabela e vamos procurar o lote que foi colocado na funcao
    cursor_entrada_mat_prima.execute(f"SELECT * FROM entrada_materias_primas WHERE lote={numeroLote}")
    # retornamos todos os valores encontrados para dentro de rows
    t_janela = cursor_entrada_mat_prima.fetchall()
    # Fechar conexao
    banco.close()

    # Formatar titulo da janela
    titulo_janela = {f'Materia Prima: {t_janela[0][2]}  |   Quantidade:  {t_janela[0][3]}   |'
                     f'  Lote:  {t_janela[0][4]}  |  Fornecedor:  {t_janela[0][1]}  |  Data:  {t_janela[0][5]}'
                     f'  |   Estoque Atual:  {VerificarQuantEstoque(lote)}'}


    # Conectar com o bando de dados
    banco = sqlite3.connect('Banco_de_dados/estoque.db')
    # Criar o cursor que vai executar
    cursor = banco.cursor()
    # Executar consulta SQL
    cursor.execute(
        f"SELECT * FROM criar_ordem_producao WHERE lote_1={numeroLote} or lote_2={numeroLote} or lote_3={numeroLote} or lote_4={numeroLote}")
    # Obter resultados
    results = cursor.fetchall()
    # Criar tabela
    table = PrettyTable()
    table.field_names = [i[0] for i in cursor.description]  # Obter nomes das colunas


    # Adicionar linhas da consulta do lote à tabela
    for row in results:
        table.add_row(row)

    # aqui criamos os nomes das colunas que serao exibidos
    table.field_names = ["ID", "Saida  -  Produto Acabado", "Numero Ordem", "Quantidade",
                         "Lote 1", "Lote 2", "Lote 3", "Lote 4", "Data", ]


    janela = tk.Tk()
    janela.title(titulo_janela)

    texto = tk.Text(janela, width=150, height=100)
    texto.pack()

    texto.insert(tk.END, table.get_string())

    # Imprimir tabela
    return table



# essa parte do codigo vai mostrar as informacoes de entrada e saida de um lote
def consultar_por_materia_prima(nomeMateriaPrima):

    def abrirBancoDeDados():
        bancoDeDados = sqlite3.connect('Banco_de_dados/estoque.db')
        return bancoDeDados

    def consultarBancoDeDados(bancoDeDados ,colunaDeRetorno, nometabela1, colunaDeConsulta, parametroConsulta):
        cursor = bancoDeDados.cursor()
        cursor.execute(f"SELECT {colunaDeRetorno} FROM {nometabela1} WHERE {colunaDeConsulta}='{parametroConsulta}'")
        return cursor.fetchall()

    def consultarLotesBancoDados(bancoDeDados, parametrosLote):
        cursor = bancoDeDados.cursor()
        matrizSaida = []

        for lotes in range(verificarComprimentoLista(parametrosLote)):
            cursor.execute(f"SELECT * FROM criar_ordem_producao WHERE lote_1='{parametrosLote[lotes][4]}' " \
                                       f"or lote_2='{parametrosLote[lotes][4]}' or lote_3='{parametrosLote[lotes][4]}' " \
                                       f"or lote_4='{parametrosLote[lotes][4]}'")

            lotesSaida = cursor.fetchall()
            matrizSaida.append(lotesSaida)

        return matrizSaida

    def fecharBancoDeDados(bancoDeDados):
        bancoDeDados.close()

    def verificarComprimentoLista(lista):
        return len(lista)

    def criarMatriz(dadosEmLista, entrada=True):

        matrizPrincipal = []
        if entrada == True:
            quantidadesItens = verificarComprimentoLista(dadosEmLista[0])
            quantidadeLinhas = verificarComprimentoLista(dadosEmLista)
            for linhas in range(quantidadeLinhas):
                matrizSecundaria = []
                for itens in range(quantidadesItens):
                    matrizSecundaria.append(dadosEmLista[linhas][itens])
                    print(dadosEmLista[linhas][itens])
                matrizSecundaria.append(VerificarQuantEstoque(dadosEmLista[linhas][4]))
                matrizPrincipal.append(matrizSecundaria)

        else:

            matrizPrincipal = []
            for tamanho_lista in range(verificarComprimentoLista(dadosEmLista)): #tamanho da primeira lista = 2
                for encontrarNasListas in range(verificarComprimentoLista(dadosEmLista[tamanho_lista])): # tamanho da primeira e segunda 5 e 2
                    matrizSecundaria = []
                    for itens in range(verificarComprimentoLista(dadosEmLista[tamanho_lista][encontrarNasListas])):
                        matrizSecundaria.append(dadosEmLista[tamanho_lista][encontrarNasListas][itens])
                    matrizPrincipal.append(matrizSecundaria)







        return matrizPrincipal

    def janelaTkinter(matrizEntrada, matrizSaida):

        janela = tk.Tk()
        janela.title("tabela1")

        # --------- Inicio tabela 1 ----------
        # Criar um widget Treeview
        tabela1 = ttk.Treeview(janela)

        altura_linha = 15  # Defina a altura desejada das linhas
        tabela1.configure(height=altura_linha)

        # Definir as colunas
        tabela1['columns'] = ('Coluna 0', 'Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4', 'Coluna 5', 'Coluna 6')

        # Formatar as colunas
        tabela1.column('#0', width=0, stretch=False)
        tabela1.column('Coluna 0', width=50)
        tabela1.column('Coluna 1', width=250)
        tabela1.column('Coluna 2', width=300)
        tabela1.column('Coluna 3', width=120)
        tabela1.column('Coluna 4', width=120)
        tabela1.column('Coluna 5', width=120)
        tabela1.column('Coluna 6', width=170)

        # Definir os cabeçalhos das colunas
        tabela1.heading('#0', text='ID')
        tabela1.heading('Coluna 0', text='Id')
        tabela1.heading('Coluna 1', text='Fornecedor')
        tabela1.heading('Coluna 2', text='Materia Prima')
        tabela1.heading('Coluna 3', text='Quantidade')
        tabela1.heading('Coluna 4', text='Lote')
        tabela1.heading('Coluna 5', text='Data')
        tabela1.heading('Coluna 6', text='Estoque Atual')

        for i, item in enumerate(matrizEntrada):
            tabela1.insert(parent='', index='end', iid=i, text=str(i), values=item)
            tabela1.tag_configure('risco', background='black')  # Configurar a cor do risco
            # tabela1.insert('', 'end', values=['', '', '', ''], tags=('risco',))
        tabela1.pack()
        # --------- Fim tabela 1 ----------


        # --------- Inicio tabela 2 ----------
        # Criar um widget Treeview
        tabela2 = ttk.Treeview(janela)

        altura_linha = 40  # Defina a altura desejada das linhas
        tabela2.configure(height=altura_linha)

        # Definir as colunas
        tabela2['columns'] = ('Coluna 0', 'Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4', 'Coluna 5',
                              'Coluna 6', 'Coluna 7', 'Coluna 8')

        # Formatar as colunas
        tabela2.column('#0', width=0, stretch=False)
        tabela2.column('Coluna 0', width=35)
        tabela2.column('Coluna 1', width=300)
        tabela2.column('Coluna 2', width=120)
        tabela2.column('Coluna 3', width=100)
        tabela2.column('Coluna 4', width=120)
        tabela2.column('Coluna 5', width=120)
        tabela2.column('Coluna 6', width=120)
        tabela2.column('Coluna 7', width=120)
        tabela2.column('Coluna 8', width=90)



        # Definir os cabeçalhos das colunas
        tabela2.heading('#0', text='ID')
        tabela2.heading('Coluna 0', text='Id')
        tabela2.heading('Coluna 1', text='Produto')
        tabela2.heading('Coluna 2', text='Numero Ordem')
        tabela2.heading('Coluna 3', text='Quantidade')
        tabela2.heading('Coluna 4', text='Lote 1')
        tabela2.heading('Coluna 5', text='Lote 2')
        tabela2.heading('Coluna 6', text='Lote 3')
        tabela2.heading('Coluna 7', text='Lote 4')
        tabela2.heading('Coluna 8', text='Data')


        for i, item in enumerate(matrizSaida):
            tabela2.insert(parent='', index='end', iid=i, text=str(i), values=item)
        tabela2.pack()
        # --------- Fim tabela 2 ----------

        janela.mainloop()


    bancoDeDados = abrirBancoDeDados()
    correspondenciaEntrada = consultarBancoDeDados(bancoDeDados ,'*', 'entrada_materias_primas', 'produto', nomeMateriaPrima)

    correspondenciaSaida = consultarLotesBancoDados(bancoDeDados, correspondenciaEntrada)
    fecharBancoDeDados(bancoDeDados)
    matrizSaida = criarMatriz(correspondenciaSaida, False)

    matrizEntrada = criarMatriz(correspondenciaEntrada)
    janelaTkinter(matrizEntrada, matrizSaida)



def buscar_ordem_producao(lote):
    # Procurar um lote na tabela de entrada (entrada_materias_primas)
    # Abrir conexao com o sqlite estoque
    banco = sqlite3.connect('Banco_de_dados/estoque.db')
    # Definir o cursor para mexer na tabela entrada_materias_primas
    cursor_entrada_mat_prima = banco.cursor()
    # selecionamos a tabela e vamos procurar o lote que foi colocado na funcao
    cursor_entrada_mat_prima.execute(f"SELECT * FROM criar_ordem_producao WHERE numero_Ordem={lote}")
    # retornamos todos os valores encontrados para dentro de rows
    info = cursor_entrada_mat_prima.fetchall()
    # Fechar conexao
    banco.close()

    return info



def buscar_produto_acabado(produto):
    produto = str(produto)
    # Procurar um lote na tabela de saida (criar_ordem_producao)
    # Abrir conexao com o sqlite estoque
    banco = sqlite3.connect('Banco_de_dados/estoque.db')
    # Definir o cursor para mexer na tabela entrada_materias_primas
    cursor_saida_ordem = banco.cursor()
    # selecionamos a tabela e vamos procurar o lote que foi colocado na funcao
    cursor_saida_ordem.execute(f"SELECT * FROM criar_ordem_producao WHERE produto='{produto}'")
    # retornamos todos os valores encontrados para dentro de rows
    info = cursor_saida_ordem.fetchall()
    # Fechar conexao
    banco.close()

    # segunda tabela - saida da materia prima selecionada
    # Criar tabela
    table1 = PrettyTable()
    table1.field_names = [i[0] for i in cursor_saida_ordem.description]  # Obter nomes das colunas

    # Adicionar linhas da consulta do lote à tabela
    for row in info:
        table1.add_row(row)

    # aqui criamos os nomes das colunas que serao exibidos
    table1.field_names = ["ID", "Entrada  -  Produto Acabado", "Numero Ordem", "Quantidade",
                          "Lote 1", "Lote 2", "Lote 3", "Lote 4", "Data", ]

    # criaca da janela que vai exbibir as duas tabelas: entrada e saida
    janela = tk.Tk()
    janela.title('Pesquisa por produto acabado')

    texto = tk.Text(janela, width=150, height=100)
    texto.pack()

    # tabela da saida da materia prima selecionada
    texto.insert(tk.END, "\n\nSaida da materia prima:\n")
    texto.insert(tk.END, table1.get_string())

    # abrir a janela do tkinter
    janela.mainloop()


def VerificarQuantEstoque(lote):
    # Procurar um lote na tabela de entrada (entrada_materias_primas)
    # Abrir conexao com o sqlite estoque
    banco = sqlite3.connect('Banco_de_dados/estoque.db')
    # Definir o cursor para mexer na tabela entrada_materias_primas
    cursor_entrada_mat_prima = banco.cursor()
    # selecionamos a tabela e vamos procurar o lote que foi colocado na funcao
    cursor_entrada_mat_prima.execute(f"SELECT quantidade FROM entrada_materias_primas WHERE lote='{lote}'")
    # retornamos todos os valores encontrados para dentro de rows
    t_janela = cursor_entrada_mat_prima.fetchall()
    # Fechar conexao
    banco.close()

    # Atribuimos aqui a quantidade original da materia prima. Ex: chegou do fornecedor 2000 garrafas
    quantLote = t_janela[0]

    # Conectar com o bando de dados
    banco = sqlite3.connect('Banco_de_dados/estoque.db')
    # Criar o cursor que vai executar
    cursor = banco.cursor()
    # Executar consulta SQL
    cursor.execute(
        f"SELECT quantidade FROM criar_ordem_producao WHERE lote_1='{lote}' or lote_2='{lote}' or lote_3='{lote}' or lote_4='{lote}'")
    # Obter resultados
    results = cursor.fetchall()
    # Criar tabela
    table = PrettyTable()
    table.field_names = [i[0] for i in cursor.description]  # Obter nomes das colunas

    quantSaidas = 0


    for quantItens in range(len(results)):
        quantSaidas += converterTuplaInt(results[quantItens])

    quantidadeEstoque = converterTuplaInt(quantLote) - quantSaidas

    return quantidadeEstoque



def consultar_entrada_matPrima(nome_materia):
    # Procurar um lote na tabela de entrada (entrada_materias_primas)
    # Abrir conexao com o sqlite estoque
    banco = sqlite3.connect('Banco_de_dados/estoque.db')
    # Definir o cursor para mexer na tabela entrada_materias_primas
    cursor_entrada_mat_prima = banco.cursor()
    # selecionamos a tabela e vamos procurar o lote que foi colocado na funcao
    cursor_entrada_mat_prima.execute(f"SELECT quantidade FROM entrada_materias_primas WHERE produto='{nome_materia}'")
    # retornamos todos os valores encontrados para dentro de rows
    t_janela = cursor_entrada_mat_prima.fetchall()
    # Fechar conexao
    banco.close()

    return t_janela


def consultar_saida_matPrima(lote):
    # Procurar um lote na tabela de entrada (entrada_materias_primas)
    # Abrir conexao com o sqlite estoque
    banco = sqlite3.connect('Banco_de_dados/estoque.db')
    # Definir o cursor para mexer na tabela entrada_materias_primas
    cursor_entrada_mat_prima = banco.cursor()
    # selecionamos a tabela e vamos procurar o lote que foi colocado na funcao
    cursor_entrada_mat_prima.execute(
        f"SELECT quantidade FROM criar_ordem_producao WHERE lote_1={lote} or lote_2={lote} or lote_3={lote} or lote_4={lote}")
    # Obter resultados
    t_janela = cursor_entrada_mat_prima.fetchall()
    # Fechar conexao
    banco.close()
    return t_janela


def TranfNomeEmLote(nome_materia):
    # Procurar um lote na tabela de entrada (entrada_materias_primas)
    # Abrir conexao com o sqlite estoque
    banco = sqlite3.connect('Banco_de_dados/estoque.db')
    # Definir o cursor para mexer na tabela entrada_materias_primas
    cursor_entrada_mat_prima = banco.cursor()
    # selecionamos a tabela e vamos procurar o lote que foi colocado na funcao
    cursor_entrada_mat_prima.execute(f"SELECT lote FROM entrada_materias_primas WHERE produto='{nome_materia}'")
    # retornamos todos os valores encontrados para dentro de rows
    t_janela = cursor_entrada_mat_prima.fetchall()
    # Fechar conexao
    banco.close()

    return t_janela


def abrirTelaEstoque():
    janela = tk.Tk()
    janela.title("Tabela")

    # Criar um widget Treeview
    tabela = ttk.Treeview(janela)

    altura_linha = 40  # Defina a altura desejada das linhas
    tabela.configure(height=altura_linha)

    # Definir as colunas
    tabela['columns'] = ('Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4')

    # Formatar as colunas
    tabela.column('#0', width=0, stretch=False)
    tabela.column('Coluna 1', width=400)
    tabela.column('Coluna 2', width=120)
    tabela.column('Coluna 3', width=120)
    tabela.column('Coluna 4', width=120)

    # Definir os cabeçalhos das colunas
    tabela.heading('#0', text='ID')
    tabela.heading('Coluna 1', text='Produto')
    tabela.heading('Coluna 2', text='Entrada')
    tabela.heading('Coluna 3', text='Saida')
    tabela.heading('Coluna 4', text='Estoque')

    valor = 10

    matriz = []

    for nome_produto in range(len(valores)):
        listas = []
        listas.append(valores[nome_produto])
        listas.append(consultar_entrada_matPrima(valores[nome_produto]))
        # listas.append(consultar_saida_matPrima(valores[nome_produto]))
        matriz.append(listas)

    matriz2 = []
    for linhas in range(len(matriz)):
        listas2 = []
        soma = 0
        soma2 = 0
        lotes_do_produto = TranfNomeEmLote(valores[linhas])

        for itens_linhas in range(len(matriz[linhas][1])):
            soma += converterTuplaInt(matriz[linhas][1][itens_linhas])

        for lote_para_quantidade in range(len(lotes_do_produto)):
            quantidades = consultar_saida_matPrima(lotes_do_produto[lote_para_quantidade][0])
            for quantidade_unitaria in range(len(quantidades)):
                soma2 += quantidades[quantidade_unitaria][0]

        listas2.append(matriz[linhas][0])
        listas2.append(soma)
        listas2.append(soma2)
        listas2.append(soma - soma2)

        matriz2.append(listas2)

    dados = matriz2

    for i, item in enumerate(dados):
        tabela.insert(parent='', index='end', iid=i, text=str(i), values=item)
        tabela.tag_configure('risco', background='black')  # Configurar a cor do risco
        # tabela.insert('', 'end', values=['', '', '', ''], tags=('risco',))

    tabela.pack()

    janela.mainloop()





