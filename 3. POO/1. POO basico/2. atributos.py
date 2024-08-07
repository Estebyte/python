class Celular:
    def __init__(self, marca, modelo, camara):
        #self hace referencia al mismo objeto que se creará con la clase.
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

        #Atributos de intancia, creados al intanciar una clase (crear un objeto).
    
celular1 = Celular("Samsung", "S23", "48MP")
print(celular1.marca, celular1.modelo, celular1.camara)

celular2 = Celular("Apple", " Iphone 15", "36MP")
print(celular2.marca, celular2.modelo, celular2.camara)