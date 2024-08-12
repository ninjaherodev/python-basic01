set_paises = {'col','mex', 'bol'}
print(set_paises)
print(type(set_paises))

set_from_string = set('hola')
print(set_from_string)

set_from_tuples = set(('abc','cbv','as','abc'))
print(set_from_tuples)

album_set_1 = {"AC/DC", "Back in Black", "Thriller"}
album_set_2 = {"AC/DC", "Back in Black", "The Dark Side of the Moon"}
# add
album_set_1.add('Save to Willy')
album_set_1.update({'per','col','ven'})
album_set_1.remove('col')
album_set_1.discard('col')
print(album_set_1)
print(album_set_2)
print(len(album_set_1))
print(len(album_set_2))
print('AC/DC' in album_set_1)


#unir dos sets
print(album_set_1  | album_set_2) #print(album_set_1.union(album_set_2))
#interseccion
print(album_set_1  & album_set_2) #print(album_set_1.intersection(album_set_2))
#Diferencia
print(album_set_1 - album_set_2) #print(album_set_1.difference(album_set_2))
#Diferencia Simetrica
print(album_set_1 ^ album_set_2) #print(album_set_1.symmetric_difference(album_set_2))
#Pregunta si album_set_1 es super conjunto de album_set_2
set(album_set_1).issuperset(album_set_2)
#Pregunta si album_set_1 es subconjunto de album_set_2
set(album_set_1).issubset(album_set_2)  

print('---------' * 10)

print({"A","A"})
print({'a','b'} & {'a'})