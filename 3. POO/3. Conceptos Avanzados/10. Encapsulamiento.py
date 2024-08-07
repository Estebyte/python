"""
Es proteger metodos o argumentos de una clase, 
haciendolos privados, similar al Public/Private de otros lenguajes.
"""

class Miclase:
    def __init__(self):
        self.__atributoPrivado = "Valor" #__ para Encapsular
        self._atributoNoTanPrivado = "Queso" 
        """
        Usar un _ no tiene un efecto directo en el programa, es mas una conveción 
        para indicar que el argumento/metodo no debe ser accedido/modificado directamente.
        """
    def __saludar(self):
        print("Hola")

objeto = Miclase()
print(objeto._atributoNoTanPrivado)
#print(objeto.__atributoprivado)  ==> AttributeError: 'Miclase' object has no attribute '__atributoprivado'
#objeto.__saludar()  ==> AttributeError: 'Miclase' object has no attribute '__saludar'
