# filtra los numeros entre 0 y 100
def catch_number(message):
    while True:
        try:
             input_message = input(message).strip()
             number = float(input_message)
             if 0 <= number <= 100:
                return number
             else:
                print("Invalid value: enter number 0 to 100")    
        except ValueError:
            print("Invalid value: Enter a number")
        except KeyboardInterrupt:
            print("Input canceled")
            return 0
        
        
# Add a new student information
# Valido que solo se agregue texto sin espacios
# uso catch_number para validar que realice el filtro entre la informacion que necesito unicamente
def add_student():
    print("Add information of student: ")


student_grade = (input("Insert student grade ad group: ")).strip()

spanish_note = catch_number("Add spanish note: ")
english_note = catch_number("Add english note: ")
sociales_note = catch_number("Add sociales note: ")
ciencias_note = catch_number("Add ciencias note: ")

# guardo informacion en diccionario
new_student = {
    "Name": student_name,
    "Grade": student_grade,
    "Notes": {
        "spanish": spanish_note,
        "English": english_note,
        "Sociales": sociales_note,
        "Ciencias": ciencias_note,
    
      }

   }



def add(current, new_number):
    result = current + new_number
    print(f"The sum of:  {current} + {new_number} = {result}")
    return result


#mostrar estudiantes

def see_students(dicc_student):
    if not students:
        print("Dont have any student")
        return

for i, dicc_student in enumarte (student, 1):
    print(f"Student {i}")
    print(f"Name: {student['name']}")
    print(f"Grade: {student['grade']}")
    print(f" Notes:")

for materia, note in dicc_student['notes'].items():
    print(f"     - {materia.capitalize()}: {nota}")




def agregar_estudiante():
    # Código para agregar estudiante
    student_name = (input("Insert student name: ")).strip()
    pass

def ver_estudiantes(students):
    # Código para mostrar estudiantes
   def see_students(dicc_student):
    if not students:
        print("Dont have any student")
        return

for i, dicc_student in enumarte (student, 1):
    print(f"Student {i}")
    print(f"Name: {student['name']}")
    print(f"Grade: {student['grade']}")
    print(f" Notes:")

for materia, note in dicc_student['notes'].items():
    print(f"     - {materia.capitalize()}: {nota}")
    pass

def see_information(students):
    # Código para buscar un estudiante

    prome = (spanish_note, english_note, sociales_note, ciencias_note) / 4
    pass

def eliminar_estudiante(students):
    # Código para eliminar estudiante
    pass

def modificar_estudiante(students):
    # Código para modificar notas o datos
    pass

def calcular_promedios(students):
    # Código para calcular promedio general o por estudiante
    pass

def salir():
    print("👋 Saliendo del programa. ¡Hasta luego!")

def main():
    students = []

    while True:
        print("\ MENÚ PRINCIPAL:")
        print("1. Add student")
        print("2. See information")
        print("3. Top calification")
        print("4. Promedio")
        print("5. Import")
        print("6. Export")
        print("7. Exit")

        opcion = input("Select option (1-7): ").strip()

        if option == "1":
            estudiante = add_student()
            if estudiante:
                students.append(estudiante)
        elif option == "2":
            see_student(students)
        elif option == "3":
            search_student(students)
        elif option == "4":
            delete_student(students)
        elif option == "5":
            modify_student(students)
        elif option == "6":
            calcular_promedios(students)
        elif option == "7":
            salir()
            break
        else:
            print("Invalid value: Enter a number ( 1-7 )")

if __name__ == "__main__":
    main()