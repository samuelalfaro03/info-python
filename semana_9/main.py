from info_inputs import add_student
from metrics_inputs import show_all, top3  # Cambiado a tu nombre de módulo

def main():
    students = []  # Almacena todos los estudiantes
    
    while True:
        print("\n=== SISTEMA ACADÉMICO ===")
        print("1. Agregar estudiante")
        print("2. Ver todos los estudiantes")
        print("3. Ver top 3 estudiantes")
        print("4. Salir")
        
        opcion = input("Seleccione opción (1-4): ").strip()
        
        if opcion == "1":
            new_student = add_student()
            if new_student:
                students.append(new_student)
                print("¡Estudiante agregado!")
        
        elif opcion == "2":
            show_all(students)
        
        elif opcion == "3":
            top3(students)
        
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Intente nuevamente.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()