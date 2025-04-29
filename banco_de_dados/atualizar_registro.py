import os
import sqlite3


# conexao: é a variável para conexão com o banco de dados 
conexao = sqlite3.connect('inserir_dados.db')
cursor = conexao.cursor()

os.system('cls')
nome_cliente = input('Digite o nome do cliente: ')
nova_idade = int(input('Digite a nova idade: '))

# Atualiza a idade com base no nome fornecido pelo usuário
cursor.execute('UPDATE clientes SET idade = ? WHERE nome = ?',
            (nova_idade, nome_cliente))

# Salva as alterações no banco de dados
conexao.commit()
print('Dados atualizados com sucesso!')
conexao.close()