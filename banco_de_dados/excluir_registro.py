import os
import sqlite3


# conexao: é a variável para conexão com o banco de dados 
conexao = sqlite3.connect('inserir_dados.db')
cursor = conexao.cursor()

os.system('cls')

nome_cliente = input('Digite o nome do cliente para excluir: ')

# Executa a exclusão com base no nome forecido pelo usuário
cursor.execute('DELETE FROM clientes WHERE nome = ?', (nome_cliente,))
conexao.commit()

print('Cliente deletado com sucesso!')

# Fecha a conexão
conexao.close()