def get_population(country):
    result = {
    age[:4] : int(population) for (age, population) in country.items() 
    if "Population" in age and not "World Population Percentage" in age
    }
    return result


def population_by_country(country, data):
    result = list(filter(lambda i: i["Country/Territory"] == country, data))
    return result
