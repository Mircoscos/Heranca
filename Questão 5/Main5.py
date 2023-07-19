from ContaBancaria import ContaBancaria
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

conta1 = ContaBancaria(1234, 999)
conta2 = ContaCorrente(4321, 999, 2)
conta3 = ContaPoupanca(3412, 999, 10)

print('========= Conta 1 =========')
conta1.depositar(2)
conta1.sacar(1)
conta1.detalhesConta()
print('========= Conta 2 =========')
conta2.depositar(4)
conta2.sacar(5)
conta2.detalhesConta()
print('========= Conta 3 =========')
conta3.depositar(10)
conta3.sacar(29)
conta3.detalhesConta()