# Ejercicio #3 número secreto

import random

numero_secreto = random.randint(1,10)

adivina = False

while True:
    intento = input("Ingrese un número entre 1 y 10: ")
    if intento == numero_secreto:
        print("Excelente! número acertado")
        
    else:
        print("Incorrecto! Ingrese un número de nuevo")