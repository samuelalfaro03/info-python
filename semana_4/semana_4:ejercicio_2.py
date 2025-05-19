#Filtre por generos 

nombre = str(input("Ingresar su nombre: "))
apellido = str(input ("Ingresar su apellido: "))
edad = int(input ("Ingresar su edad: "))


if edad <= 2:
    print ("Bebé")

elif 3 <= edad <= 12:
    print ("Niño")
elif 13 <= edad <= 17:
    print ("Preadolescente")
elif 18 <= edad <= 21:
    print ("Adolescente")
elif 22 <= edad <= 35:
    print ("Adulto Joven")
elif 36 <= edad <= 64:
    print ("Adulto")
else:
    print ("Adulto Mayor")
