import utils

"""
import moduloconnombrelargo as m

m.función()  //Esto es igual a poner moduloconnombrelargo.función()
"""
country_list = [
    {
        "Country" : "Colombia",
        "Population" : 100
    },
    {
        "Country" : "Panamá",
        "Population" : 250
    }
]

def run():
    keys, values = utils.get_population()
    print(keys, values)

    print(utils.x)

    election = input("Ingresa el país a investigar: ").capitalize()
    my_country = utils.population_by_country(election, country_list)
    print(my_country)

print ("Este texto se imprime si no está dentro de una función")

if __name__ == "__main__": #De esta manera se puede ejecutar este modulo como script al ser llamado en consola
    run()
