edad = int(input("Ingresa tu edad: "))

if edad < 12:
    print("El costo de la entrada es: $50")
elif edad <= 17:
    print("El costo de la entrada es: $80")
else:
    print("El costo de la entrada es: $120")