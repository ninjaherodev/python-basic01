import numpy as np

array = np.array([[1,2,3],[4,5,6]])
add = np.sum(array)
print(array.ndim)
print(array.shape)
print(array.dtype)

# suma los elosmentos del array
print('add:',add)

#La media
mean = np.mean(array)
print('mean:',mean)

#desviacion estandar
std = np.std(array)
print('std:',std)

z = np.array(3, dtype=np.uint8)
print(z)

double_array = np.array([1,2,3], dtype='d')
print(double_array)


z = z.astype(np.float64)
print(z)

#Cual crees que es la principal diferencia entre el uso de lista y el uso de arrays que nos va ayudar a nosotros en los proyectos. 