# Activity 6-11 cities
cities = {
    'cainta': {
        'country': 'philippines',
        'population': 100_000,
        'fact': 'Cainta specialty is sumbintik'
    },
    'manila': {
        'country': 'philippines',
        'population': 300_000,
        'fact': 'capital of the philippines'
    }
}

for city, value in cities.items():
    print(f"City: {city.title()}")
    print(f"Country: {value['country'].title()}")
    print(f"Population: {value['population']}")
    print(f"Fact: {value['fact']}")
    
