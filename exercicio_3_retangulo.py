# 3.	Classe Retangulo: Crie uma classe que modele um retângulo:
    # a.	Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
    # b.	Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
    # c.	Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um local. 
    # Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.


class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def mudar_valor_lado(self, novo_lado_base, novo_lado_altura):
        self.base = novo_lado_base
        self.altura = novo_lado_altura
        
    def retornar_valor_lado(self):
        return self.base, self.altura
    
    def calcular_area(self):
        total_area = self.base * self.altura
        return total_area
    
    def calcular_perimetro(self):
        total_perimetro = 2 * (self.base + self.altura)
        return total_perimetro
    
valor_base = float(input("Digite o valor da Base: "))
valor_altura = float(input("Digite o valor da Altura: "))

retangulo1 = Retangulo(valor_base, valor_altura)

area = retangulo1.calcular_area()
perimetro = retangulo1.calcular_perimetro()

print(f"Área: {area} m²")
print(f"Perímetro: {perimetro} m²")

print(f"Quantidade de piso necessário: {area:.2f}")
print(f"Quantidade de rodpés necessario: {perimetro:.2f}")