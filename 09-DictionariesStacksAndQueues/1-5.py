countries = [
{"name":"Poland", "population":38000000},
{"name":"Japan", "population":123488000},
{"name":"Germany", "population":84480000},
{"name":"France", "population":68170000},
{"name":"Sweden", "population":10000000}
]

print(f"{'COUNTRY'} {'POPULATION'}")

for country in countries:
    print(f'{country["name"]} {country["population"]}')