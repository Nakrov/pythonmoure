# 1. Declara una variable text con la frase â€œAprendiendo Pythonâ€ y luego imprime la longitud de la cadena usando len().
my_string = 'Aprendiendo Python'
print(len(my_string))

# 2. Concatena dos cadenas: â€œHolaâ€ y â€œPythonâ€, y muestra el resultado en una sola lÃ­nea.
my_string = 'Hola'
my_other_string = 'Python'
print(my_string + ' ' + my_other_string)

# 3. Crea una cadena que incluya un salto de lÃ­nea, y luego imprÃ­mela para ver el resultado.
my_string = '\nHola'
print(my_string)

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
name, surname, age = 'Leandro', 'Brito', 32
print(f'Mi nombre es {name} {surname} y mi edad es {age} años')

# 5. Desempaqueta los caracteres de la palabra â€œPythonâ€ en variables separadas y luego imprÃ­melos uno por uno.
language = 'Python'
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 6. Extrae un â€œsliceâ€ de la palabra â€œProgramaciÃ³nâ€ para obtener los caracteres desde la posiciÃ³n 3 hasta la 7.
language = 'Programacion'
language_slice = language[3:8]
print(language_slice)

# 7. Invierte la cadena â€œPythonâ€ usando slicing y muestra el resultado.
language = 'Python'
language_slice = language[::-1]
print(language_slice)

# 8. Convierte la cadena â€œaprendiendo pythonâ€ en mayÃºsculas usando el mÃ©todo adecuado e imprÃ­mela.
my_string = 'aprendiendo python'
print(my_string.upper())

# 9. Cuenta cuÃ¡ntas veces aparece la letra â€œnâ€ en la cadena â€œProgramaciÃ³n en Pythonâ€.
my_string = 'Programacion'
print(my_string.count('n'))

# 10. Verifica si la cadena â€œ12345â€ es numÃ©rica usando el mÃ©todo adecuado e imprime el resultado.
my_string = '12345'
print(my_string.isnumeric())

print('Hola Python'[0:4])