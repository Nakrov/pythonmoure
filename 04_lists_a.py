### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, 'Brais', 'Moure']

print(type(my_other_list))
print(type(my_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))
# print(my_other_list[-5]) IndexError
# print(my_other_list[4]) IndexError

age, height,name,surname = my_other_list
print(name)

name, height, age, name = my_other_list[2], my_other_list[1], my_other_list[0   ], my_other_list[3]
print(age)

print(my_list + my_other_list)
# print(my_list - my_other_list)

my_other_list.append('MoureDev')
print(my_other_list)

my_other_list.insert(1, 'Rojo')
print(my_other_list)

my_other_list[1] = 'Azul'
print(my_other_list)

my_other_list.remove('Azul')
print(my_other_list)

my_list.remove(30) # eliminamos un elemento que conocemos que esta adentro
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2) # no se usa en un inidice en concreteo se suele usar apra desapilar el ultimo elemento usando un pop generico .pop()
print(my_pop_element)
print(my_list)

del my_list[2] # elimina por idice
print(my_list)

my_new_list = my_list.copy()

my_list.clear() # elimna el primero que encuentra
print(my_list)
print(my_new_list)

my_new_list.reverse() # Da vuelta el oreden de la lista lo ultimo va primero y lo primero al ultimo
print(my_new_list)

my_new_list.sort() # Podemos indicar criterios para orednar o si no oredena sola de menos a mayor
print(my_new_list)

print(my_new_list[1:3])


my_list = 'Hola Python'
print(my_list)
print(type(my_list)) # Python tiene un tipado dinamico, se pueden trabajar con diferente tipos de datos y se pueden cambiar

