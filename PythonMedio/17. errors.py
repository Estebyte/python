# AssertionError

def assert_error(x, y):
    sum = x + y
    assert sum == 10, "La suma de los dos numeros debería dar 10" 
    # Siempre se deberia cumplir
    

# raise Exception

def valid_age(age):
    if age < 18:
        raise Exception("No se permiten menores de edad")

assert_error(5, 5)
valid_age(18)

# Estos errores cortan el flujo del programa

print("Este texto debería verse si no hay ningún error")