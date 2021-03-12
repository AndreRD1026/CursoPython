#Ejercicio 1
print("Ejercicio #1")
contra = "andreramirez123"
password = input("Por favor introduce la contraseña: \n ")
if contra == password.lower():
    print("La contaseña ingresada coincide")
else:
    print("La contraseña ingresada no coincide\n")


#Ejercicio 2 
print("Ejercicio #2")
nombre = input("Por favor escriba su nombre:  \n")
genero = input("Por favor escriba su genero (H o M): \n")
if genero == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print(nombre + ", tu grupo correspondiente es el: " + grupo)




