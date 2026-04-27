x = 5
y = "Juan"
print(x)
print(y)

x = str(3)    # x será '3'
y = int(3)    # y será 3
z = float(3)  # z será 3.0
print(type(x))
print(type(y))

x = "Hola"
# es lo mismo que 
x = 'Hola'

a = 4
A = "Cuatro"
# A no remplaza a

x, y, z = "Naranja", "Pera", "Fresa"
print(x)
print(y)
print(z)

x = y = z = "Naranja"
print(x)
print(y)
print(z)

fruits = ["Manzana", "Uva", "Mandarina"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python "
y = "es "
z = "amigable"
print(x + y + z)
x = 5
y = 10
print(x + y)