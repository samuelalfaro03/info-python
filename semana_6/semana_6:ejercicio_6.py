# 1. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#    1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#    2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

input_text = input("Write words separated by a hyphen: ")


list_sentences = input_text.split("-")
list_sentences.sort()
ordered_text = "-".join(list_sentences)

print(ordered_text)