import CRUD
import this
import time

this.cod = 0
this.opcao = -1
msg = ''

def menu():
    print('\nEscolha uma das opções abaixo:\n'
               '1. Cadastrar Aluno\n'
               '2. Consultar Alunos\n'
               '3. Atualizar nome do Aluno\n'
               '4. Excluir Aluno e todas as notas\n'
               '5. Cadastrar nota\n'
               '6. Consultar notas\n'
               '7. Atualizar nota\n'
               '8. Atualizar imagem da atividade\n'
               '9. Excluir nota\n'
                '0. Sair\n')
    this.opcao = int(input())

def operacoes():
    while (this.opcao != 0):
        menu()
        if this.opcao == 1:
            CRUD.inserirAluno()

        elif this.opcao == 2:
            CRUD.consultarAlunos()

        elif this.opcao == 3:
            CRUD.atualizarAluno()

        elif this.opcao == 4:
            print('Digite o código do aluno que deseja excluir: ')
            cod = int(input())
            CRUD.excluirAluno(cod)

        elif this.opcao == 5:
            CRUD.cadastrarNota()

        elif this.opcao == 6:
            CRUD.consultarNotas()

        elif this.opcao == 7:
            CRUD.atualizarNota()

        elif this.opcao == 8:
            CRUD.atualizarImagem()

        elif this.opcao == 9:
            print('Digite a linha em que está a nota que deseja excluir: ')
            cod = int(input())
            CRUD.excluirNota(cod)

        elif this.opcao == 0:
            result = time.localtime()

            print('Obrigado por utilizar nossa aplicação\n')

            if result.tm_hour > 17:
                print('Tenha uma Boa Noite')

            elif result.tm_hour > 11 and result.tm_hour < 18:
                print('Tenha uma Boa Tarde')

            elif result.tm_hour > 0 and result.tm_hour < 12:
                print('Tenha um Bom Dia')

        else:
            print('Ops, não encontrei essa opção   :(   ')