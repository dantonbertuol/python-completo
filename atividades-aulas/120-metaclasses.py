class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'AA':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace:
            print(f'Oi você precisa criar o método b_fala em {name}.')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método em {name}.')
        return type.__new__(mcs, name, bases, namespace)

class AA(metaclass=Meta):
    def falar(self):
        self.b_fala()

class BB(AA):
    def b_fala(self):
        print('Falei!')

b = BB()
b.falar()