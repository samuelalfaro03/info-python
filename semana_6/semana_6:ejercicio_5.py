# 1. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#    1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”



def sum_letters(text):
    uppercase = sum(1 for char in text if char.isupper())
    lowercase = sum(1 for char in text if char.islower())
    return uppercase, lowercase

input_text = input("write a sentence: ")

upper, lower = sum_letters(input_text)

print("Uppercase:", upper, "Lowercase", lower)