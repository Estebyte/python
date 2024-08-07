"""
Principio Abierto/Cerrado:
Las entidades de software (clases, modulos, funciones, etc...) 
tienen que estar abiertas para la extensión y cerradas para la modificación.

Open for extension, Closed for Modify
"""
#Programa para enviar notificaciones al usuario
from abc import ABC, abstractmethod

class User(ABC): #Hacer abstracta la clase usuario para cerrar su modificación
    def __init__(self, username):
        self.username = username

    @abstractmethod
    def notificar(self): #Tambien es posible hacer un raise NotImplementedError
        pass

class WhatsappNotification(User):
    def __init__(self, username, number):
        super().__init__(username)
        self.number = number

    def notificar(self):
        print(f"Sending mensage to {self.username}'s number: {self.number}")

class EmailNotification(User):
    def __init__(self, username, email):
        super().__init__(username)
        self.email = email

    def notificar(self):
        print(f"Sending email to {self.username}'s mail: {self.email}")

user_1 = WhatsappNotification("EstebanCrack777", 12345678)
user_1.notificar()

user_2 = EmailNotification("IsaacNewton43", "mrgravity@gmail.com")
user_2.notificar()

"""
De esta manera, podriamos seguir extendiendo el codigo agregando plataformas,
sin modificar la clase principal
"""