def factorial(n):
   resultado = 1
   for i in range(1, n + 1):
       resultado *= i
   return resultado
n = int(input("Ingrese un numero: "))
print(f"El factorial de {n} es: {factorial(n)}")