import utils
import csv_reader 
import charts


def run():
    data = csv_reader.read_csv("Python/PythonMedio/World Population Graphic/world_population.csv")
    country = input("Select the country ==> ")

    country_data = utils.select_country(country, data)
    #print(country_data)

    population = utils.get_population(country_data)
    #print(population)

    labels = population.keys()
    values = population.values()
    charts.generate_bar_chart(labels, values)

if __name__ == "__main__":
    run()