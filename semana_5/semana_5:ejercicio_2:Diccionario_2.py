Keys = ['Marca', 'Modelo', 'Transmision', 'Año']
Values = ['Toyota', 'Camry', 'Automatico', '2020']


dictionary = {}

for i in range(len(Keys)):
    dictionary[Keys[i]] = Values[i]

print(dictionary)