from ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self, numeroConta, saldo, limite):
        super().__init__(numeroConta, saldo)
        self.limite = limite

    def detalhesConta(self):
        print(f'''Saldo: {self.saldo}
    Numero da Conta: {self.numeroConta}
    Limite Cheque Especial: {self.limite}''')
        