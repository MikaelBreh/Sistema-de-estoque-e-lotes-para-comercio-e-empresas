from PySimpleGUI import PySimpleGUI as sg
from layout import tela_consulta
from Banco_de_dados.consultar_tabela import consultar_por_lote


# funcao para abrir a consulta como lista
def PopUpconsulta():
    # criando a janela de consutlas - com base no import do layout
    janela = tela_consulta()

    # Criar loop para leitura de eventos
    while True:
        window, event, values = sg.read_all_windows()

        print('tela de consulta aberta')
        consultar_por_lote()

        # Quando a janela é fechada ou processo cancelado
        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            break

        if event == 'Voltar' or event == 'OK':
            janela.close()
            return 'Voltar'


    # fechando menu de consultas
    janela.close()