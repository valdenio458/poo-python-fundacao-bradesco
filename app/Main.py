from Cliente import Cliente
from Conta import Conta


class Main:
    pass


print("Testando o projeto")


c1 = Cliente("João", "9999-9999")
conta = Conta("c1.nome", "0001", 100)

print(f"A conta {conta.numero} de {c1.nome} tem R${conta.saldo:.2f} de saldo.")