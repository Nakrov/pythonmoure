# 1. Realiza las siguientes operaciones aritmÃ©ticas:
# â€¢	Suma: 15 + 25
# â€¢	Resta: 50 - 22
# â€¢	MultiplicaciÃ³n: 8 * 7
# â€¢	DivisiÃ³n: 100 / 20

print('15 + 25 =', 15 + 25 )
print('50 - 22 =', 50 - 22)
print('8 * 7 =', 8 * 7)
print('100 / 20 =', 100 / 20)


# 2. Calcula el resto de la divisiÃ³n de 37 entre 5 y almacÃ©nalo en una variable remainder. Luego imprÃ­melo.

resto = 37 % 5
print ('37 % 5 =', resto)

# 3. Convierte el nÃºmero 7 en una cadena de texto y concatÃ©nalo con la frase â€œ es mi nÃºmero favoritoâ€. Imprime el resultado.

num_str = str(7)
print('Mi numero favorito es:', num_str)

# 4. Repite la palabra â€œPythonâ€ 10 veces usando el operador de multiplicaciÃ³n para cadenas y luego imprÃ­mela.

print("Python" * 10)

# 5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si a es mayor que b y almacena el resultado en una variable booleana resultado. Imprime el valor de resultado.

a = 12
b = 8
difrencia = a > b
print(difrencia)

# 6. Compara dos cadenas de texto (â€œappleâ€ y â€œbananaâ€) usando los operadores > y < y explica cuÃ¡l tiene mayor orden alfabÃ©tico.


dif1 = 'apple' > 'banana'
dif2 = 'apple' < 'banana'

print(dif1)
print(dif2)
print('Banana tiene mayor orden alfabetico')

# 7. Realiza una comparaciÃ³n lÃ³gica usando and para verificar si el nÃºmero 10 es mayor que 5 y menor que 20. Imprime el resultado.

dif1 = 10 > 5
dif2 = 10 > 20

print(dif1 and dif2)

# 8. Usa el operador or para verificar si el nÃºmero 7 es menor que 3 o mayor que 5. Imprime el resultado.

dif1 = 7 < 3
dif2 = 7 > 5

print(dif1 or dif2)

# 9. Aplica el operador not para invertir el resultado de la comparaciÃ³n 15 > 20. Â¿CuÃ¡l es el resultado?

dif = 15 > 20
print(not dif)

# 10. Combina operadores aritmÃ©ticos y lÃ³gicos: Verifica si el nÃºmero resultante de la expresiÃ³n (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.

operat = 5 * 3 + 2
dif1 = operat > 2
dif2 = operat < 20

print( dif1 and dif2)

print('Python' > 'Java')