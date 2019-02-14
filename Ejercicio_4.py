class Fraccion():
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def get_numerador():
        return numerador
        
    def get_denominador():
        return denominador
    
    def get_sumar(self,fraccion):
        numerador1 = self.get_numerador()
        denominador1 = self.get_denominador()
        numerador2 = fraccion.get_numerador()
        denominador2 = fraccion.get_denominador()
        return (numerador1/denominador1)+(numerador2/denominador2)
    
    def get_restar(self,fraccion):
        numerador1 = self.get_numerador()
        denominador1 = self.get_denominador()
        numerador2 = fraccion.get_numerador()
        denominador2 = fraccion.get_denominador()
        return (numerador1/denominador1)-(numerador2/denominador2)
        
    def get_multiplicar(self,fraccion):
        numerador1 = self.get_numerador()
        denominador1 = self.get_denominador()
        numerador2 = fraccion.get_numerador()
        denominador2 = fraccion.get_denominador()
        return (numerador1 * numerador2)/(denominador1*denominador2)
    
    def get_dividir(self,fraccion):
        numerador1 = self.get_numerador()
        denominador1 = self.get_denominador()
        numerador2 = fraccion.get_numerador()
        denominador2 = fraccion.get_denominador()
        return (numerador1/denominador1)/ (numerador2/denominador2)
        
    


fraccion1 = Fraccion(3,4)
fraccion2 = Fraccion(1,2)

print(fraccion1.sumar(fraccion2))
print(fraccion1.restar(fraccion2))
print(fraccion1.multiplicar(fraccion2))
print(fraccion1.dividir(fraccion2))
