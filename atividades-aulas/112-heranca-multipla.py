class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log', 'a+', encoding='UTF-8') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            return
        self._ligado = False

class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conetar(self):
        if not self._ligado:
            info = f'{self._nome} não está ligado'
            print(info)
            self.log_error(info)
            return

        if self._conectado:
            error = f'{self._nome} JÁ ESTÁ CONECTADO.'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} ESTÁ CONECTADO.'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} NÃO ESTÁ CONECTADO.'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} foi deligado com sucesso.'
        print(info)
        self.log_info(info)
        self._conectado = False

smartphone = Smartphone('Xiaomi Mi 9 SE')
smartphone.conetar()
smartphone.desligar()
smartphone.ligar()
smartphone.conetar()
smartphone.conetar()
smartphone.conetar()
smartphone.desligar()
smartphone.conetar()
smartphone.desconectar()
smartphone.desconectar()
