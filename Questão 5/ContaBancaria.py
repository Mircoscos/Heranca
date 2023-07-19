class ContaBancaria:
    def __init__(self, numeroConta, saldo):
        self.numeroConta = numeroConta
        self.saldo = saldo

    def detalhesConta(self):
        print(f'''Saldo: {self.saldo}
    Numero da Conta: {self.numeroConta}''')

    def depositar(self, deposito):
        self.saldo += deposito

    def sacar(self, saque):
        self.saldo -= saque
