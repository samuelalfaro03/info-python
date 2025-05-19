'''
1. Experimente con el concepto de scope:
    1. Intente accesar a una variable definida dentro de una función desde afuera.
    2.  Intente accesar a una variable global desde una función y cambiar su valor.
'''

def turn():
    message = "login on turn A"
    print(message)

turn()
print(message)


banner = "Entrada parqueo"

def final_banner():
    global banner
    banner = "Salida parqueo"

print(banner)
final_banner()
print(banner)