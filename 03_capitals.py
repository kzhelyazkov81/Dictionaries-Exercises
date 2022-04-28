countries = input().split(', ')
capitals = input().split(', ')
result = dict(zip(countries, capitals))

for key, value in result.items():
    print(f'{key} -> {value}')
