import sqlite3
from prettytable import PrettyTable
import tkinter as tk
import tkinter.ttk as ttk
from General.Listas import valores, estoque_minimo
from Banco_de_dados.Validar_lote import verificarCategoriaMatPrima
from Banco_de_dados.link_tabela import link
import smtplib
from email.message import EmailMessage
from conteudoSensivel.info_email_remetente import *

def converterTuplaInt(tupla):
    tuplaConvertida = int(''.join(map(str, tupla)))
    return tuplaConvertida

# Criar uma funcao que vai receber um lote e retornar informacoes de saida dele
def consultar_por_lote(lote):

    def abrirBancoDeDados():
        bancoDeDados = sqlite3.connect(link)
        return bancoDeDados

    def consultarBancoDeDados(bancoDeDados, colunaDeRetorno, nometabela1, colunaDeConsulta, parametroConsulta):
        cursor = bancoDeDados.cursor()
        cursor.execute(f"SELECT {colunaDeRetorno} FROM {nometabela1} WHERE {colunaDeConsulta}='{parametroConsulta}'")
        return cursor.fetchall()

    def consultarSaidaBancoDeDados(bancoDeDados, parametroConsulta):
        cursor = bancoDeDados.cursor()
        cursor.execute(f"SELECT * FROM saida_materias_primas WHERE lote='{parametroConsulta}'")
        return cursor.fetchall()

    def fecharBancoDeDados(bancoDeDados):
        bancoDeDados.close()

    def verificarComprimentoLista(lista):
        return len(lista)

    def converterTuplaEmString(tupla):
        string = tupla[0][0]
        return string

    def criarMatriz(dadosEmLista, entrada=True):

        matrizPrincipal = []
        if entrada == True:

            quantidadesItens = verificarComprimentoLista(dadosEmLista[0])
            quantidadeLinhas = verificarComprimentoLista(dadosEmLista)

            for linhas in range(quantidadeLinhas):
                matrizSecundaria = []

                for itens in range(quantidadesItens):
                    matrizSecundaria.append(dadosEmLista[linhas][itens])

                matrizSecundaria.append(VerificarQuantEstoque(dadosEmLista[linhas][6]))
                matrizPrincipal.append(matrizSecundaria)


        else:

            matrizPrincipal = []
            for tamanho_lista in range(verificarComprimentoLista(dadosEmLista)):

                matrizSecundaria = []
                for encontrarNasListas in range(verificarComprimentoLista(dadosEmLista[tamanho_lista])):
                    matrizSecundaria.append(dadosEmLista[tamanho_lista][encontrarNasListas])

                matrizSecundaria.append(
                     converterTuplaEmString(consultarBancoDeDados(bancoDeDados, 'produto', 'criar_ordem_producao', 'numero_Ordem',
                                          dadosEmLista[tamanho_lista][4])))
                matrizPrincipal.append(matrizSecundaria)

        return matrizPrincipal

    def janelaTkinter(matrizEntrada, matrizSaida):

        janela = tk.Tk()
        janela.title("Entrada e Saida Materia prima - por numero de Lote")

        # --------- Inicio tabela 1 ----------
        # Criar um widget Treeview
        tabela1 = ttk.Treeview(janela)

        altura_linha = 2  # Defina a altura desejada das linhas
        tabela1.configure(height=altura_linha)

        # Definir as colunas
        tabela1['columns'] = ('Coluna 0', 'Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4', 'Coluna 5', 'Coluna 6', 'Coluna 7')

        # Formatar as colunas
        tabela1.column('#0', width=0, stretch=False)
        tabela1.column('Coluna 0', width=50)
        tabela1.column('Coluna 1', width=250, anchor='center')
        tabela1.column('Coluna 2', width=300, anchor='center')
        tabela1.column('Coluna 3', width=120, anchor='center')
        tabela1.column('Coluna 4', width=120, anchor='center')
        tabela1.column('Coluna 5', width=120, anchor='center')
        tabela1.column('Coluna 6', width=170, anchor='center')
        tabela1.column('Coluna 7', width=170, anchor='center')

        # Definir os cabeçalhos das colunas
        tabela1.heading('#0', text='ID')
        tabela1.heading('Coluna 0', text='Id')
        tabela1.heading('Coluna 1', text='Fornecedor')
        tabela1.heading('Coluna 2', text='Materia Prima')
        tabela1.heading('Coluna 3', text='Categoria')
        tabela1.heading('Coluna 4', text='Quantidade')
        tabela1.heading('Coluna 5', text='Data')
        tabela1.heading('Coluna 6', text='Lote')
        tabela1.heading('Coluna 7', text='Estoque Atual')

        for i, item in enumerate(matrizEntrada):
            tabela1.insert(parent='', index='end', iid=i, text=str(i), values=item)
            tabela1.tag_configure('risco', background='#ffc375')  # Configurar a cor do risco
            tabela1.insert('', 'end', values=['', '', '', ''], tags=('risco',))
        tabela1.pack()
        # --------- Fim tabela 1 ----------


        # --------- Inicio tabela 2 ----------
        # Criar um widget Treeview
        tabela2 = ttk.Treeview(janela)

        altura_linha = 30  # Defina a altura desejada das linhas
        tabela2.configure(height=altura_linha)

        # Definir as colunas
        tabela2['columns'] = ('Coluna 0', 'Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4', 'Coluna 5',
                              'Coluna 6', 'Coluna 7')

        # Formatar as colunas
        tabela2.column('#0', width=0, stretch=False)
        tabela2.column('Coluna 0', width=35)
        tabela2.column('Coluna 1', width=300)
        tabela2.column('Coluna 2', width=120, anchor='center')
        tabela2.column('Coluna 3', width=100, anchor='center')
        tabela2.column('Coluna 4', width=120, anchor='center')
        tabela2.column('Coluna 5', width=120, anchor='center')
        tabela2.column('Coluna 6', width=120, anchor='center')
        tabela2.column('Coluna 7', width=382, anchor='center')




        # Definir os cabeçalhos das colunas
        tabela2.heading('#0', text='ID')
        tabela2.heading('Coluna 0', text='Id')
        tabela2.heading('Coluna 1', text='Materia Prima') # o unico que vem de criar ordem de producao
        tabela2.heading('Coluna 2', text='Categoria')
        tabela2.heading('Coluna 3', text='Quantidade')
        tabela2.heading('Coluna 4', text='Numero da Ordem')
        tabela2.heading('Coluna 5', text='lote')
        tabela2.heading('Coluna 6', text='Data')
        tabela2.heading('Coluna 7', text='Produto feito')


        for i, item in enumerate(matrizSaida):
            tabela2.insert(parent='', index='end', iid=i, text=str(i), values=item)
        tabela2.pack()
        # --------- Fim tabela 2 ----------

        janela.mainloop()

    bancoDeDados = abrirBancoDeDados()
    correspondenciaEntrada = consultarBancoDeDados(bancoDeDados, '*', 'entrada_materias_primas', 'lote', lote)
    correspondenciaSaida = consultarSaidaBancoDeDados(bancoDeDados, lote)
    matrizEntrada = criarMatriz(correspondenciaEntrada)
    matrizSaida = criarMatriz(correspondenciaSaida, False)
    fecharBancoDeDados(bancoDeDados)

    janelaTkinter(matrizEntrada, matrizSaida)


