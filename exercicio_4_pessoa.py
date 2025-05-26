# 4.	Classe Pessoa: Crie uma classe que modele uma pessoa:
    # a.	Atributos: nome, idade, peso e altura
    # b.	Métodos: Envelhercer, engordar, emagrecer, crescer.
    # Obs: Por padrão, a cada ano que nossa pessoa envelhece,
    # sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def envelhecer(self, anos):
        for _ in range(anos):
            if self.idade < 21:
                self.altura += 0.05
            self.idade += 1

    def engordar(self, quilos):
        self.peso += quilos
    
    def emagrecer(self, quilos):
        self.peso -= quilos
    
    def crescer(self, cm):
        self.altura += cm
        
        #* Exemplo com __repr__
    def __repr__(self):
        return (f"Pessoa(nome: ='{self.nome}' , idade: ='{self.idade} '"
                f"peso: = '{self.peso} ', altura: = '{self.altura}')")
    
        #* Exemplo com __str__ 
    def __str__(self):
        return f"{self.nome} ,{self.idade} anos,{self.peso} Kg, {self.altura:.2f}m"
        
        
pessoa1 = Pessoa("Marcello", 18, 60, 1.6)
pessoa1.envelhecer(1)
pessoa1.engordar(5)
pessoa1.emagrecer(2)
pessoa1.crescer(0.02)

print(pessoa1)
print(f"Histórico da pessoa: {pessoa1}")