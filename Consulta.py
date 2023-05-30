from PySimpleGUI import PySimpleGUI as sg
from layout import consulta
from Banco_de_dados.consultar_tabela import consultar_por_lote, buscar_ordem_producao, \
    consultar_por_materia_prima, buscar_produto_acabado, VerificarQuantEstoque
from layout import tela_consulta
from Validar_lote import validar_ordem_producao, validar_lote, verificar_produto_lote



# funcao para abrir menu de consultas
def Consulta():
    # criando a janela de consutlas - com base no import do layout
    janela = consulta()


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

            if values['Por lote do fornecedor'] != '' and validar_lote(values['Por lote do fornecedor']) != None:
                consultar_por_lote(values['Por lote do fornecedor'])

            if values['Por ordem de producao'] != '':

                if validar_ordem_producao(values['Por ordem de producao']) != None:

                    # criando a janela de consutlas - com base no import do layout
                    janela2 = tela_consulta()

                    info = buscar_ordem_producao(values['Por ordem de producao'])

                    texto_usuario = f'\nProduto Acabado: {info[0][1]}' \
                                    f'\nNumero da Ordem: {info[0][2]}' \
                                    f'\nQuantidade Fab:  {info[0][3]}\n' \
                                    f'\nLote 1 usado:   {info[0][4]} \n' \
                                    f'Produto: {verificar_produto_lote(info[0][4])}\n' \
                                    f'\nLote 2 usado:   {info[0][5]}\n' \
                                    f'Produto: {verificar_produto_lote(info[0][5])}\n' \
                                    f'\nLote 3 usado:   {info[0][6]}\n' \
                                    f'Produto: {verificar_produto_lote(info[0][6])}\n' \
                                    f'\nLote 4 usado:   {info[0][7]}\n' \
                                    f'Produto: {verificar_produto_lote(info[0][7])}\n' \
                                    f'\nData da Ordem:  {info[0][8]}'


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
                    sg.popup('Lote nao encontrado')

            elif values['Por Materia Prima'] != '' and values['Por Materia Prima'] != 'selecionar':
                try:
                    consultar_por_materia_prima(values['Por Materia Prima'])
                except ValueError:
                    sg.popup('Materia prima sem lançamento')

            elif values['Por Produto Acabado'] != '' and values['Por Produto Acabado'] != 'selecionar':
                buscar_produto_acabado(values['Por Produto Acabado'])


    # fechando menu de consultas
    janela.close()


