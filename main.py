variable = int(input("Seleccione que ejercicio desea ejecutar(5-7): "))
if variable == 5:
    import ejercicio5
elif variable == 6:
    import ejercicio6
elif variable == 7:
    import ejercicio7
else:
    print("Introduzca valores entre 5 y 7.")
