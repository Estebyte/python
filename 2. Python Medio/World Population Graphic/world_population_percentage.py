import csv_reader
import charts

def select_continent(continent="World Wide"):
    world_wide_data = csv_reader.read_csv("Python/PythonMedio/World Population Graphic/world_population.csv")
    continets = set(i["Continent"] for i in world_wide_data)
    if continent in continets:
        continent_data = list(filter(lambda x: x["Continent"] == continent, world_wide_data))
        return continent_data
    else:
        return world_wide_data



def run():
    print("Select the continent, (If you do not select one, the chart will be done with the world wide data) ")
    data = select_continent(input("=>"))
    countries = list(map(lambda x: x["Country/Territory"], data))
    percentages = list(map(lambda x: x["World Population Percentage"], data))
    charts.generate_pie_chart(countries, percentages)

if __name__ == "__main__":
    run()

