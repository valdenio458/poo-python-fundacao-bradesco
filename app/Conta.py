class Conta:
    def __init__(self, titular, numero, saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    # método get
    def get_saldo(self):
        return self.saldo

    # método set
    def set_saldo(self, saldo):
        if (saldo < 0):
            print("O saldo não pode ser negativo")
        else:
            self.saldo = saldo

    def saque(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")

    def depositar(self, valor):
        self.saldo += valor

    def extrato(self):
        print(f"Cliente: {self.titular} - Saldo: {self.saldo}")
