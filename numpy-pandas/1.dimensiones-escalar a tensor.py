'''
por que numpy: 
* es 50 veces mas rapido que una lista de python o de C.
* optimiza el almacenamiento en memoria
* maneja diferente tipos de datos
'''
import numpy as np

escalar = np.array(42)
print(type(escalar))
print(escalar)

vector = np.array([30,29,35,31,33,36,42])
print(vector)

matrix = np.array([[1,2,3],[4,5,6], [7,8,9] ])
print(matrix)

tensor = np.array([[[1,2],[3,4], [5,6], [7,8]]])
print(tensor)

array_arrange = np.arange(10)
print(array_arrange)

eye_matriz = np.eye(3)
print(eye_matriz)

diag = np.diag([1,2,3])
print(diag)

ramdon = np.random.random((2,3))
print(ramdon)

random_int_array = np.random.randint(1, 100, size=(4, 4))
print(random_int_array)