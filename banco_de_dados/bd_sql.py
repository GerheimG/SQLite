import sqlite3

# conexao: é a variável para conexão com o banco de dados 
conexao = sqlite3.connect('C:\guilherme\SQLite\SQLite\meu_banco_de_dados.db')

# para operações no banco de dados, você também precisará de um cursor,
# que é um objeto que permite executar comandos SQL.
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
''')

