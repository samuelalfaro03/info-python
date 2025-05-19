'''
1. Cree una función que retorne la suma de todos los números de una lista.
    1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
    2. [4, 6, 2, 29] → 41
'''
def sum_list(numbers):
    return sum(numbers)


count = input("Enter numbers separated by spaces: ")

numbers_list = [int(num) for num in count.split()]

result = sum_list(numbers_list)
print("The sum of the numbers is:", result)