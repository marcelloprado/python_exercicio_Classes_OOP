#    1. Classe Bola: 
#       Crie uma classe que modele uma bola:
# a.	Atributos: Cor, circunferência, material
# b.	Métodos: trocaCor e mostraCor

#* Crio a classe e passo os parâmetros
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        
        #* crio os métodos
    def troca_cor(self, nova_cor):
        self.cor = nova_cor
    
    def mostrar_cor(self):
        print(f"A cor atual da bola é {self.cor}")
        
#* Criando um objeto de classe bola
bola1 = Bola("Azul", "25cm", "Tecido")
   
#* Mostrando a cor atual 
bola1.mostrar_cor()

#* Trocando a cor para Vermelha
bola1.troca_cor("Vermelha")

#* Mostrando a nova cor
bola1.mostrar_cor()

# class Bola:
#     def __init__(self, cor, circunferencia, material):
#         self.cor = cor
#         self.circunferencia = circunferencia
#         self.material = material

#     def trocaCor(self, nova_cor):
#         self.cor = nova_cor

#     def mostraCor(self):
#         print(f"A cor da bola é {self.cor}")

# #Criando um objeto de classe bola
# bola1 = Bola("azul", "25cm", "tecido")

# #Mostrando a cor atual
# bola1.mostraCor()

# #Trocando a cor
# bola1.trocaCor("Vermelha")

# #mostrando nova cor
# bola1.mostraCor()

