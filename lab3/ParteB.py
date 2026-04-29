a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

b = "Hello, World!"
print(b[2:5])
b = "Hello, World!"
print(b[:5])

a = "Hello, World!"
print(a.upper())
a = "Hello, World!"
print(a.lower())
a = " Hello, World! "
print(a.strip())

a = "Hello, World!"
print(a.replace("H", "J"))
a = "Hello, World!"
print(a.split(","))
# retorna ['Hello', ' World!']
a = "Hello"
b = "World"
c = a + b
print(c)

age = 36
txt = f"Estudio python, tengo {age} años"
print(txt)
price = 59
txt = f"El precio es {price:.2f} dolares"
print(txt)