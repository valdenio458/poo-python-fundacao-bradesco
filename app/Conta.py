class Conta:
    def __init__(self, titular, numero, saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    @property
    def saldo(self):
        return self.saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("O saldo não pode ser negativo")
        else:
            self.saldo = saldo
