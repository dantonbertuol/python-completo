import sqlite3

# Cria a conexão com o banco de dados (arquivo no caso do SQLite)
conexao = sqlite3.connect('arquivos/basedados.db') 
# Cursor - executa os comandos na base de dados
cursor = conexao.cursor()

# Cria tabela - Comando SQL
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                'nome TEXT,'
                'peso REAL'
                ')')

# Insere um registro na tabela - Comando SQL INSERT - Forma insegura passando direto os valores
cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Danton", 72.5)')

# Insere um registro na tabela - Comando SQL INSERT com SQL Injection - Boa prática
# Utilizando uma tupla
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ("José", 50))
# Utilizando um dicionário com as chaves
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {'nome': 'Mari', 'peso': 51})

# Alteração de dados - Comando SQL UPDATE
cursor.execute('UPDATE clientes SET nome=:nome where id=:id',{'nome': 'Marihelly', 'id': 3})

# Exclusão de dados - Comando SQL DELETE
cursor.execute('DELETE FROM clientes where id=:id',{'id': 2})

# Dá um commit - confirma os comandos
conexao.commit()

# Busca os dados - Comando SQL SELECT
cursor.execute('SELECT * FROM clientes')
# Fetch all busca todos os valores
for linha in cursor.fetchall():
    print(f'id: {linha[0]}, nome: {linha[1]}, peso: {linha[2]}')

# Fecha o cursor e base de dados - Boa prática fechar
cursor.close()
conexao.close()
