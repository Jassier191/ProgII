def fahrenheit_to_celsius(fahrenheit):
 return (fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

def obtener_saludo():
 return "Saludos desde una funcion en python"
mensaje = obtener_saludo()
print(mensaje)

def my_function(num):
 print("Numero " + num)
my_function("Uno")
my_function("Dos")
my_function("Tres")

def my_function(pais = "Panama"):
 print("Soy de ", pais)
my_function("Argentina")
my_function("Mexico")
my_function()
my_function("Canada")

def my_function(mascota, nombre):
 print("Tengo un", mascota)
 print("Mi", mascota + " se llama", nombre)
my_function(mascota = "perro", nombre = "Manchas")

def my_function(*kids):
 print("El niño mas joven es " + kids[2])
my_function("Pedro", "Juan", "Jose")

def my_function(*numeros):
 total = 0
 for num in numeros:
   total += num
 return total
print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

x = lambda a : a + 10
print(x(5))
x = lambda a, b : a * b
print(x(5, 6))

def my_generator():
 yield 1
 yield 2
 yield 3
for value in my_generator():
 print(value)

def contar_hasta(n):
 cuenta = 1
 while cuenta <= n:
   yield cuenta
   cuenta += 1
for num in contar_hasta(5):
 print(num)

x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)
z = pow(4, 3)
print(z)
import math
r = math.sqrt(64)
print(r)
