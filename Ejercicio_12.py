class Coche():
    def __init__(self, color, marca, modelo, caballos, puertas, matricula):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.caballos = caballos
        self.puertas = puertas
        self.matricula = matricula
    
    def get_color(self):
        return self.color
    
    def get_marca(self):
        return self.marca
    
    def get_modelo(self):
        return modelo
    
    def get_caballos(self):
        return caballos
        
    def get_puertas(self):
        return puertas
    
    def get_matricula(self):
        return matricula

class PruebaCoche(Coche):
    def __init__(self, color, marca, modelo, caballos, puertas, matricula):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.caballos = caballos
        self.puertas = puertas
        self.matricula = matricula     

    def set_color(self, otrocolor):
        self.color = otrocolor
        
coche = PruebaCoche("Negro", "BMW", "X5", 400, 4, "HOLAQTAL")
print("El color del coche es: ", coche.get_color())
print("La marca del coche es: ", coche.get_marca())
print("El modelo del coche es: ", coche.get_modelo())
print("El numero de caballos del coche es: ", coche.get_caballos())
print("El numero de puertas que tiene el coche es: ", coche.get_puertas())
print("La matricula del coche es: ", coche.get_matricula())

Otro_Color = coche.set_color("Blanco")
print("El nuevo color del coche es: ", coche.get_color())
    


fraccion1 = Fraccion(3,4)
fraccion2 = Fraccion(1,2)

print(fraccion1.sumar(fraccion2))
print(fraccion1.restar(fraccion2))
print(fraccion1.multiplicar(fraccion2))
print(fraccion1.dividir(fraccion2))
