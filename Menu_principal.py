from PySimpleGUI import PySimpleGUI as sg
from layout import menu_principal

# funcao para abrir menu principal e executar funcoes
def Menu_Principal():
    # criando janela do menu principal - com base no import do layout
    janela = menu_principal()

    # Criar loop para leitura de eventos
    while True:
        window,event,values = sg.read_all_windows()
        # Quando a janela é fechada ou processo cancelado
        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            return False
            break

        # Se usuario tiver clicado em lancar entrada m.p:
        if event == 'Lançar entrada M.P':
            janela.close()
            return 'Lançar entrada M.P'

        # Se usuario tiver clicado em Criar ordem de producao:
        if event == 'Criar Ordem de Producao':
            janela.close()
            return 'Criar Ordem de Producao'

        # Se usuario tiver clicado em Consultas:
        if event == 'Consultas':
            janela.close()
            return 'Consultas'

        # Se usuario tiver clicado em Estoque:
        if event == 'Estoque':
            janela.close()
            return 'Estoque'

    # fechando menu principal
    janela.close()





