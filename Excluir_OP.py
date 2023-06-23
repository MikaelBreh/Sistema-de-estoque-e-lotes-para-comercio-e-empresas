from PySimpleGUI import PySimpleGUI as sg
from layout import Excluir
from Validar_lote import validar_ordem_producao
from login_adm import login_ADM
from Banco_de_dados.excluiLinha_SQL import Excluir_linha_SQL
from layout import tela_consulta
from Banco_de_dados.consultar_tabela import buscar_ordem_producao, consultarLotePorOrdemDeProducao as lpop


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

            texto_usuario = f'\nProduto {organizar + 1} usado:   {info[0][4 + organizar]}' \
                            f'\nLote usado: {quantLote[organizar][5]}' \
                            f'\nQuantidade: {quantLote[organizar][3]} \n'

            texto_total += texto_usuario

    return texto_total

def excluir_OP():
    # Criar a janela inicial de login
    janela1 = Excluir()

    janela1['Excluir'].update(disabled=True)

    # Criar loop para leitura de eventos
    while True:
        window,event,values = sg.read_all_windows()
        # Quando a janela é fechada ou processo cancelado
        if event == sg.WINDOW_CLOSED or event == 'Voltar':
            janela1.close()
            break

        if event == 'Conferencia':
            if values['Lote'] != '' and\
            validar_ordem_producao(values['Lote']) is not None:

                janela1['Excluir'].update(disabled=False)

                # criando a janela de consutlas - com base no import do layout
                janela2 = tela_consulta()

                info = buscar_ordem_producao(values['Lote'])

                texto_usuario = f'\nProduto Acabado: {info[0][1]}' \
                                f'\nNumero da Ordem: {info[0][2]}' \
                                f'\nQuantidade Fab:  {info[0][3]}\n' \
                                f'{textoConsultaOrdemProducao(info)}' \
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
                sg.popup('Lote Não encontrado')
                janela1['Excluir'].update(disabled=True)


        elif event == 'Excluir':
            permitirExcluir = login_ADM()
            if permitirExcluir:
                print('usuario pode excluir')
                Excluir_linha_SQL('criar_ordem_producao', 'numero_Ordem', values['Lote'], True)


    janela1.close()