# essa parte do codigo vai mostrar as informacoes de entrada e saida de um lote
def consultar_por_materia_prima(nomeMateriaPrima):
    def abrirBancoDeDados():
        bancoDeDados = sqlite3.connect(link)
        return bancoDeDados

    def consultarProdutoAcabadoOrdem(bancoDeDados, parametroConsulta):
        cursor = bancoDeDados.cursor()
        cursor.execute(f"SELECT produto FROM criar_ordem_producao WHERE numero_Ordem='{parametroConsulta}'")
        return cursor.fetchall()

    def consultarBancoDeDadosEntrada(bancoDeDados, parametroConsulta):
        cursor = bancoDeDados.cursor()
        cursor.execute(f"SELECT * FROM entrada_materias_primas WHERE produto='{parametroConsulta}'")
        return cursor.fetchall()

    def consultarSaidaMateriasPrimas(bancoDeDados, parametrosLote):
        cursor = bancoDeDados.cursor()
        cursor.execute(f"SELECT * FROM saida_materias_primas WHERE produto='{parametrosLote}'")
        saidas = cursor.fetchall()
        if saidas == []:
            none = []
            return none
        else:
            return saidas

    def fecharBancoDeDados(bancoDeDados):
        bancoDeDados.close()

    def verificarComprimentoLista(lista):
        return len(lista)

    def criarMatriz(dadosEmLista, entrada=True):

        matrizPrincipal = []
        if entrada:
            quantidadesItens = verificarComprimentoLista(dadosEmLista[0])
            quantidadeLinhas = verificarComprimentoLista(dadosEmLista)
            for linhas in range(quantidadeLinhas):
                matrizSecundaria = []
                for itens in range(quantidadesItens):
                    matrizSecundaria.append(dadosEmLista[linhas][itens])
                matrizSecundaria.append(VerificarQuantEstoque(dadosEmLista[linhas][6]))
                matrizPrincipal.append(matrizSecundaria)

        else:
            if dadosEmLista == []:
                print('sem dados')
            else:
                quantidadesItens = verificarComprimentoLista(dadosEmLista[0])
                quantidadeLinhas = verificarComprimentoLista(dadosEmLista)
                for linhas in range(quantidadeLinhas):
                    matrizSecundaria = []
                    for itens in range(quantidadesItens):
                        matrizSecundaria.append(dadosEmLista[linhas][itens])
                    matrizSecundaria.append(consultarProdutoAcabadoOrdem(bancoDeDados, dadosEmLista[linhas][4])[0][0])
                    matrizPrincipal.append(matrizSecundaria)

        return matrizPrincipal

    def janelaTkinter(matrizEntrada, matrizSaida):

        janela = tk.Tk()
        janela.title("Consulta de entrada e saida por materias primas")

        # --------- Inicio tabela 1 ----------
        # Criar um widget Treeview
        tabela1 = ttk.Treeview(janela)

        altura_linha = 15  # Defina a altura desejada das linhas
        tabela1.configure(height=altura_linha)

        # Definir as colunas
        tabela1['columns'] = ('Coluna 0', 'Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4', 'Coluna 5', 'Coluna 6', 'Coluna 7')

        # Formatar as colunas
        tabela1.column('#0', width=0, stretch=False)
        tabela1.column('Coluna 0', width=50, anchor='center')
        tabela1.column('Coluna 1', width=190, anchor='center')
        tabela1.column('Coluna 2', width=300, anchor='center')
        tabela1.column('Coluna 3', width=80, anchor='center')
        tabela1.column('Coluna 4', width=140, anchor='center')
        tabela1.column('Coluna 5', width=120, anchor='center')
        tabela1.column('Coluna 6', width=170, anchor='center')
        tabela1.column('Coluna 7', width=80, anchor='center')

        # Definir os cabeçalhos das colunas
        tabela1.heading('#0', text='ID')
        tabela1.heading('Coluna 0', text='Id')
        tabela1.heading('Coluna 1', text='Fornecedor')
        tabela1.heading('Coluna 2', text='Materia Prima')
        tabela1.heading('Coluna 3', text='Categoria')
        tabela1.heading('Coluna 4', text='Quantidade Entrada')
        tabela1.heading('Coluna 5', text='Data')
        tabela1.heading('Coluna 6', text='Lote M.P')
        tabela1.heading('Coluna 7', text='Quant. Atual')


        for i, item in enumerate(matrizEntrada):
            tabela1.insert(parent='', index='end', iid=i, text=str(i), values=item)
        tabela1.pack()
        # --------- Fim tabela 1 ----------

        # --------- Inicio tabela 2 ----------
        # Criar um widget Treeview
        tabela2 = ttk.Treeview(janela)

        altura_linha = 40  # Defina a altura desejada das linhas
        tabela2.configure(height=altura_linha)

        # Definir as colunas
        tabela2['columns'] = ('Coluna 0', 'Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4', 'Coluna 5',
                              'Coluna 6', 'Coluna 7')

        # Formatar as colunas
        tabela2.column('#0', width=0, stretch=False)
        tabela2.column('Coluna 0', width=35, anchor='center')
        tabela2.column('Coluna 1', width=220, anchor='center')
        tabela2.column('Coluna 2', width=80, anchor='center')
        tabela2.column('Coluna 3', width=100, anchor='center')
        tabela2.column('Coluna 4', width=120, anchor='center')
        tabela2.column('Coluna 5', width=120, anchor='center')
        tabela2.column('Coluna 6', width=120, anchor='center')
        tabela2.column('Coluna 7', width=340, anchor='center')

        # Definir os cabeçalhos das colunas
        tabela2.heading('#0', text='ID')
        tabela2.heading('Coluna 0', text='Id')
        tabela2.heading('Coluna 1', text='Materia Prima')
        tabela2.heading('Coluna 2', text='Categoria')
        tabela2.heading('Coluna 3', text='Quantidade')
        tabela2.heading('Coluna 4', text='Numero Ordem')
        tabela2.heading('Coluna 5', text='Lote M.P')
        tabela2.heading('Coluna 6', text='Data')
        tabela2.heading('Coluna 7', text='Produto Acabado Feito')

        for i, item in enumerate(matrizSaida):
            tabela2.insert(parent='', index='end', iid=i, text=str(i), values=item)
        tabela2.pack()
        # --------- Fim tabela 2 ----------

        janela.mainloop()

    bancoDeDados = abrirBancoDeDados()
    correspondenciaEntrada = consultarBancoDeDadosEntrada(bancoDeDados, nomeMateriaPrima)
    print(correspondenciaEntrada)

    matrizEntrada = criarMatriz(correspondenciaEntrada)
    print(f'matriz entrada: {matrizEntrada}')

    correspondeciaSaida = consultarSaidaMateriasPrimas(bancoDeDados, nomeMateriaPrima)
    print(correspondeciaSaida)

    matrizSaida = criarMatriz(correspondeciaSaida, False)
    print(f'matriz saida: {matrizSaida}')

    fecharBancoDeDados(bancoDeDados)
    janelaTkinter(matrizEntrada, matrizSaida)


