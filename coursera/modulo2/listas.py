# numbers = [1,2,3,4,5,6]
# print(numbers[3:-5])
# print(20 in numbers)
# print(type(numbers))

# task = ["revisar correos","revisar el estado de los servidores","programar"]
# print(task)

# types=[1, True, 'hola']
# print(types)
# print(numbers[0])
# print(task[0])

# texto = 'Hola' #INMUTABLES
# nuevo_texto = texto.replace('H', 'w')
# print(nuevo_texto)
# print(texto)

# task[0] = 'estudiar python'
# print(task)


# vamos a ver un crud en las listas (CREATE/READ/UPDATE/DELETE)
# CREATE
#number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# numbers = list(range(1,11))
# print(numbers)

# #UPDATE
# numbers.append(11)
# print(numbers)
# numbers.insert(3,3.5)
# print(numbers)
# listaOne = [1,2,3]
# listaTwo = [4,5,6]
# listaOne.extend(listaTwo)
# print(listaOne)
# print([*listaOne, *listaTwo])

def safe_index(list, item):
    try:
      return list.index(item)
    except ValueError:
      return -1

consolas = ['Nintendo Switch', 'xbox','play 5', 'genesis', 'dreamcast', 'Atari']
search_element = 'xbox'
index = safe_index(consolas,search_element)
if(index == -1):
   print(f'no se encontro el item {search_element} en la lista')
else:
   consolas[index] = 'Atari'
   print(consolas)


#Delete
consolas.remove('Atari')
consolas.pop()
consolas.pop(1)
# consolas.reverse()
consolas.sort()
print(consolas)

frutas = ['banana','naranja','piña','uvas']
copy = frutas
# copy2 = [fruta for fruta in frutas]
copy2 = frutas.copy()
frutas[0]='fresas'
print(frutas)
print(copy)
print(copy2)
print(frutas.count('naranja'))

numeros = [1,5,3,4,2]
print(numeros)
numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)

B=[1,2,[3,'a'],[4,'b']]
print(B[3][1])

print([1,2,3] + [1,1,1])