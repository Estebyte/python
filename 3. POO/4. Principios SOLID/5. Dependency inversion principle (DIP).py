"""
Principio de Inversión de Dependecias:

1. Los modulos de alto nivel no deben depender de los modulos de bajo nivel, 
si no ambos deben depender de las abstracción.

2. Las abstracciones no deben depender de los detalles, si no los detalles deben
depender de estas.

No hay que depender de implementaciones especificas.
"""
"""
class SMS:
    def notify(self):
        print("Sms notification...")

class Email:
    def notify(self):
        print("Email notification...")

class PushNotification:
    def notify(self):
        print("Push Notification...")

class Notification:
    def sms_notification(self, sms = SMS()):
        sms.notify()

    def email_notification(self, email = Email()):
        email.notify()
    
    def push_notification(self, push = PushNotification()):
        push.notify()

notification = Notification()
notification.sms_notification()
notification.email_notification()
notification.push_notification()

Este codigo viola el principio de inversión de dependecias, ya que la clase de alto nivel,
Notification, esta dependiendo de las clases de bajo nivel SMS(), Email(), PushNotification()   
Por lo que si se quisiera expandir el codigo, habria que modificar la clase principal.

Una posible solución puede ser:
"""

from abc import ABC, abstractmethod

class NotificationChannel(ABC):  
    @abstractmethod
    def send(self):
        pass

class SMS(NotificationChannel):
    def send(self):
        print("SMS Notification...")

class Email(NotificationChannel):
    def send(self):
        print("Email Notification...")

class PushNotification(NotificationChannel):
    def send(self):
        print("Push Notification...")

class Notification():
    def notify(self, other):
        other.send()

#Crear instancias de los canales
sms = SMS()
email = Email()
push = PushNotification()

#Crear instancia de Notification()
notification = Notification()

#Probar el metodo notify()
notification.notify(sms)
notification.notify(email)
notification.notify(push)

"""
De esta manera, tanto la clase Notification() como las clases SMS(), Email(), y PushNotification()
dependen de la clase abstracta NotificationChannel(), dando asi la posibilidad de un codigo expandible y 
facilmente legible.
"""