def buscar_ordem_producao(lote):
    # Procurar um lote na tabela de entrada (entrada_materias_primas)
    # Abrir conexao com o sqlite estoque
    banco = sqlite3.connect(link)
    # Definir o cursor para mexer na tabela entrada_materias_primas
    cursor_entrada_mat_prima = banco.cursor()
    # selecionamos a tabela e vamos procurar o lote que foi colocado na funcao
    cursor_entrada_mat_prima.execute(f"SELECT * FROM criar_ordem_producao WHERE numero_Ordem='{lote}'")
    # retornamos todos os valores encontrados para dentro de rows
    info = cursor_entrada_mat_prima.fetchall()
    # Fechar conexao
    banco.close()

    return info


def consultarLotePorOrdemDeProducao(ordem):

    def abrirBancoDeDados():
        bancoDeDados = sqlite3.connect(link)
        return bancoDeDados

    def consultarBancoDeDados(bancoDeDados, colunaDeRetorno, nometabela1, colunaDeConsulta, parametroConsulta):
        cursor = bancoDeDados.cursor()
        cursor.execute(f"SELECT {colunaDeRetorno} FROM {nometabela1} WHERE {colunaDeConsulta}='{parametroConsulta}'")
        return cursor.fetchall()

    def fecharBancoDeDados(bancoDeDados):
        bancoDeDados.close()


    bancoDeDados = abrirBancoDeDados()
    correspondencia = consultarBancoDeDados(bancoDeDados, '*', 'saida_materias_primas', 'numeroOrdem', ordem)
    fecharBancoDeDados(bancoDeDados)
    return correspondencia


