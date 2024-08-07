class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self, respuesta):
        if respuesta == "estudiar":
            print(f"El estudiante {self.nombre} esta estudiando...")
        else:
            print("Ponete a estudiar vago de mierda")

print("Hola, A continuación, por favor presenta:")

nombre = input("Tu nombre: ")
edad = int(input("Tu edad: "))
grado = input("Tu grado: ")
estudiar_o_no = input('Ahora escribe "estudiar" si quieres estudiar: ').lower()

estudiante1 = Estudiante(nombre, edad, grado)
estudiante1.estudiar(estudiar_o_no)