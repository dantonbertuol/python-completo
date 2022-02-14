def saudacao(msg='Olá', nome='Usuário'): # Após o igual é o valor default do parâmetro
    print(msg, nome)

saudacao() # Se não manda os argumentos pega o default
saudacao(nome='Maria', msg='Hello') # Atribuindo o nome do argumento não precisa estar na ordem
saudacao('Olá', 'Danton')
saudacao('Oi', 'José')
saudacao('Bom dia', 'Bertuol')
