from PySimpleGUI import PySimpleGUI as sg
from General.layout import entrada_mat_primas
from General.Verificar_data import validar_data
from Banco_de_dados.Insert import insertEntradaMateriaPrima
from Banco_de_dados.Validar_lote import verificarCategoriaMatPrima, validar_lote

fonte = ('Helvetica', 16)


# funcao para abrir janela para dar entrada de materias primas
def Entrada_Materias_primas():

    # criamos a janela de entrada de materia primas - com base no import do layout
    janela = entrada_mat_primas()

    janela['OK'].update(disabled=True)

    # Criar loop para leitura de eventos
    while True:
        window, event, values = sg.read_all_windows()
        # Quando a janela é fechada ou processo cancelado
        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            break
        if event == 'Voltar':
            janela.close()
            return 'Voltar'

        if event == 'Conferencia':

            try:
                # Tenta converter a string em um número inteiro
                numero = int(values['Quantidade'])

            except ValueError:
                # Se ocorrer um erro, exibe uma mensagem de erro para o usuário
                sg.popup_error('Erro: entrada inválida!', font=fonte)
                break

            if values['Fornecedor'] != '' and values['Produto'] != '' and \
                    int(values['Quantidade']) > 0 and values['Lote'] != '' and \
                    validar_data(values['Data']) != False:

                if validar_lote(values['Lote']) is None:

                    sg.popup(f"Voce deseja adicionar: \n"
                             f"\n {values['Produto']}"
                             f"\n Quantidade: {values['Quantidade']} unidades"
                             f"\n Fornecedor: {values['Fornecedor']}"
                             f"\n Data: {values['Data']}"
                             f"\n Lote: {values['Lote']}", font=fonte)
                    janela['OK'].update(disabled=False)

                else:
                    sg.popup('Lote já existente')

            else:
                sg.popup('Verifique as informacoes adicionadas')

        if event == 'OK':
            janela.close()

            insertEntradaMateriaPrima('entrada_materias_primas', values['Fornecedor'],
                                      values['Produto'], verificarCategoriaMatPrima(values['Produto']),
                                      int(values['Quantidade']), values['Lote'], values['Data'])

    # fechando menu de entrada de materias primas
    janela.close()
