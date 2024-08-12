import re
#Python sigue el orden de las operaciones (BODMASS) para realizar operaciones con expresiones múltiples.
my_string="   Hello   "
print(my_string.strip()) 
split_text = my_string.split()
print('split:',split_text)

print("AB\nC\nDE")
print("holaMike".find("Mike"))
def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.fullmatch(pattern, email))

def validate_celular(celular):
    pattern = r"\d{10}"
    return bool(re.fullmatch(pattern, celular))

s2 = "Michael Jackson was a singer and known as the 'King of Pop'"


# Use the findall() function to find all occurrences of the "as" in the string
result = re.findall("as", s2)
print(result)
split_array = re.split("\s", s2)

# The split_array contains all the substrings, split by whitespace characters
print('split_array:',split_array) 

pattern = r"King of Pop"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)
print('new_string:',new_string)

# Write your code below and press Shift+Enter to execute
str1= "The quick brown fox jumps over the lazy dog."
pattern = r"fox"
new_string = re.sub(pattern, 'bear', str1, flags=re.IGNORECASE)
#new_string = re.sub(r"fox", "bear", str1)
print(new_string)

print('es una numero de 10 digitos?',validate_celular('3183895020'))
nombre = r'Mis números favoritos son 123-4567 y 987-6543.'
regla_email= r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
print('res=>',validate_email('fabio.rojas@contraloria.gov.co'))
print('res=>',validate_email('fabiorojas7@gmail.com'))
print('res=>',validate_email('fabiorojas7gmail.com'))

pattern = r"\d{3}-\d{4}"
result = re.search(pattern, nombre)
result1 = re.findall(pattern, nombre)
result2 = re.fullmatch(pattern, nombre)

print('result:',result.group())
print('result:',result1)
print('result:',result2)

print('find:',nombre.find('elw'))
print('split:',nombre.split())
# nombre_mayus = nombre.upper()
# nombre_minuscula = nombre.lower()
# replace = nombre.replace('Michael', 'Janet')
# # character_especial = '@#_[]%$'
# print('mayus:', nombre_mayus)
# print('minus:', nombre_minuscula)
# print('reemplazo:',replace)

# # Recorrer cada carácter del nombre
# for caracter in nombre:
#     print(caracter)

# # Recorrer cada carácter del nombre con su índice
# for indice, caracter in enumerate(nombre):
#     print(f'Índice {indice}: {caracter}')

# caracteres = [caracter for caracter in nombre]
# print(caracteres)

# resultados = map(lambda caracter: caracter.upper(), nombre)
# print(list(resultados))

# resultado = '-'.join(nombre)
# print(resultado)

# print(nombre[0:7])  # Imprime 'Michael'

# #String interpolation
# name = "John"
# age = 30
# print(f"My name is {name} and I am {age} years old.")

# x = 10
# y = 20
# print(f"The sum of x and y is {x+y}.")

# #Otra forma
# name = "John"
# age = 50
# print("My name is {} and I am {} years old.".format(name, age))

# # % Operator
# name = "Johnathan"
# age = 30
# print("My name is %s and I am %d years old." % (name, age))


# #Raw String (r’’)
# regular_string = "C:\new_folder\file.txt"
# print("Regular String:", regular_string)

# raw_string = r"C:\new_folder\file.txt"
# print("Raw String:", raw_string)