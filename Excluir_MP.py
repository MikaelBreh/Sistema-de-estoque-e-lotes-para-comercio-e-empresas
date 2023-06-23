from PySimpleGUI import PySimpleGUI as sg
from layout import Excluir
from Banco_de_dados.consultar_tabela import consultar_por_lote
from Validar_lote import validarEntradaLote
from login_adm import login_ADM
from Banco_de_dados.excluiLinha_SQL import Excluir_linha_SQL


def excluir_MP():
    # Criar a janela inicial de login
    janela1 = Excluir()

    janela1['Excluir'].update(disabled=True)

    # Criar loop para leitura de eventos
    while True:
        window,event,values = sg.read_all_windows()
        # Quando a janela é fechada ou processo cancelado
        if event == sg.WINDOW_CLOSED or event == 'Voltar':
            janela1.close()
            return False
            break

        if event == 'Conferencia':
            if values['Lote'] != '' and\
            validarEntradaLote(values['Lote'], 1, True):

                janela1['Excluir'].update(disabled=False)
                consultar_por_lote(values['Lote'])

            else:
                sg.popup('Lote Não encontrado')
                janela1['Excluir'].update(disabled=True)


        elif event == 'Excluir':
            permitirExcluir = login_ADM()
            if permitirExcluir:
                print('usuario pode excluir')
                Excluir_linha_SQL('entrada_materias_primas', 'lote', values['Lote'])









    janela1.close()