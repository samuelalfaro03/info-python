first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']

combined_list = []

for i in range(0, len(first_list)):
    combined_list = first_list[i] + ' ' + second_list[i]
    print(combined_list)
