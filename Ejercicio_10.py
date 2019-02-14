class Rectangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calculo_area(self):
        return self.base * self.altura
    def calculo_perimetro(self):
        return 2*self.base + 2*self.altura

rect = Rectangulo(base = 10, altura = 2)

print(rect.calculo_area())
print(rect.calculo_perimetro())

class PruebaRectangulo():
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura
    def set_altura(self, nuevaltura):
        self.altura = nuevaltura
    def set_base(self,base):
        self.base = nuevabase
