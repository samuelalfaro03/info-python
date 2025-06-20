#main
from info_inputs import add_student # informacion de agregar
from metrics_inputs import show_all, top3, overall_average # ver estudiantes, filtre top 3, promedio
from csv_export import export_simple_csv, import_from_csv  # exportar e importar cvs

def main():
    students = []
    
    while True:
        print("\n INFORMATION SYSTEM ")
        print("1 - Add student")
        print("2 - View all students")
        print("3 - View top 3 students")
        print("4 - Average grade of all students")
        print("5 - Export to CSV")
        print("6 - Import from CSV")
        print("7 - Exit")
        
        opcion = input("Select option (1-7): ").strip()
        
        if opcion == "1":
            new_student = add_student()
            if new_student:
                students.append(new_student)
                print("Student added successfully")
        
        elif opcion == "2":
            show_all(students)
        
        elif opcion == "3":
            top3(students)

        elif opcion == "4":
            overall_average(students)

        elif opcion == "5":
            export_simple_csv(students)
        
        elif opcion == "6":
            imported = import_from_csv()
            if imported:  # Si se importó correctamente
                students = imported  # Reemplazamos la lista actual
        
        elif opcion == "7":
            print("Query finished")
            break
        
        else:
            print("Invalid option. Select one of the options..")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()