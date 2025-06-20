
#info_inputs
#Numbers between 0 and 100
def catch_number(message):
    while True:
        try:
            num = float(input(message).strip())
            if 0 <= num <= 100:
                return num
            print("Invalid! Enter a number between 0-100")
        except ValueError:
            print("Invalid! Enter a valid number")
        except KeyboardInterrupt:
            print("\nInput canceled")
            return None
# 1 Add student
#Collect information from a student

# grade = Seccion or grupo
# grades = notas
def add_student():
    print("\n Add New Student ")
    
    while True:
        name = input("Student name: ").strip()
        if name.replace(" ", "").isalpha() and 2 <= len(name) <= 30:
            break
        print("Error! Name must contain only letters (min 2 chars)")
    
    while True:
        grade = input("Group: ").strip()
        if grade.isalnum() and len(grade) >= 2:
            break
        print("Error! Only use format like '11A'")
    
    grades = {
        'spanish': catch_number("Spanish grade: "),
        'english': catch_number("English grade: "),
        'social_studies': catch_number("Social Studies grade: "),
        'science': catch_number("Science grade grade: ")
    }
    
    #Note canceled return None
    if None in grades.values():
        return None
    
    return {
        'name': name.title(),
        'grade': grade.upper(),
        'grades': grades
    }