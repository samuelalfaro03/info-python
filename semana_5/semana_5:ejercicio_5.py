lista = []
for i in range(10):
    numeros_input = float(input(f"Ingrese un número {i+1}: "))
    lista.append(numeros_input)
def mayor(lista):
    return max(lista)
mayor_numero = mayor(lista)
print(f"El número mayor es: {mayor_numero}")