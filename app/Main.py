from Cliente import Cliente
from Conta import Conta


class Main:
    pass


print("Testando o projeto")


c1 = Cliente("João", "9999-9999")
c1.nome = c1.get_nome()
conta = Conta(c1.nome, "0001", 100)

conta.depositar(1000)
conta.saque(50)
print(f"A conta {conta.numero} de {c1.nome} tem R${conta.saldo:.2f} de saldo.")
