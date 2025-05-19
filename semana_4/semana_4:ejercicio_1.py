# Suma de datos

# string + string
dia = str("jueves 4 abril" )
fecha = str(" del año 2024")

data = dia + fecha

print(f"La fecha exacta es {data}")


# string + int 
dia_acumulado =str("1")
vacaciones =int("9")

resultado = int(dia_acumulado) + vacaciones

print(f'La cantidad de vacaciones es {resultado}')


# int + string
tiempo = int("2")
nombre = str("Tiempos")

nota = str(tiempo) + ' ' + nombre 

print(f'El valor de la figura musical blanca es: {nota}')


# list + list

valor1 = [2,4,6,8]
valor2 = [3,6,9,13]

respuesta = valor1 + valor2

print (f"El resultado de la suma de los valores es {respuesta}")


# string + list

vuelo = ["El", "vuelo", "del", "día", "martes", "será", "con"]
aerolinea = str("spirit")

viaje = vuelo + ' ' + aerolinea

print (viaje)

# float + int

sub_total = float(18.500)
cupon_descuento = int(1150)

total = sub_total - cupon_descuento
print(total)

# bool + bool


examen1 = True
examen2 = False

resultado = examen1 + examen2

print(f"Examen completado:", resultado)
