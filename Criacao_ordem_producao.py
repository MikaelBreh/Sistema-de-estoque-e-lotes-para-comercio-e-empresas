from PySimpleGUI import PySimpleGUI as sg
from layout import criar_ordem_producao
from Menu_principal import Menu_Principal
from Verificar_data import validar_data
from Banco_de_dados.Insert import insertSaidaMateriaPrima
from Validar_lote import validar_lote, verificar_produto_lote, verificarCategoriaMatPrima
from Banco_de_dados.consultar_tabela import transLoteEmNome

fonte = ('Helvetica', 16)


# funcao para abrir janela para dar entrada de materias primas
def Criar_ordem_producao():
    # Validar todas as informacoes referente a lote e quantidade dentro da criacao de ordem de producao
    def validarEntradaLote(value_lote, value_quantidade, preenchimento_obrigatorio=True):

        if preenchimento_obrigatorio == True:
            if value_lote != '':
                if validar_lote(value_lote) is not None:
                    if value_quantidade != '':
                        try:
                         if int(value_quantidade) > 0:
                             return True
                        # Se ao tentar comparar a quantidade com um int gerar um erro, nao executará
                        except ValueError:
                            return False
                    else:
                        # Se o valor do lote nao for maior que 0 ele nao vai aceitar
                        return False
                        print('obrigatorio -  quantidade é inferior a zero ou nula - False')
                else:
                    # Se a funcao validar lote nao encontrar um lote, não será aceito
                    return False
                    print('obrigatorio - lote nao encontrado - False')
            else:
                # Se o 'input' lote igualar nada, não será aceito
                return False
                print('obrigatorio - lote nulo - False')

        if preenchimento_obrigatorio == False:
            # Se valor e quantidade nao forem preenchidos, executa
            if value_lote == '' and value_quantidade == '':
                return True

            # Se preenchimento nao for obrigatorio e valor ou quantidade estiverem preenchidos, validar:
            else:
                # Se o lote for encontrado, validar:
                if validar_lote(value_lote) is not None:
                    if value_quantidade != '':
                        try:
                            # Se quantidade estiver correta, executa:
                            if int(value_quantidade) > 0:
                                return True
                        # Se ao tentar comparar quantidade com int resultar em erro, não será aceito
                        except ValueError:
                            return False
                else:
                    # Se for preenchido, mas com lote invalido, não será aceito
                    return False
                    print('nao obrigatorio, prebchdio, lote nao encontrado')


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

            # Lançar ordem de producao no banco de dados
            insertSaidaMateriaPrima(values['Produto'], values['Numero Ordem'],
                                    verificarCategoriaMatPrima(values['Produto']),
                                    int(values['Quantidade']),
                                    values['Lote_1'], values['Lote_2'],
                                    values['Lote_3'], values['Lote_4'],
                                    values['Lote_5'], values['Lote_6'],
                                    values['Data'])

    # fechando menu de entrada de materias primas
    janela.close()
