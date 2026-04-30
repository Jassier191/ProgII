datos = bytearray(b"Hola Mundo")
vista = memoryview(datos)
vista[0] = 104 
print(datos) 

archivo_binario = bytearray(range(100))
parte = memoryview(archivo_binario)[10:20]
print(parte.tolist)