def buscar_produto_acabado(nomeMateriaPrima):

    def abrirBancoDeDados():
        bancoDeDados = sqlite3.connect(link)
        return bancoDeDados

    def consultarProdutoAcabadoOrdem(bancoDeDados):
        cursor = bancoDeDados.cursor()
        cursor.execute(f"SELECT produto, numero_Ordem, quantidade, data FROM criar_ordem_producao WHERE produto='{nomeMateriaPrima}'")
        return cursor.fetchall()

    def consultarSaidaMateriasPrimas(bancoDeDados, parametrosLote):
        cursor = bancoDeDados.cursor()
        cursor.execute(f"SELECT produto, quantidade, lote FROM saida_materias_primas WHERE numeroOrdem='{parametrosLote}'")
        saidas = cursor.fetchall()
        return saidas


    def fecharBancoDeDados(bancoDeDados):
        bancoDeDados.close()

    def verificarComprimentoLista(lista):
        return len(lista)

    def criarMatriz(dadosEmLista, entrada=True):

        matrizPrincipal = []

        quantidadesItens = verificarComprimentoLista(dadosEmLista[0])
        quantidadeLinhas = verificarComprimentoLista(dadosEmLista)

        for linhas in range(quantidadeLinhas):
            matrizSecundaria = []
            for itens in range(quantidadesItens):
                if dadosEmLista[linhas][itens] == nomeMateriaPrima:
                    continue
                else:
                    matrizSecundaria.append(dadosEmLista[linhas][itens])
            saidasLotes = consultarSaidaMateriasPrimas(bancoDeDados, dadosEmLista[linhas][1])

            for quantidadesDeItensUsados in range(verificarComprimentoLista(saidasLotes)):

                for lotes in range(verificarComprimentoLista(saidasLotes[quantidadesDeItensUsados])):
                    matrizSecundaria.append(saidasLotes[quantidadesDeItensUsados][lotes])

            matrizPrincipal.append(matrizSecundaria)
        print(matrizPrincipal)

        return matrizPrincipal


    def janelaTkinter(matrizEntrada):
        janela = tk.Tk()
        janela.title(f"produto: {nomeMateriaPrima}")

        largura_janela = 1300  # Defina a largura desejada da janela
        altura_janela = 600  # Defina a altura desejada da janela

        # Configurar a geometria da janela
        janela.geometry(f"{largura_janela}x{altura_janela}")

        # Criar um canvas
        canvas = tk.Canvas(janela)
        canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Criar uma barra de rolagem horizontal
        scrollbar_horizontal = ttk.Scrollbar(janela, orient=tk.HORIZONTAL, command=canvas.xview)
        scrollbar_horizontal.pack(side=tk.BOTTOM, fill=tk.X)

        # Configurar o canvas para usar a barra de rolagem horizontal
        canvas.configure(xscrollcommand=scrollbar_horizontal.set)

        # Criar um widget Treeview dentro do canvas
        tabela1 = ttk.Treeview(canvas)

        # Definir as colunas, formatá-las e definir os cabeçalhos
        tabela1['columns'] = ('Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4', 'Coluna 5', 'Coluna 6',
                              'Coluna 7', 'Coluna 8', 'Coluna 9', 'Coluna 10', 'Coluna 11', 'Coluna 12', 'Coluna 13',
                              'Coluna 14', 'Coluna 15', 'Coluna 16', 'Coluna 17', 'Coluna 18', 'Coluna 19',
                              'Coluna 20', 'Coluna 21' )
        tabela1.column('#0', width=0, stretch=False)

        # Resto do código para configuração das colunas e cabeçalhos...
        # Formatar as colunas
        tabela1.column('#0', width=0, stretch=False)
        tabela1.column('Coluna 1', width=100, anchor='center')
        tabela1.column('Coluna 2', width=70, anchor='center')
        tabela1.column('Coluna 3', width=90, anchor='center')

        tabela1.column('Coluna 4', width=160, anchor='center')
        tabela1.column('Coluna 5', width=70, anchor='center')
        tabela1.column('Coluna 6', width=80, anchor='center')

        tabela1.column('Coluna 7', width=160, anchor='center')
        tabela1.column('Coluna 8', width=70, anchor='center')
        tabela1.column('Coluna 9', width=80, anchor='center')

        tabela1.column('Coluna 10', width=160, anchor='center')
        tabela1.column('Coluna 11', width=70, anchor='center')
        tabela1.column('Coluna 12', width=80, anchor='center')

        tabela1.column('Coluna 13', width=160, anchor='center')
        tabela1.column('Coluna 14', width=70, anchor='center')
        tabela1.column('Coluna 15', width=80, anchor='center')

        tabela1.column('Coluna 16', width=160, anchor='center')
        tabela1.column('Coluna 17', width=70, anchor='center')
        tabela1.column('Coluna 18', width=80, anchor='center')

        tabela1.column('Coluna 19', width=160, anchor='center')
        tabela1.column('Coluna 20', width=70, anchor='center')
        tabela1.column('Coluna 21', width=80, anchor='center')

        # Definir os cabeçalhos das colunas
        tabela1.heading('#0', text='ID')
        tabela1.heading('Coluna 1', text='Ordem Producao')
        tabela1.heading('Coluna 2', text='Quantidade')
        tabela1.heading('Coluna 3', text='Data')

        tabela1.heading('Coluna 4', text='Materia Prima 1')
        tabela1.heading('Coluna 5', text='Quantidade')
        tabela1.heading('Coluna 6', text='Lote M.P')

        tabela1.heading('Coluna 7', text='Materia Prima 2')
        tabela1.heading('Coluna 8', text='Quantidade')
        tabela1.heading('Coluna 9', text='Lote M.P')

        tabela1.heading('Coluna 10', text='Materia Prima 3')
        tabela1.heading('Coluna 11', text='Quantidade')
        tabela1.heading('Coluna 12', text='Lote M.P')

        tabela1.heading('Coluna 13', text='Materia Prima 4')
        tabela1.heading('Coluna 14', text='Quantidade')
        tabela1.heading('Coluna 15', text='Lote M.P')

        tabela1.heading('Coluna 16', text='Materia Prima 5')
        tabela1.heading('Coluna 17', text='Quantidade')
        tabela1.heading('Coluna 18', text='Lote M.P')

        tabela1.heading('Coluna 19', text='Materia Prima 6')
        tabela1.heading('Coluna 20', text='Quantidade')
        tabela1.heading('Coluna 21', text='Lote M.P')

        altura_linha = 30  # Defina a altura desejada das linhas
        tabela1.configure(height=altura_linha)

        # Definir as cores intercaladas para linhas pares e ímpares
        tabela1.tag_configure('linha_par', background='#808080')
        tabela1.tag_configure('linha_impar', background='')

        # Inserir os dados na tabela
        for i, item in enumerate(matrizEntrada):
            if i % 2 == 0:
                tabela1.insert(parent='', index='end', iid=i, text=str(i), values=item, tags=('linha_par',))
            else:
                tabela1.insert(parent='', index='end', iid=i, text=str(i), values=item, tags=('linha_impar',))

        # Colocar o Treeview dentro do canvas
        tabela1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configurar o canvas para acompanhar o tamanho do Treeview
        tabela1.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

        # Configurar a barra de rolagem do canvas
        canvas.create_window((0, 0), window=tabela1, anchor='nw')
        canvas.configure(scrollregion=canvas.bbox('all'))

        janela.mainloop()

    bancoDeDados = abrirBancoDeDados()

    retornoOrdem = consultarProdutoAcabadoOrdem(bancoDeDados)
    print(retornoOrdem)
    matrizDados = criarMatriz(retornoOrdem)
    janelaTkinter(matrizDados)

    fecharBancoDeDados(bancoDeDados)


