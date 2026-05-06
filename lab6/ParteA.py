edad = 20
if edad >= 18:
 print("Eres adulto")
 print("Puedes ir a votar en las elecciones")
 print("Tienes todos los derechos legales")

 calificacion = 75
if calificacion >= 90:
 print("Resultado: A")
elif calificacion >= 80:
 print("Resultado: B")
elif calificacion >= 70:
 print("Resultado: C")
elif calificacion >= 60:
 print("Resultado: D")

 a = 200
b = 33
if a > b: print("a mayor que b")

a = 200
b = 33
c = 500
if a > b or a > c:
 print("Al menos una de las condiciones es Verdadera")

dia = 4
match dia:
 case 1:
   print("Lunes")
 case 2:
   print("Martes")
 case 3:
   print("Miercoles")
 case 4:
   print("Jueves")
 case 5:
   print("Viernes")
 case 6:
   print("Sabado")
 case 7:
   print("Domingo")