from PySimpleGUI import PySimpleGUI as sg
from Login import login
from Login import janela_login
from layout import menu_principal
from Menu_principal import Menu_Principal
from Entrada_materias_primas import Entrada_Materias_primas
from Criacao_ordem_producao import Criar_ordem_producao
from Consulta import Consulta
from Banco_de_dados.consultar_tabela import abrirTelaEstoque
from Estoque import Estoque

# Criar a janela inicial de login
situacao_login = login()

# criando janela do menu principal
if situacao_login != False:
    opcao_menu = Menu_Principal()

    while opcao_menu != False:

        # Abrir pagina do menu conforme escolha do usuario
        if opcao_menu == 'Lançar entrada M.P':
            print('lancar entrada')
            valor = Entrada_Materias_primas()

        if opcao_menu == 'Criar Ordem de Producao':
            print('Criar Ordem de Producao')
            valor = Criar_ordem_producao()

        if opcao_menu == 'Estoque':
            print('Abrir Estoque')
            valor = Estoque()

        if opcao_menu == 'Consultas':
            print('Abrir Consultas')
            valor = Consulta()

        opcao_menu = Menu_Principal()








