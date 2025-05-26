# 2.	Classe Quadrado: Crie uma classe que modele um quadrado:
# a.	Atributos: Tamanho do lado
# b.	Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área

    #* Crio a Classe
class Quadrado:
    def __init__(self, lado):
        self.lado = lado
        
        #* crio os métodos
    def mudar_valor_lado(self, novo_valor):
      self.lado = novo_valor
    
    def retornar_valor_lado(self):
       return self.lado
      
    def calcular_area(self):
        return self.lado ** 2
        
        #* Crio os objetos
quadrado1 = Quadrado(5)
print("Área do quadrado Atual: ", quadrado1.calcular_area(), "Mts")
quadrado1.mudar_valor_lado(10)

print("Novo Lado: ", quadrado1.retornar_valor_lado(), "Mts")
print("Área do quadrado novo: ", quadrado1.calcular_area(), "Mts")
