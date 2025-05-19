''' 
Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.
'''
import json

#Ubicacion arhivo JSON 
def get_pokemon_file():
    return '/Users/sonidomg/Documents/SAMUEL/progra/python2025/clase_8/pokemon_list.json'  # cambiado a .json

#Leer formato JSON del archivo
def load_pokemons(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("File not found. Staring with new list.")
        return []

#Guardar los cambios al archivo
def save_pokemons(filepath, pokemons):
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(pokemons, file, indent=4)

#Agregar nuevo Pokémon
def add_new_pokemon(pokemons):
    name = input("Enter the Pokémon's name: ").strip()

    # a "Debe leer el archivo para importar los Pokémones existentes"
    already_exists = any(p["name"]["english"].lower() == name.lower() for p in pokemons)

    # valida si el pokemon ya existe, si ya existe realiza el print con el msj sino pasa para agregar uno
    if already_exists:
        print(f"The Pokémon '{name}' already exists in the list. It won't be added.")
    else:
        types = input("Enter the Pokémon type, separated by commas if more than one: ").split(',')

        print("Enter the base stats of the Pokémon:")
        hp = int(input("HP: "))
        attack = int(input("Attack: "))
        defense = int(input("Defense: "))
        sp_attack = int(input("Sp. Attack: "))
        sp_defense = int(input("Sp. Defense: "))
        speed = int(input("Speed: "))

        # b "Luego debe pedir la información del Pokémon a agregar."
        new_pokemon = {
            "name": {"english": name},
            "type": [t.strip() for t in types],
            "base": {
                "HP": hp,
                "Attack": attack,
                "Defense": defense,
                "Sp. Attack": sp_attack,
                "Sp. Defense": sp_defense,
                "Speed": speed
            }
        }

        # Agrega un nuevo pokemon a la lista
        pokemons.append(new_pokemon)

        # Ordena por nombre alfabéticamente (opcional pero útil)
        pokemons.sort(key=lambda p: p["name"]["english"].lower())

        print(f"Pokémon '{name}' added and list saved in alphabetical order!")

# Función principal que organiza todo
def main():
    pokemon_file = get_pokemon_file()
    pokemons = load_pokemons(pokemon_file)
    add_new_pokemon(pokemons)
    # "Finalmente debe guardar el nuevo Pokémon en el archivo."
    save_pokemons(pokemon_file, pokemons)

# Ejecutar programa
main()
