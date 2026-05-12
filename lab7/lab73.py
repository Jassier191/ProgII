import string
def contar_palabras_unicas(texto):
   texto = texto.lower()
   texto = texto.translate(str.maketrans("", "", string.punctuation))
   palabras = texto.split()
   unicas = set(palabras)
   return len(unicas)
def palabra_mas_larga(texto):
   texto = texto.translate(str.maketrans("", "", string.punctuation))
   palabras = texto.split()
   return max(palabras, key=len)
def frecuencia_caracteres(texto):
   texto = texto.lower().replace(" ", "")
   texto = texto.translate(str.maketrans("", "", string.punctuation))
   total = len(texto)
   frecuencia = {}
   for letra in texto:
       frecuencia[letra] = frecuencia.get(letra, 0) + 1
   return {letra: (cantidad, round((cantidad / total) * 100, 2)) for letra, cantidad in sorted(frecuencia.items())}
# Flujo principal
texto = input("Ingrese una cadena de texto: ")
print("\n===== REPORTE DE TEXTO =====")
print(f"Palabras unicas:     {contar_palabras_unicas(texto)}")
print(f"Palabra mas larga:   {palabra_mas_larga(texto)}")
print("\nFrecuencia de caracteres:")
for letra, (cantidad, porcentaje) in frecuencia_caracteres(texto).items():
   print(f"  '{letra}': {cantidad} veces ({porcentaje}%)")
print("============================")