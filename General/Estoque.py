from Banco_de_dados.consultar_tabela import abrirTelaEstoque
from PySimpleGUI import PySimpleGUI as sg
from General.layout import estoque

def Estoque():
    # Criar a janela inicial de login
    janela1 = estoque()

    # Criar loop para leitura de eventos
    while True:
        window,event,values = sg.read_all_windows()
        # Quando a janela é fechada ou processo cancelado
        if event == sg.WINDOW_CLOSED or event == 'Voltar':
            janela1.close()
            return False
            break

        if event == 'Consultar Estoque':
            if values['filtrarCategorias'] == '' or values['filtrarCategorias'] == 'selecionar':
                abrirTelaEstoque()
            else:
                abrirTelaEstoque(values['filtrarCategorias'])



    janela1.close()

