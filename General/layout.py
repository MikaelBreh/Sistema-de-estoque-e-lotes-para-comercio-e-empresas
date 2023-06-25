from PySimpleGUI import PySimpleGUI as sg
from General.Listas import valores, forncedores, produtos_acabados, categorias

# Criar as janelas

# padronizando texto
fonte = ('Helvetica', 16)
fonte_box = ('Helvetiva', 15)
fonte_button = ('Helvetiva', 13)


# Layout login
def janela_login():
    sg.theme('Reddit')  # É possivel colocar outros temas (doc. oficial)
    layout = [
        [sg.Text('Usuario', font=fonte), sg.Input(key='usuario', font=fonte_box)],
        [sg.Text('Senha', font=fonte), sg.Input(key='senha', password_char='*', font=fonte_box)],
        [sg.Button('Entrar', font=fonte_button), sg.Button('Cancelar', font=fonte_button)],
        [sg.Text(key='texto_usuario', font=fonte_button)]
    ]
    return sg.Window('Login', layout=layout, finalize=True)


# Layout Menu Principal
def menu_principal():
    sg.theme('Reddit')
    layout = [
        [sg.Button('Lançar entrada M.P', font=fonte_button, size=(10, 2)),
         sg.Button('Excluir M.P Lançada', font=fonte_button, size=(10, 2), button_color='#FF6666')],
        [sg.Button('Criar Ordem de Producao', font=fonte_button, size=(10, 2)),
         sg.Button('Excluir Ordem Lançada', font=fonte_button, size=(10, 2), button_color='#FF6666')],
        [sg.Button('Estoque', font=fonte_button, size=(10, 2)),
         sg.Button('Consultas', font=fonte_button, size=(10, 2))],
        [sg.Button('Cancelar', font=fonte_button, size=(10, 2))]

    ]

    return sg.Window('Menu Principal', layout=layout, size=(350, 450), finalize=True)


# Layout entrada materias primas
def entrada_mat_primas():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Fornecedor', font=fonte),
         sg.OptionMenu(values=forncedores, size=(8, 12), default_value='selecionar', key='Fornecedor')],
        [sg.Text('Produto', font=fonte),
         sg.OptionMenu(values=valores, size=(8, 12), default_value='selecionar', key='Produto')],
        [sg.Text('Quantidade', font=fonte), sg.Input(key='Quantidade', font=fonte_box)],
        [sg.Text('Lote', font=fonte), sg.Input(key='Lote', font=fonte_box)],
        [sg.Text('Data', font=fonte), sg.Input(key='Data', font=fonte_box)],
        [sg.Text('Voce so podera clicar em ok depois de clicar em conferir', font=fonte)],
        [sg.Button('Conferencia', font=fonte), sg.Button('OK', font=fonte), sg.Button('Voltar', font=fonte)]
    ]
    return sg.Window('Entrada de Materias Primas', layout=layout, finalize=True)


def Excluir():
    sg.theme('Reddit')  # É possivel colocar outros temas (doc. oficial)
    layout = [
        [sg.Text('Você deseja realmente excluir?', font=fonte)],
        [sg.Text('Digite o Lote/numero Ordem:  ', font=fonte), sg.Input(key='Lote', font=fonte_box)],
        [sg.Button('Conferencia', font=fonte), sg.Button('Excluir', font=fonte), sg.Button('Voltar', font=fonte)]
    ]

    return sg.Window('Excluir Materia Prima/Ordem de producao com Lançamento', layout=layout, finalize=True)



# Layout criacao de ordem de producao
def criar_ordem_producao():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Produto'),
         sg.OptionMenu(values=produtos_acabados, size=(8, 12), default_value='selecionar', key='Produto')],
        [sg.Text('Numero Ordem', font=fonte), sg.Input(key='Numero Ordem', font=fonte_box)],
        [sg.Text('Quantidade', font=fonte), sg.Input(key='Quantidade', font=fonte_box)],

        [sg.Text('Lote 1', font=fonte), sg.Input(key='Lote_1', font=fonte_box, size=(25, 1)),
         sg.Text('Quantidade', font=fonte, text_color='gray'), sg.Input(key='quant1', font=fonte_box, size=(13, 1))],

        [sg.Text('Lote 2', font=fonte), sg.Input(key='Lote_2', font=fonte_box, size=(25, 1)),
         sg.Text('Quantidade', font=fonte, text_color='gray'), sg.Input(key='quant2', font=fonte_box, size=(13, 1))],

        [sg.Text('Lote 3', font=fonte), sg.Input(key='Lote_3', font=fonte_box, size=(25, 1)),
         sg.Text('Quantidade', font=fonte, text_color='gray'), sg.Input(key='quant3', font=fonte_box, size=(13, 1))],

        [sg.Text('Lote 4', font=fonte), sg.Input(key='Lote_4', font=fonte_box, size=(25, 1)),
         sg.Text('Quantidade', font=fonte, text_color='gray'), sg.Input(key='quant4', font=fonte_box, size=(13, 1))],

        [sg.Text('Lote 5', font=fonte), sg.Input(key='Lote_5', font=fonte_box, size=(25, 1)),
         sg.Text('Quantidade', font=fonte, text_color='gray'), sg.Input(key='quant5', font=fonte_box, size=(13, 1))],

        [sg.Text('Lote 6', font=fonte), sg.Input(key='Lote_6', font=fonte_box, size=(25, 1)),
         sg.Text('Quantidade', font=fonte, text_color='gray'), sg.Input(key='quant6', font=fonte_box, size=(13, 1))],

        [sg.Text('Data', font=fonte), sg.Input(key='Data', font=fonte_box)],
        [sg.Text('Voce so podera clicar em ok depois de clicar em conferir', font=fonte_button)],
        [sg.Button('Conferencia'), sg.Button('OK'), sg.Button('Voltar')]
    ]
    return sg.Window('Criar ordem de proucao', layout=layout, finalize=True)


# Layout criacao de ordem de producao
def consulta():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Por lote do fornecedor', font=fonte), sg.Input(key='Por lote do fornecedor', font=fonte_box)],
        [sg.Text('Por ordem de producao', font=fonte), sg.Input(key='Por ordem de producao', font=fonte_box)],
        [sg.Text('Por Materia Prima', font=fonte),
         sg.OptionMenu(values=valores, size=(4, 8), default_value='selecionar', key='Por Materia Prima')],
        [sg.Text('Por Produto Acabado', font=fonte),
         sg.OptionMenu(values=produtos_acabados, size=(4, 8), default_value='selecionar', key='Por Produto Acabado')],
        [sg.Button('OK', font=fonte_button), sg.Button('Voltar', font=fonte_button)]
    ]

    return sg.Window('Consultas', layout=layout, finalize=True)


def tela_consulta():
    sg.theme('Reddit')
    layout = [
        [sg.Text(key='texto_da_consulta', font=fonte)],
        [sg.Text(key='texto_da_consulta2', font=fonte)],
        [sg.Button('OK', font=fonte_button), sg.Button('Voltar', font=fonte_button)]
    ]

    return sg.Window('Consulta', layout=layout, finalize=True, size=(600, 700))


def estoque():
    sg.theme('Reddit')
    layout = [
        [sg.Button('Consultar Estoque', font=fonte_button, size=(10, 2))],
        [sg.Text('Filtrar', font=fonte), sg.OptionMenu(values=categorias, size=(8, 12),
                                                       default_value='selecionar', key='filtrarCategorias')],
        [sg.Button('Voltar', font=fonte_button)]

    ]

    return sg.Window('Consulta', layout=layout, finalize=True, size=(600, 500))
