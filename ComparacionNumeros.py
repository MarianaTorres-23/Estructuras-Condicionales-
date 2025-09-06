x = float(input("Ingresa el primer número: "))
y = float(input("Ingresa el segundo número: "))
z = float(input("Ingresa el tercer número: "))
mayor = x
if y > mayor:
    mayor = y
if z > mayor:
    mayor = z
menor = x
if y < menor:
    menor = y
if z < menor:
    menor = z
print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")