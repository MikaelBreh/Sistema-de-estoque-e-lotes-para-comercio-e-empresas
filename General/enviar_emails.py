from conteudoSensivel.info_email_remetente import EMAIL_ADDRESS, EMAIL_PASSWORD, porta_smtp, servidor_smtps, EMAIL_TO
import smtplib
from email.message import EmailMessage
from Banco_de_dados.Validar_lote import verificar_produto_lote


def enviar_email_acoes_do_sistema(opcao_de_envio, dados1, dados2= '', dados3= '', dados4= '', dados5='',
                                  dados6= '', dados7= '', dados8= '', dados9= '', dados10= '', dados11= '',
                                  dados12='', dados13= '', dados14= '', dados15= '', dados16= '',):


    def criar_corpo_email():
        # Definindo qual mensagem deve ser enviado com base em cada opcao
        if opcao_de_envio == 'Criacao_ordem_producao':
            subject = f'Ordem de producao criada - {dados1}'
            msg = f'---------------- Criação Ordem de Produção -----------------\n\n' \
                f'Produto Acabado: {dados1}    \n' \
                  f'numero Ordem: {dados2}       \n' \
                  f'Quantidade: {dados3}         \n\n' \
                  f'Lote 1 usado: {dados4} \n Produto Usado: {verificar_produto_lote(dados4)} \nQuantidade: {dados11}      \n\n'\
                  f'Lote 2 usado: {dados5} \n Produto Usado: {verificar_produto_lote(dados5)} \nQuantidade: {dados12}      \n\n'\
                  f'Lote 3 usado: {dados6} \n Produto Usado: {verificar_produto_lote(dados6)} \nQuantidade: {dados13}      \n\n'\
                  f'Lote 4 usado: {dados7} \n Produto Usado: {verificar_produto_lote(dados7)} \nQuantidade: {dados14}      \n\n'\
                  f'Lote 5 usado: {dados8} \n Produto Usado: {verificar_produto_lote(dados8)} \nQuantidade: {dados15}      \n\n'\
                  f'Lote 6 usado: {dados9} \n Produto Usado: {verificar_produto_lote(dados9)} \nQuantidade: {dados16}      \n \n'\
                  f'Data: {dados10}'

        elif opcao_de_envio == 'Entrada_materias_primas':
            subject = f'Entrada De Materia Prima - {dados2}'
            msg = f'---------------- Entrada Materia Prima -----------------\n\n' \
                  f'Materia Prima: {dados2}   \n' \
                  f'Fornecedor: {dados1}      \n' \
                  f'Categoria: {dados3}       \n' \
                  f'Quantidade: {dados4}      \n' \
                  f'Lote: {dados5}            \n' \
                  f'Data: {dados6}              '

        elif opcao_de_envio == 'Excluir_OP':
            subject = f'Excluir Ordem Producao - {verificar_produto_lote(dados1)}'
            msg = f'---------------- Excluir Ordem Producao -----------------\n\n' \
                  f'{dados1}'

        elif opcao_de_envio == 'Excluir_MP':
            subject = f'Excluir Materia Prima - '
            msg = f'---------------- Excluir Materia Prima -----------------\n\n' \
                  f'Lote Materia Prima: {dados1} \n' \
                  f'Materia Prima: {verificar_produto_lote(dados1)}'


        return subject, msg


    def enviar_email(subject, corpo):
        # criando email
        msg = EmailMessage()
        msg['Subject'] = subject # assunto do email
        msg['From'] = EMAIL_ADDRESS  # remetente
        msg['To'] = EMAIL_TO  # email do destinatario
        msg.set_content(corpo)

        # Enviar Email
        with smtplib.SMTP_SSL(servidor_smtps, porta_smtp) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print('email de alteracao no sistema enviado')


    subject, msg = criar_corpo_email()
    print(subject)
    print(msg)
    enviar_email(subject, msg)
    print('email enviado')