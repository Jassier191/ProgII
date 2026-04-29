a = 200
b = 33
if b > a:
    print("b es mas grande que a")
else:
    print("b no es mas grande que a")

# Asignando True a b
b = True
if b:
    print("b es True")
else:
    print("b es False")

# 1. Literal de bytes (forma mas comun)
mi_byte = b"\xFF"

# 2. Constructor bytes a partir de un entero
mi_byte_dos = bytes([255])
# Verificacion
print(type(mi_byte))   # <class 'bytes'>
print(mi_byte[0])      # 255