with open('ejemplo.txt', 'w') as file:
    file.write('Hola, mundo!\n')
    file.write('Esto es una prueba de escritura en un archivo de texto.')

# Leer desde un archivo de texto
with open('ejemplo.txt', 'r') as file:
    contenido = file.read()
    print(contenido)