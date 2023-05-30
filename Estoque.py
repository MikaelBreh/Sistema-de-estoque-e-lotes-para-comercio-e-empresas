from Banco_de_dados.consultar_tabela import abrirTelaEstoque
from PySimpleGUI import PySimpleGUI as sg
from layout import estoque

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
        # Quando queremos ir para o menu principal
        if event == 'Entrar':
            if values['usuario'] == 'mikael' and values['senha'] == '12349':
                print('Acessando estoque')
                break

        if event == 'Consultar Estoque':
            abrirTelaEstoque()
            janela1.close()

    janela1.close()

