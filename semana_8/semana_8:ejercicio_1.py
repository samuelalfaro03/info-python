# Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

file_1 = '/Users/sonidomg/Documents/SAMUEL/progra/python2025/clase_8/music_2025.txt'
file_edit = '/Users/sonidomg/Documents/SAMUEL/progra/python2025/clase_8/music_2025_new.txt'

#Leo el archivo con la información
with open(file_1, 'r', encoding='utf-8') as file:
    content = file.readlines()

#Ordeno las lineas
orden_content = sorted([line.strip() for line in content if line.strip() != ''])

#Escribo la nueva informacion ya ordenada alfabeticamente
with open(file_edit, 'w', encoding='utf-8') as new_file:
    for line in orden_content:
        new_file.write(line + '\n')

print('Archivo ordenado creado en:', file_edit)