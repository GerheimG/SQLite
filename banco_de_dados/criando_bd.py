import sqlite3

# conexao: é a variável para conexão com o banco de dados 
conexao = sqlite3.connect('C:\guilherme\SQLite\SQLite\primeiro_bd.db')

# para operações no banco de dados, você também precisará de um cursor,
# que é um objeto que permite executar comandos SQL.
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes(
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
        )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS telefones(
        id_telefone INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER,
        telefone TEXT NOT NULL
        )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS endereco(
        id_cliente INTEGER,
        rua TEXT NOT NULL,
        numero_casa REAL NOT NULL,
        bairro TEXT NOT NULL,
        cidade TEXT NOT NULL,
        estado TEXT NOT NULL
        )
''')

