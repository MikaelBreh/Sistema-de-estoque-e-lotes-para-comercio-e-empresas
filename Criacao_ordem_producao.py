from PySimpleGUI import PySimpleGUI as sg
from layout import criar_ordem_producao
from Menu_principal import Menu_Principal
from Verificar_data import validar_data
from Banco_de_dados.Insert import insert_data_ordem
from Validar_lote import validar_lote, verificar_produto_lote

fonte = ('Helvetica', 16)

# funcao para abrir janela para dar entrada de materias primas
def Criar_ordem_producao():
    # criamos a janela de entrada de materia primas - com base no import do layout
    janela = criar_ordem_producao()

    janela['OK'].update(disabled=True)

    # Criar loop para leitura de eventos
    while True:
        window,event,values = sg.read_all_windows()
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


            if values['Produto'] != '' and values['Produto'] != 'selecionar'\
                    and values['Numero Ordem'] != '' and \
                    int(values['Quantidade']) > 0 and \
                    validar_lote(values['Lote_1']) != None and \
                    validar_lote(values['Lote_2']) != None and \
                    validar_lote(values['Lote_3']) != None and \
                    validar_data(values['Data']) != False:
                if values['Lote_4'] == '':

                    sg.popup(f"Voce deseja criar a ordem de numero: {values['Numero Ordem']}\n"
                             f"\n {values['Produto']}"
                             f"\n Quantidade: {values['Quantidade']} unidades"
                             f"\n M.P 1: {verificar_produto_lote(values['Lote_1'])}"
                             f"\n M.P 2: {verificar_produto_lote(values['Lote_2'])}"
                             f"\n M.P 3: {verificar_produto_lote(values['Lote_3'])}"
                             f"\n Data: {values['Data']}", font=fonte)
                    janela['OK'].update(disabled=False)


                elif values['Lote_4'] != ''and validar_lote(values['Lote_4']) != None:
                    sg.popup(f"Voce deseja criar a ordem de numero: {values['Numero Ordem']}\n"
                             f"\n {values['Produto']}"
                             f"\n Quantidade: {values['Quantidade']} unidades"
                             f"\n M.P 1: {verificar_produto_lote(values['Lote_1'])}"
                             f"\n M.P 2: {verificar_produto_lote(values['Lote_2'])}"
                             f"\n M.P 3: {verificar_produto_lote(values['Lote_3'])}"
                             f"\n M.P 4: {verificar_produto_lote(values['Lote_4'])}"
                             f"\n Data: {values['Data']}", font=fonte)
                    janela['OK'].update(disabled=False)

                else:
                    sg.popup('ERRO')


            else:
                sg.popup('Verifique as informacoes adicionadas')

        if event == 'OK':
            janela.close()

            insert_data_ordem(values['Produto'], values['Numero Ordem'],
                              int(values['Quantidade']),  values['Lote_1'], values['Lote_2'],
                              values['Lote_3'], values['Lote_4'], values['Data'])


    # fechando menu de entrada de materias primas
    janela.close()