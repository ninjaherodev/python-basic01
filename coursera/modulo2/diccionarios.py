import json
mi_dict = {}
print(type(mi_dict))

my_dict = {
    "name": "Fabio",
    "lastName": "Rojas",
    "age": 40,
    "lang": ["python","javascript","rust","php","java","c","c#"]
}

print(my_dict['age'])
print(my_dict.get('age'))
print('age' in my_dict )
print('estatura' in my_dict )
my_dict['name'] = 'santi'
my_dict['age'] -= 10
my_dict['lang'].append('go')
del my_dict['lastName']
my_dict.pop('name')
print('items:', my_dict.items())
print('keys:', my_dict.keys())
print('values:', my_dict.values())
print(my_dict)
my_dict.update({'age': 45}) 
print(my_dict)

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
print(Dict)
print(Dict[(0,1)])
release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
print(json.dumps(release_year_dict, indent=8))
print(release_year_dict['Thriller'] )
print(release_year_dict['The Bodyguard'])
print(release_year_dict.keys() ) 
print(release_year_dict.values() )
release_year_dict['Graduation'] = '2007'
release_year_dict
print(release_year_dict)
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
print(release_year_dict)
print(json.dumps(release_year_dict, indent=8))
print('The Bodyguard' in release_year_dict)

dic =  {"a":1,"b":2}
print(dic.keys())
Dict={"A":1,"B":"2","C":[3,3,3],"D":(4,4,4),'E':5,'F':6}
print(Dict["D"])