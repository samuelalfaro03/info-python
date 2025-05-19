#  notas estudiante

cantidad_notas = int(input("Ingrese la cantidad de notas: "))
notas_agregadas = []
n = 0

for n in range(1,cantidad_notas + 1):
    nota = int(input("Nota: "))
    n = n + nota
    notas_agregadas.append(nota)

mayor_igual_70 = 0
menor_70 = 0

for nota in notas_agregadas:
    if nota >= 70:
        mayor_igual_70 +=1

for nota in notas_agregadas:
    if nota < 70:
        menor_70 +=1

mayor_igual_70 = [nota for nota in notas_agregadas if nota > 70]

if mayor_igual_70:
    suma = sum(mayor_igual_70)
    cantidad_notas = len(mayor_igual_70)
    promedio = suma / cantidad_notas
else:
    promedio = 0


print("Notas Aprobadas:", mayor_igual_70)
print("Notas Reprobadas:", menor_70)
print("El promedio de las notas es: ", promedio)