country_names = input().split(', ')
capital_cities = input().split(', ')

result = {country_names[i] : capital_cities[i] for i in range(len(country_names))}

for country, capital in result.items():
    print(f'{country} -> {capital}')