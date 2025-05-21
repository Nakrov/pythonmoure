### Strings ###

my_string = 'Mi String'
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + ' ' + my_other_string)

my_new_line_string = 'Este es un Sting\ncon salto de lines'
print(my_new_line_string)

my_tab_sting = '\tEste es un String \n escapado'
print(my_tab_sting)

my_scape_string = '\\tEste es un String \\n escapado'
print(my_scape_string)

# Formateo

name, surname, age = 'Brais', 'Moure', 35

print('Mi nombre es {} {} y mi edad es {}'.format(name, surname, age))
print('Mi nombre es %s %s y mi edad es %d' %(name, surname, age))
print('mi nombre es ' + ' ' + surname + ' y mi edad es ' + str(age)) # es muy engorrozo
print(f'Mi nombre es {name} {surname} y mi edad es {age}')


# Desempaquetado de caracteres
language = 'python'
a, b, c, d, e, f = language
print(a)
print(e)


# Division

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize()) # primera en mayusculas
print(language.upper()) # todo en mayusculas
print(language.count('t')) # cantidad de veces que se repite la letra
print(language.isnumeric()) # pregunta si es numerico
print('1'.isnumeric())
print(language.lower()) # todo en minusculas
print(language.lower().isupper()) # pone en mayusculas y luego pregunta si esta en mayusculas
print(language.startswith('Py'))