import pymysql as MySQLdb
import PySimpleGUI as a

conexao = MySQLdb.connect(host="localhost", user="root",
                          passwd="marcos", database="python")

banco = conexao.cursor()
#

layout = [
    [a.Text('Usuario')],
    [a.Input(key='usuario')],
    [a.Text('Senha')],
    [a.Input(key='senha')],
    [a.Button('entrar'), a.Text(
        '                                                '), a.Button('cadastrar')],
    [a.Text('', key='Mensagem')]
]

window = a.Window('entrar', layout=layout)
while True:
    event, value = window.read()
    if event == a.WIN_CLOSED:
        break
    elif event == 'entrar':
        marcos = value['usuario']
        senha = value['senha']

        try:
            banco.execute(
                f"select * from cadastro where nome='{marcos}' and senha='{senha}';")
            resultado = banco.fetchall()

            for x in resultado:
                if x != "":
                    print(x)
                    print("Query Excecuted successfully")
                else:
                    print(x)
                    print("senha ou login inesistente")
        except:
            conexao.rollback()
            print("Error occured")
    elif event == 'cadastrar':
        marcos = value['usuario']
        senha = value['senha']
        print('cadastrar')
        banco.execute(f"insert into cadastro values ('{marcos}', '{senha}');")
        banco.execute("commit;")

        conexao.close()
