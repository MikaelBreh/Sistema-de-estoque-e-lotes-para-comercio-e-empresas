from PySimpleGUI import PySimpleGUI as sg
from layout import janela_login

def login_ADM():
    # Criar a janela inicial de login
    janela1 = janela_login()


    # Criar loop para leitura de eventos
    while True:
        window,event,values = sg.read_all_windows()
        # Quando a janela é fechada ou processo cancelado
        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            break

        if event == 'Entrar':
            if values['usuario'] == '1' and values['senha'] == '':
                print('Voce fez o login com sucesso!')
                janela1.close()
                return True

            else:
                janela1['texto_usuario'].update('usuario ou senha incorretos!')

    janela1.close()