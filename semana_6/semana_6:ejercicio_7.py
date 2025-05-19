# 2. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#    1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]

import math


input_numbers = input("Enter numbers separated by '-': ")

try:
    numbers = [int(num) for num in input_numbers.split("-")]

    def n_prime(num_check):
        if num_check < 2 or (num_check > 2 and num_check % 2 == 0):
            return False  
        return all(num_check % i != 0 for i in range(3, int(math.sqrt(num_check)) + 1, 2))

   
    def filter_primes(numbers):
        return [num for num in numbers if n_prime(num)]

    prime_numbers = filter_primes(numbers)
    print("These numbers are not prime:", numbers)
    print("Prime numbers:", prime_numbers)

except ValueError:
    print("Invalid input. Please enter only numbers separated by '-'")