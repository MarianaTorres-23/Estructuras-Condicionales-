print("Clasificación de Triángulos")
a = float(input("Ingresa la longitud del lado 1: "))
b = float(input("Ingresa la longitud del lado 2: "))
c = float(input("Ingresa la longitud del lado 3: "))

if a == b == c:
    print("El triángulo es equilátero.")
elif a == b or a == c or b == c:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")