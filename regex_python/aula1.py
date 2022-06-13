import re

# findall search sub
# compile

string = 'Esté é um teste de expressões regulares.'
# search - Encontra a expressão regular r'teste' dentro da string
print(re.search(r'teste', string))
# findall - Encontra todas as ocorrencias da expressao regular na string
print(re.findall(r'teste', string))
# sub - substitui a expressao regular por outra coisa na string
print(re.sub(r'teste', 'ABCD', string))

# compile - compila uma expressão regular para ser reutilizada
regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('ABCD', string))
