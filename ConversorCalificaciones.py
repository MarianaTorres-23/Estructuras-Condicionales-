cal = int(input("Ingresa tu calificación (0-100): "))

if cal >= 90 and cal <= 100:
    print("Tu calificación en letra es: A")
elif cal >= 80:
    print("Tu calificación en letra es: B")
elif cal >= 70:
    print("Tu calificación en letra es: C")
elif cal >= 60:
    print("Tu calificación en letra es: D")
else:
    print("Tu calificación en letra es: F")