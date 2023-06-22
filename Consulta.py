from PySimpleGUI import PySimpleGUI as sg
from layout import consulta
from Banco_de_dados.consultar_tabela import consultar_por_lote, buscar_ordem_producao, \
    consultar_por_materia_prima, buscar_produto_acabado, VerificarQuantEstoque, consultarLotePorOrdemDeProducao as lpop
from layout import tela_consulta
from Validar_lote import validar_ordem_producao, validar_lote, verificar_produto_lote



# funcao para abrir menu de consultas
def Consulta():
    # criando a janela de consutlas - com base no import do layout
    janela = consulta()

    def textoConsultaOrdemProducao(info):

        lista_organizada_produto = []
        lista_organizada_lote = []
        lista_organizada_quantidade = []

        texto_total = ''

        for organizar in range(6):

            if info[0][4 + organizar] != '':
                lista_organizada_produto.append(info[0][4 + organizar])
                quantLote = lpop(info[0][2])
                lista_organizada_lote.append(quantLote[organizar][5])
                lista_organizada_quantidade.append(quantLote[organizar][3])


                texto_usuario= f'\nProduto {organizar+1} usado:   {info[0][4 + organizar]}' \
                                f'\nLote usado: {quantLote[organizar][5]}' \
                                f'\nQuantidade: {quantLote[organizar][3]} \n'

                texto_total += texto_usuario




        return texto_total



    # Criar loop para leitura de eventos
    while True:
        window,event,values = sg.read_all_windows()
        # Quando a janela é fechada ou processo cancelado
        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            break

        if event == 'Voltar':
            janela.close()
            return 'Voltar'

        if event == 'OK':

            if values['Por lote do fornecedor'] != '':
                if validar_lote(values['Por lote do fornecedor']) != None:
                    consultar_por_lote(values['Por lote do fornecedor'])

                else:
                    sg.popup('Lote nao encontrado')

            elif values['Por ordem de producao'] != '':

                if validar_ordem_producao(values['Por ordem de producao']) != None:

                    # criando a janela de consutlas - com base no import do layout
                    janela2 = tela_consulta()

                    info = buscar_ordem_producao(values['Por ordem de producao'])

                    texto_usuario = f'\nProduto Acabado: {info[0][1]}' \
                                    f'\nNumero da Ordem: {info[0][2]}' \
                                    f'\nQuantidade Fab:  {info[0][3]}\n' \
                                    f'{textoConsultaOrdemProducao(info)}'\
                                    f'\n Data da ordem: {info[0][10]}'

                    janela2['texto_da_consulta'].update(texto_usuario)

                    # Criar loop para leitura de eventos
                    while True:
                        window, event, values = sg.read_all_windows()
                        # Quando a janela é fechada ou processo cancelado
                        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
                            break
                        if event == 'Voltar' or event == 'OK':
                            janela2.close()
                            break

                    # fechando menu de consultas
                    janela2.close()

                else:
                    sg.popup('Ordem nao encontrado')

            elif values['Por Materia Prima'] != '' and values['Por Materia Prima'] != 'selecionar':
                try:
                    consultar_por_materia_prima(values['Por Materia Prima'])
                except IndexError:
                    sg.popup('Materia prima sem lançamento')

            elif values['Por Produto Acabado'] != '' and values['Por Produto Acabado'] != 'selecionar':
                try:
                    buscar_produto_acabado(values['Por Produto Acabado'])
                except IndexError:
                    sg.popup('Produto Acabado nao encontrado')

    # fechando menu de consultas
    janela.close()


