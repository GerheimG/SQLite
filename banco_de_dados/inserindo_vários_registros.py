import sqlite3

# conexao: é a variável para conexão com o banco de dados 
conexao = sqlite3.connect('C:\guilherme\SQLite\SQLite\inserir_dados.db')

cursor = conexao.cursor()



dados_varios_clientes = [
    ('Maria Souza', 25),
    ('Carlos Pereira', 35),
    ('Pedro José', 28),
    ('Ana Costa', 28),
    ('Luís Gomes', 30),
    ('Fernanda Lima', 22),
    ('Roberto Silva', 40),
    ('Juliana Almeida', 33),
    ('Lucas Martins', 27),
    ('Sofia Ferreira', 31)
]
cursor.executemany(
    'INSERT INTO clientes (nome, idade) VALUES (?, ?)', dados_varios_clientes)
conexao.commit()

conexao.close()