my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares_list = []
impares_list = []

for pares in my_list:
    if pares %2 == 0:
        pares_list.append(pares)
    else:
        impares_list.append(pares)

print('Número pares =>',pares_list)