import mysql.connector
import conexaoBD
import this

db_connection = conexaoBD.conectar()
con = db_connection.cursor()

this.opcional = -1

def inserirAluno():
    try:
        print('Digite o nome do aluno: ')
        nome = input()
        sql = "select nome from alunos where nome = '{}'".format(nome)
        con.execute(sql)
        resultado = con.fetchall()
        if len(resultado) != 0:
            while (this.opcional < 1) or (this.opcional > 2):
                print('Ops, encontrei aluno(s) com nome: {}, mesmo assim deseja adicionar? Digite 1 para SIM ou 2 para NÃO'.format(nome))
                this.opcional = int(input())
                if (this.opcional < 1) or (this.opcional > 2):
                    print('Valor inválido! Digite 1 para SIM ou 2 para NÃO')
            if this.opcional == 1:
                sql = "insert into alunos (codAluno, nome) values ('', '{}')".format(nome)
                con.execute(sql)
                db_connection.commit()
                print('{} cadastrado(a) com sucesso!'.format(con.rowcount))
            if this.opcional == 2:
                print('Aluno não adicionado')

        else:
            sql = "insert into alunos (codAluno, nome) values ('', '{}')".format(nome)
            con.execute(sql)
            db_connection.commit()
            print('{} cadastrado(a) com sucesso!'.format(con.rowcount))

    except Exception as erro:
        return erro

def consultarAlunos():
    try:
        sql = "select * from alunos"
        con.execute(sql)
        resultado = con.fetchall()

        if len(resultado) != 0:
            sql = "select * from alunos"
            con.execute(sql)
            for (codAluno, nome) in con:
                print('Código do Aluno: {}, Nome do Aluno: {}'.format(codAluno, nome))
                print('\n')

        else:
            print('Não há alunos na base de dados :(')

    except Exception as erro:
        print(erro)

def atualizarAluno():
    try:
        print('Digite o código do aluno que deseja alterar o nome: ')
        cod = int(input())

        sql = "select codAluno from alunos where codAluno = '{}'".format(cod)
        con.execute(sql)
        resultado = con.fetchall()
        if len(resultado) != 0:
            print('Digite o nome correto do aluno: ')
            novoDado = input()
            sql = "update alunos set nome = '{}' where codAluno = '{}'".format(novoDado, cod)
            con.execute(sql)
            db_connection.commit()
            print('{} Atualizado com sucesso!'.format(con.rowcount))

        else:
            print('Não há alunos com este cógido :(')

    except Exception as erro:
        print(erro)

def excluirAluno(cod):
    try:
        sql = "select codAluno from alunos where codAluno = '{}'".format(cod)
        con.execute(sql)
        resultado = con.fetchall()
        if len(resultado) != 0:
            sql = "delete from alunos where codAluno = '{}'".format(cod)
            con.execute(sql)
            db_connection.commit()
            sql2 = "delete from midia where codNotas = '{}'".format(cod)
            con.execute(sql2)
            db_connection.commit()
            print('Aluno Excluído com sucesso!')

        else:
            print('Não há alunos com este código :(')

    except Exception as erro:
        print(erro)

def cadastrarNota():
    try:
        notas = -1
        print('Digite o código do aluno que receberá a nota: ')
        cod = int(input())
        sql = "select codAluno from alunos where codAluno = '{}'".format(cod)
        con.execute(sql)
        resultado = con.fetchall()

        if len(resultado) != 0:
            print('Digite o caminho da imagem da nota, caso deseje adicionar: ')
            foto = input()
            if foto == '':
                foto = 'Não há imagem da atividade'
            while (notas < 0) or (notas > 10):
                print('Digite uma nota de 0 a 10: ')
                notas = float(input())
                if (notas < 0) or (notas > 10):
                    print('Nota inválida, tente novamente!')
            sql = "insert into midia (id, codNotas, foto, notas) values ('', '{}', '{}', '{}')".format(cod, foto, notas)
            con.execute(sql)
            db_connection.commit()
            print('{} Nota Cadastrada ao aluno de código {}'.format(con.rowcount, cod))

        else:
            print('Não encontrei o código na base de dados :(')

    except Exception as erro:
        print(erro)

def consultarNotas():
    try:
        sql = "select * from midia"
        con.execute(sql)
        resultado = con.fetchall()

        if len(resultado) != 0:
            sql = "select * from midia"
            con.execute(sql)
            for (id, codNotas, foto, notas) in con:
                print("(nota na linha {}), aluno de código {}, foto no endereço: {}, nota {}".format(id, codNotas, foto, notas))
                print('\n')

        else:
            print('Ops, parece que não há notas cadastradas :(')

    except Exception as erro:
        print(erro)

def atualizarNota():
    try:
        novoDado = -1
        print('Digite a linha da nota que deseja atualizar: ')
        id = int(input())

        sql = "select id from midia where id = '{}'".format(id)
        con.execute(sql)
        resultado = con.fetchall()

        if len(resultado) != 0:
            while (novoDado<0) or (novoDado>10):
                print('Digite a nova nota: ')
                novoDado = float(input())
                if (novoDado<0) or (novoDado>10):
                    print('Nota inválida, tente novamente')
            sql = "update midia set notas = '{}' where id = '{}'".format(novoDado, id)
            con.execute(sql)
            db_connection.commit()
            print('{} Atualizado com sucesso!'.format(con.rowcount))

        else:
            print('Ops, não encontrei essa nota em nosso banquinho de dados :(')

    except Exception as erro:
        print(erro)

def atualizarImagem():
    try:
        print('Digite a linha em que está a nota: ')
        cod = int(input())

        sql = "select id from midia where id = '{}'".format(cod)
        con.execute(sql)
        resultado = con.fetchall()

        if len(resultado) !=0:
            print('Digite o novo caminho da imagem da atividade: ')
            novoDado = input()
            if novoDado =='':
                novoDado = 'Não há imagem da atividade'
            sql = "update midia set foto = '{}' where id = '{}'".format(novoDado, cod)
            con.execute(sql)
            db_connection.commit()
            print('{} Imagem da atividade atualizada com sucesso!'.format(con.rowcount))

        else:
            print('Não encontrei esse caminho em nosso banquinho de dados :(')

    except Exception as erro:
        print(erro)

def excluirNota(cod):
    try:
        sql = "select id from midia where id = '{}'".format(cod)
        con.execute(sql)
        resultado = con.fetchall()

        if len(resultado) !=0:
            sql = "delete from midia where id = '{}'".format(cod)
            con.execute(sql)
            db_connection.commit()
            print('{}, A nota foi excluída com sucesso!'.format(con.rowcount))

        else:
            print('Ops, não encontrei a linha dessa nota na base de dados :(')

    except Exception as erro:
        print(erro)