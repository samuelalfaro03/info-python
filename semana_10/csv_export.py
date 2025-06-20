# csv_export
import csv
import os

#6
#Export students to CSV
def export_simple_csv(students, filename="students.csv"):
    if not students:
        print("There are no students to export")
        return False
    
    try:
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            
            # Escribir encabezados
            writer.writerow(["Name", "Grade", "Spanish", "English", "Social_Studies", "Science"])
            
            # Escribir datos de cada estudiante
            for student in students:
                writer.writerow([
                    student["name"],
                    student["grade"],
                    student["grades"]["spanish"],
                    student["grades"]["english"],
                    student["grades"]["social_studies"],
                    student["grades"]["science"]
                ])
        
        print(f"Data exported to {filename}")
        return True
    
    except Exception as error:
        print(f"Export error {error}")
        return False

#6 Import students from CSV
def import_from_csv(filename="students.csv"):
    if not os.path.exists(filename):
        print(f"The file {filename} does not exist")
        return []
    
    try:
        students = []
        
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la primera línea (encabezados)
            
            for row in reader:
                if len(row) == 6:  # Verificar que tenga 6 columnas
                    student = {
                        "name": row[0],
                        "grade": row[1],
                        "grades": {
                            "spanish": float(row[2]),
                            "english": float(row[3]),
                            "social_studies": float(row[4]),
                            "science": float(row[5])
                        }
                    }
                    students.append(student)
        
        print(f"it was imported {len(students)} students")
        return students
    
    except Exception as error:
        print(f"Error importing: {error}")
        return []