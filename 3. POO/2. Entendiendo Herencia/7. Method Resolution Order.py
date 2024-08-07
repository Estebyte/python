class A:
    def hablar(self):
        print("hola desde A")

class B(A):
    def hablar(self):
        print("hola desde B")

class F:
    def hablar(self):
        print("Hola desde F")

class C(F):
    def hablar(self):
        print("hola desde C")

class D(B, C):
    def hablar(self):
        print("Hola desde D")
        


miau = D()
miau.hablar()

#Acceder a metodos de clases superiores
A.hablar(miau)

print(D.mro())