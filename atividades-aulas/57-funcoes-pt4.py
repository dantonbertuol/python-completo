variavel = 'valor' # Variável global

def func():
    print(variavel)

def func2():
    global variavel # Dessa forma a variável local assume como global (não é uma boa prática)
    variavel = 'Outro Valor' # Neste momento cria uma nova variável local
    print(variavel)

func()
func2()
print(variavel)