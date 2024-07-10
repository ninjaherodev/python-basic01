# Curso Basico Python

## Temas de Python

- [Curso Basico Python](#curso-basico-python)
  - [Temas de Python](#temas-de-python)
  - [Instalación](#instalación)
  - [String](#string)
    - [Indexación](#indexación)
  - [Métodos de Transformación](#métodos-de-transformación)
    - [Count](#count)
    - [Lower](#lower)
    - [Capitalize](#capitalize)
    - [Title](#title)
    - [Strip](#strip)
    - [Lstrip](#lstrip)
    - [Rstrip](#rstrip)
    - [Replace](#replace)
  - [Métodos de Consulta](#métodos-de-consulta)
    - [Find](#find)
    - [Index](#index)
    - [Count](#count-1)
    - [Startswith](#startswith)
    - [Endswith](#endswith)
  - [Métodos de Formateo](#métodos-de-formateo)
    - [Center](#center)
    - [Ljust](#ljust)
    - [Rjust](#rjust)
  - [Métodos de División y Unión](#métodos-de-división-y-unión)
    - [Split](#split)
    - [Rsplit](#rsplit)
    - [Join](#join)
    - [Partition](#partition)
    - [Rpartition](#rpartition)
  - [Métodos de Validación](#métodos-de-validación)
    - [Isalpha](#isalpha)
    - [Isdigit](#isdigit)
    - [Isalnum](#isalnum)
    - [Isspace](#isspace)
    - [Islower](#islower)
    - [Isupper](#isupper)
    - [Istitle](#istitle)
  - [Otros Métodos](#otros-métodos)
    - [Zfill](#zfill)
    - [Encode](#encode)
    - [Decode](#decode)

## Instalación

Para instalar Python, sigue estos pasos:

1. Dirígete a la [página oficial de descargas de Python](https://www.python.org/downloads/).
2. Descarga el instalador correspondiente a tu sistema operativo.
3. Sigue las instrucciones de instalación.

## String

Un string en Python es una secuencia de caracteres. Puedes definir un string de tres maneras
1. usando comillas simples (') 
2. usando comillas dobles (")
3. usando commilas triples (''') que me permite tener saltos de lieneas

```python
name = "fabio"   #usando comillas dobles
character = 'c'  #usando comillas simples
prueba = '''hola
como estas?
espero que bien
'''

print(prueba)
print(type(name))
print(type(character))
```
### Indexación

La indexación en Python te permite acceder a caracteres individuales en un string mediante su posición. En Python, la indexación comienza desde `0`.

Ejemplo de indexación:

```python
texto = "Hola mundo"

# Acceder al primer caracter
primer_caracter = texto[0]
print(f"Primer caracter: {primer_caracter}")  # Imprime: H

# Acceder al último caracter
ultimo_caracter = texto[-1]
print(f"Último caracter: {ultimo_caracter}")  # Imprime: o
```

## Métodos de Transformación

### Count
Devuelve el número de veces que `sub` aparece en la cadena.
```python
"hola mundo".count("o")  # 2
```
### Lower
Convierte todos los caracteres de la cadena a minúsculas.

```python
"Hola Mundo".upper()  # 'HOLA MUNDO'
```
### Capitalize
Convierte el primer carácter de la cadena a mayúscula y el resto a minúsculas.

```python
"hola mundo".capitalize()  # 'Hola mundo'
```
### Title
Convierte el primer carácter de cada palabra a mayúscula.

```python
"hola mundo".title()  # 'Hola Mundo'
```

### Strip
Elimina los caracteres al principio y al final de la cadena. Si no se especifica chars, elimina espacios en blanco.

```python
"  hola mundo  ".strip()  # 'hola mundo'
```

### Lstrip
Elimina los caracteres al principio de la cadena. Si no se especifica chars, elimina espacios en blanco.

```python
"  hola mundo  ".lstrip()  # 'hola mundo  '
```

### Rstrip
Elimina los caracteres al final de la cadena. Si no se especifica chars, elimina espacios en blanco.

```python
"  hola mundo  ".rstrip()  # '  hola mundo'
```
### Replace
Reemplaza todas las apariciones de old por new. Si se especifica count, solo reemplaza count veces.

```python
"hola mundo".replace("mundo", "Python")  # 'hola Python'
```
## Métodos de Consulta

### Find
Devuelve el índice más bajo en el que se encuentra la subcadena sub dentro de la cadena, o -1 si no se encuentra.

```python
"hola mundo".find("mundo")  # 5
```
### Index
Similar a find(), pero lanza una excepción ValueError si sub no se encuentra.

```python
"hola mundo".index("mundo")  # 5
```
### Count
Devuelve el número de veces que sub aparece en la cadena.

```python
"hola mundo".count("o")  # 2
```

### Startswith
Devuelve True si la cadena comienza con el prefijo prefix.

```python
"hola mundo".startswith("hola")  # True
```

### Endswith
Devuelve True si la cadena termina con el sufijo suffix.

```python
"hola mundo".endswith("mundo")  # True
```

## Métodos de Formateo

### Center
Devuelve una cadena centrada en una cadena de longitud width, rellenada con fillchar (espacio por defecto).

```python
"hola".center(10, '*')  # '***hola***'
```
### Ljust
Devuelve una cadena alineada a la izquierda en una cadena de longitud width, rellenada con fillchar (espacio por defecto).

```python
"hola".ljust(10, '-')  # 'hola------'
```
### Rjust
Devuelve una cadena alineada a la derecha en una cadena de longitud width, rellenada con fillchar (espacio por defecto).

```python
"hola".rjust(10, '-')  # '------hola'
```

## Métodos de División y Unión

### Split
Divide la cadena en una lista usando sep como delimitador. Si no se especifica sep, se usan espacios en blanco.

```python
"hola mundo".split()  # ['hola', 'mundo']
```
### Rsplit
Divide la cadena en una lista, comenzando por el final.
```python
"uno, dos, tres".rsplit(', ', 1)  # ['uno, dos', 'tres']
```
### Join
Une los elementos de iterable con la cadena como delimitador.
```python
", ".join(["uno", "dos", "tres"])  # 'uno, dos, tres'
```
### Partition
Divide la cadena en una tupla de tres elementos: la parte antes de sep, sep y la parte después de sep.
```python
"hola mundo".partition(" ")  # ('hola', ' ', 'mundo')
```
### Rpartition
Divide la cadena en una tupla de tres elementos, comenzando por el final.
```python
"uno, dos, tres".rpartition(", ")  # ('uno, dos', ', ', 'tres')
```
## Métodos de Validación

### Isalpha
Devuelve True si todos los caracteres de la cadena son letras.
```python
"hola".isalpha()  # True
```
### Isdigit
Devuelve True si todos los caracteres de la cadena son dígitos.
```python
"12345".isdigit()  # True
```
### Isalnum
Devuelve True si todos los caracteres de la cadena son letras o dígitos.
```python
"hola123".isalnum()  # True
```
### Isspace
Devuelve True si todos los caracteres de la cadena son espacios en blanco.
```python
"   ".isspace()  # True
```
### Islower
Devuelve True si todos los caracteres de la cadena son minúsculas.
```python
"hola".islower()  # True
```
### Isupper
Devuelve True si todos los caracteres de la cadena son mayúsculas.
```python
"HOLA".isupper()  # True
```
### Istitle
Devuelve True si la cadena está en formato de título (inicial de cada palabra en mayúscula).
```python
"Hola Mundo".istitle()  # True
```

## Otros Métodos

### Zfill
Devuelve una copia de la cadena rellenada con ceros a la izquierda para alcanzar una longitud de width.
```python
"42".zfill(5)  # '00042'
```

### Encode
Devuelve una versión codificada de la cadena.
```python
"hola".encode()  # b'hola'
```

### Decode
Devuelve una versión decodificada de los bytes.
```python
b'hola'.decode()  # 'hola'
```
