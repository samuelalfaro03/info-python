# Valor de numero mas alto

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

if numero1 > numero2 > numero3:
    print("El número mayor es: ", numero1)

elif numero2 > numero3 > numero1:
    print("El numero mayor es: ", numero2)

elif numero3 > numero2 > numero1:
    print("El numero mayor es: ", numero3)