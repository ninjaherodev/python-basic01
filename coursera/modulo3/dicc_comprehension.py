# dict = {}
# for i in range(1,5):
#     dict[i] = i*2

# print(dict)

# dict = {i: i*2 for i in range(1,5)}
# print(dict)
import random
countries = ['col','mex','bol','pe']
# population = {}
# for country in countries:
#     population[country] = random.randint(50,200)
population = {country:random.randint(50,200) for country in countries }
print(population)
# print(population.items())
result = {country:population for country,population in population.items() if population > 120}
print(result)

# names = ['nico', 'zule', "santi"]
# edades = [12,56,98]
# print(dict(zip(names,edades)))
# # new_dict=dict(zip(names,edades))
# new_dict = {name:age for name,age in zip(names,edades)}
# print(new_dict)