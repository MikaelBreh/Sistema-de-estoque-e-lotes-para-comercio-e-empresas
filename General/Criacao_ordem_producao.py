from PySimpleGUI import PySimpleGUI as sg
from General.layout import criar_ordem_producao
from General.Verificar_data import validar_data
from Banco_de_dados.Insert import insertSaidaMateriaPrima
from Banco_de_dados.Validar_lote import verificar_produto_lote, verificarCategoriaMatPrima, validarOrdem, validarEntradaLote
from General.enviar_emails import enviar_email_acoes_do_sistema

fonte = ('Helvetica', 16)




# funcao para abrir janela para dar entrada de materias primas
def Criar_ordem_producao():
    # Validar todas as informacoes referente a lote e quantidade dentro da criacao de ordem de producao


    def contarLotesPreenchidos():
        lotes_preenchidos = []
        quantidades_preenchidas = []
        for contar_lote in range(6):
            if values[f'Lote_{contar_lote + 1}'] != '':
                lotes_preenchidos.append(values[f'Lote_{contar_lote + 1}'])
                quantidades_preenchidas.append(values[f'quant{contar_lote + 1}'])

        return lotes_preenchidos, quantidades_preenchidas

    # Exibir lote e sua quantidade se os mesmos estiverem preenchidos pelo usuario
    def exibirLoteQuantidadePopUp(lote, quantidade, numero):
        if verificar_produto_lote(values['Lote_1']) is not None and quantidade != '':
            return f" M.P {numero}: {verificar_produto_lote(lote)} Quant: {quantidade}"

        else:
            return ''


    # criamos a janela de entrada de materia primas - com base no 'import' do layout
    janela = criar_ordem_producao()

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
                # Tenta converter a 'string' num número inteiro
                numero = int(values['Quantidade'])

            except ValueError:
                # Se ocorrer um erro, exibe uma mensagem de erro para o utilizador
                sg.popup_error('Erro: Quantidade inválida!', font=fonte)
                break

            # Validar informacoes para lançar a ordem de producao ou nao
            if values['Produto'] != '' and values['Produto'] != 'selecionar' \
                    and values['Numero Ordem'] != '' and \
                    validarOrdem(values['Numero Ordem']) == None and \
                    int(values['Quantidade']) > 0 and \
                    validarEntradaLote(values['Lote_1'], values['quant1'], True) and \
                    validarEntradaLote(values['Lote_2'], values['quant2'], True) and \
                    validarEntradaLote(values['Lote_3'], values['quant3'], True) and \
                    validarEntradaLote(values['Lote_4'], values['quant4'], False) and \
                    validarEntradaLote(values['Lote_5'], values['quant5'], False) and \
                    validarEntradaLote(values['Lote_6'], values['quant6'], False) and \
                    validar_data(values['Data']) is not False:

                        # Exibir PopUp para usuario conferir informacoes digitadas, e apos lançar no banco de dados
                        sg.popup(f"Voce deseja criar a ordem de numero: {values['Numero Ordem']}\n"
                                 f"\n {values['Produto']}"
                                 f"\n Quantidade: {values['Quantidade']} unidades",
                                 exibirLoteQuantidadePopUp(values['Lote_1'], values['quant1'], 1),
                                 exibirLoteQuantidadePopUp(values['Lote_2'], values['quant2'], 2),
                                 exibirLoteQuantidadePopUp(values['Lote_3'], values['quant3'], 3),
                                 exibirLoteQuantidadePopUp(values['Lote_4'], values['quant4'], 4),
                                 exibirLoteQuantidadePopUp(values['Lote_5'], values['quant5'], 5),
                                 exibirLoteQuantidadePopUp(values['Lote_6'], values['quant6'], 6),
                                 f"\n Data: {values['Data']}", font=fonte)
                        janela['OK'].update(disabled=False)


            # Se validacoes gerarem um erro, solicitar ao usuario para que veja as informacoes digitadas
            else:
                sg.popup('Verifique as informacoes adicionadas')

        # Se validacoes resultarem em sucesso, habilitar botao de ok(lancar ordem e saida dentro do banco de dados)
        if event == 'OK':
            janela.close()

            enviar_email_acoes_do_sistema('Criacao_ordem_producao', values['Produto'], values['Numero Ordem'],
                                            int(values['Quantidade']),
                                            values['Lote_1'], values['Lote_2'],
                                            values['Lote_3'], values['Lote_4'],
                                            values['Lote_5'], values['Lote_6'],
                                            values['Data'],
                                            values['quant1'], values['quant2'],
                                            values['quant3'],values['quant4'],values['quant5'],
                                            values['quant6'])

            # Lançar ordem de producao no banco de dados
            insertSaidaMateriaPrima(contarLotesPreenchidos(), values['Produto'], values['Numero Ordem'],
                                    verificarCategoriaMatPrima(values['Produto']),
                                    int(values['Quantidade']),
                                    values['Lote_1'], values['Lote_2'],
                                    values['Lote_3'], values['Lote_4'],
                                    values['Lote_5'], values['Lote_6'],
                                    values['Data'])


    # fechando menu de entrada de materias primas
    janela.close()