def VerificarQuantEstoque(lote):
    # Procurar um lote na tabela de entrada (entrada_materias_primas)
    # Abrir conexao com o sqlite estoque
    banco = sqlite3.connect(link)
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
    banco = sqlite3.connect(link)
    # Criar o cursor que vai executar
    cursor = banco.cursor()
    # Executar consulta SQL
    cursor.execute(
        f"SELECT quantidade FROM saida_materias_primas WHERE lote='{lote}' ")
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
    banco = sqlite3.connect(link)
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
    banco = sqlite3.connect(link)
    # Definir o cursor para mexer na tabela entrada_materias_primas
    cursor_entrada_mat_prima = banco.cursor()
    # selecionamos a tabela e vamos procurar o lote que foi colocado na funcao
    cursor_entrada_mat_prima.execute(
        f"SELECT quantidade FROM saida_materias_primas WHERE lote={lote}")
    # Obter resultados
    t_janela = cursor_entrada_mat_prima.fetchall()
    # Fechar conexao
    banco.close()
    return t_janela


def TranfNomeEmLote(nome_materia):
    # Procurar um lote na tabela de entrada (entrada_materias_primas)
    # Abrir conexao com o sqlite estoque
    banco = sqlite3.connect(link)
    # Definir o cursor para mexer na tabela entrada_materias_primas
    cursor_entrada_mat_prima = banco.cursor()
    # selecionamos a tabela e vamos procurar o lote que foi colocado na funcao
    cursor_entrada_mat_prima.execute(f"SELECT lote FROM entrada_materias_primas WHERE produto='{nome_materia}'")
    # retornamos todos os valores encontrados para dentro de rows
    t_janela = cursor_entrada_mat_prima.fetchall()
    # Fechar conexao
    banco.close()

    return t_janela


