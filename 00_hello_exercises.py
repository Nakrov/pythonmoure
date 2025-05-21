### Ejerersicio de practica ###

# 1- Imprime 'Hola Mundo!' por consola
print('Hola Mundo!')

# 2- Escribe un comentario de una sola lÃ­nea explicando que hace el codigo del Ejercicio 1

# print muestra en consola el mensaje que queramos

# 3- Imprime tu nombre y edad en la misma li­nea utilizando la funcion print

print('mi nombre es Leandro y mi edad es', 32)

# 4- Usa la funcion type() para imprimir el tipo de dato de una cadena de texto, un numero entero y un numero decimal

print(type('Hola Mundo'))
print(type(5))
print(type(1.4))

# 5- Escribe un comentario en varias li­neas explicando que son los tipos de datos en Python

'''
Estructuras que el lenguaje de programacion
ya tiene precargadas y es capas de decirnos algo
En Python, los tipos de datos mas comunes son:
- str: para cadenas de texto
- int: para numeros enteros
- float: para numeros con decimales
- bool: para valores booleanos (True/False)
'''

# 6- Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo"
print('Hola' + ' ' +  'Mundo')

# 7- Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma li­nea

name = 'Leandro'
age = 32

print('Mi nombre es:', name, 'y mi edad es:', age)

# 8- Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo

name = input('Ingrese su nombre: ')

print('Hola', name, 'que tenga un buen dia!')

# 9- Usa print() para mostrar el resultado de la suma de dos numeros enteros y el tipo de dato resultante

sum = 5 + 2

print('5 + 2 =', sum)
print(type(sum))

# 10- Comenta el codigo del Ejercicio 9, y explica que hace cada linea usando comentarios de una sola linea

# primero creo la variable 'sum'  para sumar dos valores, en este caso 5 mas 2, muestro en pantalla con print la cadena de 5 + 2 = y coloco la variable y por ultimo imprimo que tipo de valor de sum
