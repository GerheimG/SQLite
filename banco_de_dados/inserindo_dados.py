import sqlite3

# conexao: é a variável para conexão com o banco de dados 
conexao = sqlite3.connect('C:\guilherme\SQLite\SQLite\inserir_dados.db')

cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
''')

# Definição de uma tupla com os dados
dados_cliente = ('João Silva', 30)

# Placeholders (?, ?): Os pontos de interrogação são usados como
# 'espaçoes reservados'. Eles serão substituídos pelos valores da
# tupla dados_cliente (ou seja, 'João Silva' e 30).
# Por quê: Usar placeholders é uma prática recomendade,
# pois previne ataques de injeção de SQL
cursor.execute('INSERT INTO clientes (nome, idade) VALUES (?, ?)', dados_cliente)

conexao.commit() # Salve a transação no banco de dados
conexao.close() # Fecha conexão