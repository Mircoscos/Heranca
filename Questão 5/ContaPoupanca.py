from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def __init__(self, numeroConta, saldo, taxaRendimento):
        super().__init__(numeroConta, saldo)
        self.taxaRendimento = taxaRendimento

    def detalhesConta(self):
        print(f'''Saldo: {self.saldo}
    Numero da Conta: {self.numeroConta}
    Taxa de Rendimento: {self.taxaRendimento}''')
        