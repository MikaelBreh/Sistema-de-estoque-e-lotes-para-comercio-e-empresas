from PySimpleGUI import PySimpleGUI as sg
from General.layout import janela_login
from Banco_de_dados.consultar_tabela import enviar_email_estoque_minimo

def login(valor=True):
    # Criar a janela inicial de login
    janela1 = janela_login()
    enviar_email_estoque_minimo()

    # Criar loop para leitura de eventos
    while True:
        window,event,values = sg.read_all_windows()
        # Quando a janela é fechada ou processo cancelado
        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            return False
            break

        if event == 'Entrar':
            if values['usuario'] == '' and values['senha'] == '':
                print('Voce fez o login com sucesso!')
                break
            else:
                janela1['texto_usuario'].update('usuario ou senha incorretos!')

    janela1.close()