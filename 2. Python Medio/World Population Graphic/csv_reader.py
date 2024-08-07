import csv

def read_csv(path):
    with open(path, "r") as file:
        reader = csv.reader(file, delimiter=",")
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dicts = {key: value for key, value in iterable}
            data.append(country_dicts)
    return data
if __name__ == "__main__":
    print(read_csv("Python/PythonMedio/World Population Graphic/world_population.csv"))

