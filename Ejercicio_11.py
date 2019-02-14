class Alumno():
    def __init__(self, numero, nombre, nota1, nota2, nota3):
        self.numero = numero
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    def calculo_promedio(self):
        promedio = (self.nota1 + self.nota2 + self.nota3) / 3
        if promedio < 4.8 :
            print("El alumno ha suspendido")
        else:
            print("El alumno ha aprobado")

        return promedio


alum = Alumno (23, "Juanito", 5, 4, 6)

print(alum.calculo_promedio())
