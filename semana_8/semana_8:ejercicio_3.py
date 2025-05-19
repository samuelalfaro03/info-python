'''
1. Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
    1. Debe incluir:
        1. Nombre
        2. Género
        3. Desarrollador
        4. Clasificación ESRB

        '''

import csv

# Agrego los headers que voy utilizar
game_headers = ["Name", "Genre", "Developer", "Classification"]

# en caso de escribir alguna letra u otro valor que no sea numero genera el msj
# si escribe cntl c retorna 0 y cancelo el proceso
# en el return INT  
def catch_number(message):
    while True:
        try:
            input_info = input(message)
            return int(input_info)
        except ValueError:
            print("Invalid value: Please enter a number.")
        except KeyboardInterrupt:
            print("Input canceled.")
            return 0

def write_csv_file(file_path, headers):
    with open(file_path, 'w', encoding='utf-8', newline="") as file_csv:
        writer = csv.DictWriter(file_csv, fieldnames=headers)
        writer.writeheader()

# Creo el archivo y los headers - se imprime un vez creado el archivo
file_path = "game_headers.csv"
write_csv_file(file_path, game_headers)
print("The file was created with the specified headers.")

# Ingresan los datos con utf-8 para caracteres
# 'a' append, agrego info para header

with open(file_path, 'a', encoding='utf-8', newline="") as file_csv:
    writer = csv.writer(file_csv)

    # leo los valores agreagos con el try
    amount = catch_number("Enter the number of video games: ")

# el ciclo for para cada campo y un print antes para orden visual
# imprime finalizado el proceso
    for i in range(amount):
        print(f"\n--- Video Game {i+1} ---")
        name = input("Name: ")
        genre = input("Genre: ")
        developer = input("Developer: ")
        classification = input("Classification: ")
        writer.writerow([name, genre, developer, classification])

    print("\nThe data has been added successfully.")
