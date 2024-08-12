'''
🤖 Listas en python
'''

# crear una lista

tareas = ['ir al gym', 5000, 'Estudiar', 'Mercar']

# Agregar elemento al final de la lista
tareas.append('leer un libro')
print(tareas)

#Eliminar 
tareas.remove(5000)
print(tareas)

#colocar la tarea completa
tareas[1] += ' (Completado)'
print(tareas)