# Transformar um lote de materia prima em Nome da materia prima
def transLoteEmNome(lote):
    # Procurar um lote na tabela de entrada (entrada_materias_primas)
    # Abrir conexao com o sqlite estoque
    banco = sqlite3.connect(link)
    # Definir o cursor para mexer na tabela entrada_materias_primas
    cursor_entrada_mat_prima = banco.cursor()
    # selecionamos a tabela e vamos procurar o lote que foi colocado na funcao
    cursor_entrada_mat_prima.execute(f"SELECT produto FROM entrada_materias_primas WHERE lote='{lote}'")
    # retornamos todos os valores encontrados para dentro de rows
    t_janela = cursor_entrada_mat_prima.fetchall()
    # Fechar conexao
    banco.close()

    nomeDoLote = t_janela
    # Se o nome do produto retornar vazio, passe vazio como resultado
    if nomeDoLote == '':
        return ''
    else:
        # Se nome do produto retornar diferente de vazio, tente encontrar o indice
        try:
            nomeDoLote = t_janela[0][0]
            return nomeDoLote
        # Se nao for possivel encontrar o indice, retorne vazio
        except IndexError:
            return ''


def abrirTelaEstoque(categoria='Todos', estoque_Minimo = False):

    # Abrir janela do tkinter
    def janelaTkinter(dados):
        janela = tk.Tk()
        janela.title("Tabela")

        # Criar um widget Treeview
        tabela = ttk.Treeview(janela)

        altura_linha = 40  # Defina a altura desejada das linhas
        tabela.configure(height=altura_linha)

        if estoque_Minimo:
            # Definir as colunas
            tabela['columns'] = ('Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4', 'Coluna 5')

            # Formatar as colunas
            tabela.column('#0', width=0, stretch=False)
            tabela.column('Coluna 1', width=400)
            tabela.column('Coluna 2', width=120)
            tabela.column('Coluna 3', width=120)
            tabela.column('Coluna 4', width=120)
            tabela.column('Coluna 5', width=120)

            # Definir os cabeçalhos das colunas
            tabela.heading('#0', text='ID')
            tabela.heading('Coluna 1', text='Produto')
            tabela.heading('Coluna 2', text='Entrada')
            tabela.heading('Coluna 3', text='Saida')
            tabela.heading('Coluna 4', text='Estoque Atual')
            tabela.heading('Coluna 5', text='Estoque Minimo')

        else:
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
            tabela.heading('Coluna 4', text='Estoque Atual')

        for i, item in enumerate(dados):
            tabela.insert(parent='', index='end', iid=i, text=str(i), values=item)
            tabela.tag_configure('risco', background='black')  # Configurar a cor do risco
            # tabela.insert('', 'end', values=['', '', '', ''], tags=('risco',))

        tabela.pack()

        janela.mainloop()

    # Verifica se usuario filtrou alguma categoria - retorna 'lista Filtrada'
    def consultarFiltragem(categoria):
        if categoria == 'Todos':
            lista_filtrada = valores

        else:
            lista_filtrada = []
            for filtrarCategoria in range(len(valores)):
                if verificarCategoriaMatPrima(valores[filtrarCategoria]) == categoria:
                    lista_filtrada.append(valores[filtrarCategoria])
                else:
                    continue

        return lista_filtrada

    def abrirBancoDeDados():
        banco = sqlite3.connect(link)
        return banco

    def fecharBancoDeDados(bancoDeDados):
        BancoDeDados.close()

    # Consultar a quantidade da entrada do produto procurado
    def consultar_entrada_matPrima(bancoDeDados, nome_materia):
        cursor_entrada_mat_prima = bancoDeDados.cursor()

        cursor_entrada_mat_prima.execute(
            f"SELECT quantidade FROM entrada_materias_primas WHERE produto='{nome_materia}'")
        t_janela = cursor_entrada_mat_prima.fetchall()

        return t_janela

    # Consulta nome e quantidade da entrada de uma materia prima, e retorna os mesmos
    def consultarEntrada(Banco_de_dados ,listaFiltrada):
        lista_nomes_filtrados_entrada = []
        for adicionarNomesFiltrados in range(len(listaFiltrada)):
            nomeeQuantidadeProduto = []
            # aqui vamos adicionar o nome do produto procurado
            nomeeQuantidadeProduto.append(listaFiltrada[adicionarNomesFiltrados])
            # aqui vamos adicionar a quantidade da entrada do produto procurado
            nomeeQuantidadeProduto.append(
                consultar_entrada_matPrima(Banco_de_dados ,listaFiltrada[adicionarNomesFiltrados]))

            lista_nomes_filtrados_entrada.append(nomeeQuantidadeProduto)
        return lista_nomes_filtrados_entrada

    # Procurar todas as quantidades com base no nome do produto passado
    # conexao com banco de dados, so pode encontrar um valor por vez e retornar
    def consultar_saida_matPrima(bancoDeDados, nome_materia):
        cursor_entrada_mat_prima = bancoDeDados.cursor()

        cursor_entrada_mat_prima.execute(
            f"SELECT quantidade FROM saida_materias_primas WHERE produto='{nome_materia}'")

        quantidades = cursor_entrada_mat_prima.fetchall()

        return quantidades

    # Passar valores de ˆˆ consultar_saida_matPrima, ou seja as quantidade de saida
    # Retornar Quantidades somadas da saida de cada um dos itens
    def consultarSaida(bancoDeDados, listaFiltrada):

        lista_quantidade_somada_saidas = []
        for adicionarQuantidadeFiltradas in range(len(listaFiltrada)):
            QuantidadeProduto = []
            quantidadesParaSomar = consultar_saida_matPrima(bancoDeDados,
                                        listaFiltrada[adicionarQuantidadeFiltradas])

            somaTotal = 0
            for somar in range(len(quantidadesParaSomar)):
                somaTotal += quantidadesParaSomar[somar][0]
            lista_quantidade_somada_saidas.append(somaTotal)

        return lista_quantidade_somada_saidas

    def criarMatrizGeral(quantidadeEntrada, quantidadeSaida, listaFiltrada):
        matrizGeral = []
        for organizarItenAIten in range(len(listaFiltrada)):
            matrizSecundaria = []
            matrizSecundaria.append(listaFiltrada[organizarItenAIten])

            if quantidadeEntrada[organizarItenAIten][1] == None:
                matrizSecundaria.append(0)
            else:

                somaTotalEntrada = 0
                for somarEntrada in range(len(quantidadeEntrada[organizarItenAIten][1])):
                    somaTotalEntrada += quantidadeEntrada[organizarItenAIten][1][somarEntrada][0]
                matrizSecundaria.append(somaTotalEntrada)


            if estoque_Minimo:
                if somaTotalEntrada - quantidadeSaida[organizarItenAIten] < estoque_minimo[listaFiltrada[organizarItenAIten]]:
                    matrizSecundaria.append(quantidadeSaida[organizarItenAIten])
                    matrizSecundaria.append(somaTotalEntrada - quantidadeSaida[organizarItenAIten])
                    matrizSecundaria.append(estoque_minimo[listaFiltrada[organizarItenAIten]])

                else:
                    continue

            else:
                matrizSecundaria.append(quantidadeSaida[organizarItenAIten])
                matrizSecundaria.append(somaTotalEntrada - quantidadeSaida[organizarItenAIten])

            matrizGeral.append(matrizSecundaria)

        return matrizGeral


    BancoDeDados = abrirBancoDeDados()
    listaFiltrada= consultarFiltragem(categoria)
    quantidadeEntrada = consultarEntrada(BancoDeDados, listaFiltrada)
    quantidadeSaida = consultarSaida(BancoDeDados, listaFiltrada)
    fecharBancoDeDados(BancoDeDados)

    MatrizGeral = criarMatrizGeral(quantidadeEntrada, quantidadeSaida, listaFiltrada)

    janelaTkinter(MatrizGeral)


