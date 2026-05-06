# Definición manual
matriz = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
]
# Generación automática (Matriz identidad de 3x3)
n = 3
identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
for fila in matriz:
   for elemento in fila:
       print(elemento, end="\t")
   print() # Salto de línea al terminar la fila

miTupla = ("asignacion", "laboratorio", "python")
myit = iter(miTupla)
print(next(myit))
print(next(myit))
print(next(myit))
mystr = "casa"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
for x in mystr:
 print(x)

import datetime
x = datetime.datetime.now()
print(x)
#retorna en formato: año, mes, día, hora, minuto, segundo y microsegundo.
print(x.year)
print(x.strftime("%A"))
#imprime año y dia de semana en ingles
y = datetime.datetime(2010, 5, 11)
print(y)
#crear fecha personalizada con formado año, mes, dia

print("Ingrese su nombre:")
nombre = input()
print(f"Hola {nombre}")
nombre = input("Ingrese su nombre:")
print(f"Hola {nombre}")

nombre = input("Ingrese su nombre:")
print(f"Hola {nombre}")
fav1 = input("Cual es la marca de computadora favorita? ")
fav2 = input("De que color le gusta? ")
fav3 = input("Cuantas ha tenido hasta ahora? ")
print(f"Quieres una {fav1} {fav2} con {fav3} nucleos?")

y = True
while y == True:
 x = input("Ingrese un numero:")
 try:
   x = float(x);
   y = False
 except:
   print("Entrada incorrecta, intentelo de nuevo")
print("Gracias!")

