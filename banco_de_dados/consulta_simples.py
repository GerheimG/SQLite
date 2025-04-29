import os
import sqlite3

# conexao: é a variável para conexão com o banco de dados 
conexao = sqlite3.connect('C:\guilherme\SQLite\SQLite\inserir_dados.db')

cursor = conexao.cursor()

cursor.execute('SELECT * FROM clientes')
resultados = cursor.fetchall()

os.system('cls')
for row in resultados:
    print(row)
conexao.close()