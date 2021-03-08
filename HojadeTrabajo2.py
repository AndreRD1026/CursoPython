#Ejercicio1
print("Triangulo rectangulo")
nume = int(input("Por favor ingrese un numero entero positivo \n"))
for i in range(nume):
    for j in range(i+1):
        print("*", end="")
    print("")


#Ejercicio 2
print("Numeros separados por ','")
numero = int(input("Por favor ingrese un número entero positivo: \n"))
for i in range(numero, -1, -1):
    print(i, end=", ")


#Ejercicio 3
print("\nNumero primo ")
num = input("Por favor ingrese un numero: \n")
numero = int(num)
contador = 0
verificar= False
for i in range(1,numero+1):
    if (numero% i)==0:
       contador = contador + 1
    if contador >= 3:
        verificar=True
        break
if contador==2 or verificar==False:
    print ("El numero ingresado es primo")
else: print ("El numero ingresado no es primo")