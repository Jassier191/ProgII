# capitalize() - Convierte la primera letra en mayuscula
texto = "hola mundo"
print(texto.capitalize())  # Hola mundo
# count() - Devuelve el numero de veces que un valor aparece en la cadena
frase = "banana"
print(frase.count("a"))  # 3
# find() - Busca un valor y devuelve la posicion donde se encontro
saludo = "Hello, World!"
print(saludo.find("World"))  # 7

# isalpha() - Devuelve True si todos los caracteres pertenecen al alfabeto
texto = "Hola"
print(texto.isalpha())  # True
texto2 = "Hola123"
print(texto2.isalpha())  # False
# isdigit() - Devuelve True si todos los caracteres son digitos
numero = "12345"
print(numero.isdigit())  # True
numero2 = "123abc"
print(numero2.isdigit())  # False
# isupper() - Devuelve True si todos los caracteres estan en mayusculas
mayus = "HOLA MUNDO"
print(mayus.isupper())  # True
mezcla = "Hola Mundo"
print(mezcla.isupper())  # False

