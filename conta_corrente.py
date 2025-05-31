#^ 5 - Classe Conta Corrente: 
#Crie uma classe para implementar uma conta corrente. 
# A classe deve possuir os seguintes atributos: 
# número da conta, nome do correntista e saldo. 
# Os métodos são os seguintes: alterarNome, depósito e saque;
# No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, numeroConta, nomeCorrentista, saldo=0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo
    
    def alterarNome(self, novoNome):
        self.nomeCorrentista = novoNome
    
    def deposito(self, valor):
        self.saldo += valor
                
    
    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor  
        else:
            print("Saldo Insuficiente!")
            
    def __str__(self):
        return (f"Conta: {self.numeroConta} | "
                f"Correntista: {self.nomeCorrentista} | "
                f"Saldo: {self.saldo:.2f}")
     
novaConta = ContaCorrente("001", "Marcello", 500000)
novaConta.alterarNome("Marcello Prado")
novaConta.deposito(5800)
novaConta.saque(1000)
print(novaConta)
    