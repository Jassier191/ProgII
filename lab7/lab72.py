def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
n = int(input("Ingrese un numero: "))
print(f"El factorial de {n} es: {factorial(n)}")
n = int(input("Ingrese un numero par para la matriz identidad: "))
if n % 2 != 0:
    print("El numero debe ser par.")
else:
    identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for fila in identidad:
        for elemento in fila:
            print(elemento, end="\t")
        print()