def CorpoEmailEstoqueMinimo(categoria='Todos', estoque_Minimo = True):

    # Verifica se usuario filtrou alguma categoria - retorna 'lista Filtrada'
    def consultarFiltragem(categoria):
        if categoria == 'Todos':
            lista_filtrada = valores

        else:
            lista_filtrada = []
            for filtrarCategoria in range(len(valores)):
                if verificarCategoriaMatPrima(valores[filtrarCategoria]) == categoria:
                    lista_filtrada.append(valores[filtrarCategoria])
                else:
                    continue

        return lista_filtrada

    def abrirBancoDeDados():
        banco = sqlite3.connect(link)
        return banco

    def fecharBancoDeDados(bancoDeDados):
        BancoDeDados.close()

    # Consultar a quantidade da entrada do produto procurado
    def consultar_entrada_matPrima(bancoDeDados, nome_materia):
        cursor_entrada_mat_prima = bancoDeDados.cursor()

        cursor_entrada_mat_prima.execute(
            f"SELECT quantidade FROM entrada_materias_primas WHERE produto='{nome_materia}'")
        t_janela = cursor_entrada_mat_prima.fetchall()

        return t_janela

    # Consulta nome e quantidade da entrada de uma materia prima, e retorna os mesmos
    def consultarEntrada(Banco_de_dados ,listaFiltrada):
        lista_nomes_filtrados_entrada = []
        for adicionarNomesFiltrados in range(len(listaFiltrada)):
            nomeeQuantidadeProduto = []
            # aqui vamos adicionar o nome do produto procurado
            nomeeQuantidadeProduto.append(listaFiltrada[adicionarNomesFiltrados])
            # aqui vamos adicionar a quantidade da entrada do produto procurado
            nomeeQuantidadeProduto.append(
                consultar_entrada_matPrima(Banco_de_dados ,listaFiltrada[adicionarNomesFiltrados]))

            lista_nomes_filtrados_entrada.append(nomeeQuantidadeProduto)
        return lista_nomes_filtrados_entrada

    # Procurar todas as quantidades com base no nome do produto passado
    # conexao com banco de dados, so pode encontrar um valor por vez e retornar
    def consultar_saida_matPrima(bancoDeDados, nome_materia):
        cursor_entrada_mat_prima = bancoDeDados.cursor()

        cursor_entrada_mat_prima.execute(
            f"SELECT quantidade FROM saida_materias_primas WHERE produto='{nome_materia}'")

        quantidades = cursor_entrada_mat_prima.fetchall()

        return quantidades

    # Passar valores de ˆˆ consultar_saida_matPrima, ou seja as quantidade de saida
    # Retornar Quantidades somadas da saida de cada um dos itens
    def consultarSaida(bancoDeDados, listaFiltrada):

        lista_quantidade_somada_saidas = []
        for adicionarQuantidadeFiltradas in range(len(listaFiltrada)):
            QuantidadeProduto = []
            quantidadesParaSomar = consultar_saida_matPrima(bancoDeDados,
                                        listaFiltrada[adicionarQuantidadeFiltradas])

            somaTotal = 0
            for somar in range(len(quantidadesParaSomar)):
                somaTotal += quantidadesParaSomar[somar][0]
            lista_quantidade_somada_saidas.append(somaTotal)

        return lista_quantidade_somada_saidas

    def criarMatrizGeral(quantidadeEntrada, quantidadeSaida, listaFiltrada):
        matrizGeral = []
        for organizarItenAIten in range(len(listaFiltrada)):
            matrizSecundaria = []
            matrizSecundaria.append(listaFiltrada[organizarItenAIten])

            if quantidadeEntrada[organizarItenAIten][1] == None:
                matrizSecundaria.append(0)
            else:

                somaTotalEntrada = 0
                for somarEntrada in range(len(quantidadeEntrada[organizarItenAIten][1])):
                    somaTotalEntrada += quantidadeEntrada[organizarItenAIten][1][somarEntrada][0]
                matrizSecundaria.append(somaTotalEntrada)


            if estoque_Minimo:
                if somaTotalEntrada - quantidadeSaida[organizarItenAIten] < estoque_minimo[listaFiltrada[organizarItenAIten]]:
                    matrizSecundaria.append(quantidadeSaida[organizarItenAIten])
                    matrizSecundaria.append(somaTotalEntrada - quantidadeSaida[organizarItenAIten])
                    matrizSecundaria.append(estoque_minimo[listaFiltrada[organizarItenAIten]])

                else:
                    continue

            else:
                matrizSecundaria.append(quantidadeSaida[organizarItenAIten])
                matrizSecundaria.append(somaTotalEntrada - quantidadeSaida[organizarItenAIten])

            matrizGeral.append(matrizSecundaria)

        return matrizGeral


    BancoDeDados = abrirBancoDeDados()
    listaFiltrada= consultarFiltragem(categoria)
    quantidadeEntrada = consultarEntrada(BancoDeDados, listaFiltrada)
    quantidadeSaida = consultarSaida(BancoDeDados, listaFiltrada)
    fecharBancoDeDados(BancoDeDados)

    MatrizGeral = criarMatrizGeral(quantidadeEntrada, quantidadeSaida, listaFiltrada)


    string_total = ''
    for itens in range(len(MatrizGeral)):
        string = f'Produto: {MatrizGeral[itens][0]},    Estoque Atual: {MatrizGeral[itens][3]},    ' \
                 f'Estoque Minimo: {MatrizGeral[itens][4]}\n\n'
        string_total += string

    return string_total


def enviar_email_estoque_minimo():
    # criando email
    msg = EmailMessage()
    msg['Subject'] = f'Estoque Minimo do dia' # assunto do email
    msg['From'] = EMAIL_ADDRESS  # remetente
    msg['To'] = 'mikael@milmilhasautomotivos.com.br'  # email do destinatario
    msg.set_content(CorpoEmailEstoqueMinimo())

    # Enviar Email
    with smtplib.SMTP_SSL(servidor_smtps, porta_smtp) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print('email de estoque minimo enviado')



