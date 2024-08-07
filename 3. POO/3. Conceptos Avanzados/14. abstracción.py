class Auto():
    def __init__(self):
        self.estado = "apagado"

    def encender_auto(self):
        self.estado = "encendido"
        print("El auto está encendido")

    def conducir(self):
        if self.estado == "apagado":
            self.encender_auto()
        
        print("Conduciendo Auto")

mi_auto = Auto()

mi_auto.conducir()

#Se esta abstrayendo el codigo, ocultando al usuario toda la logica interna.