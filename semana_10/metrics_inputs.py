# metrics 


def show_all(student_list):
    print("\n ALL STUDENTS ")
    if not student_list:
        print("No students yet")
        return
    
    for student_number, student_data in enumerate(student_list, 1):
        print(f"\nStudent #{student_number}:")
        print(f"Name: {student_data['name']}")
        print(f"Grade: {student_data['grade']}")
        print("Grades:")
        
        grades = student_data['grades']
        print(f"- Spanish: {grades['spanish']}")
        print(f"- English: {grades['english']}")
        print(f"- Social Studies: {grades['social_studies']}")
        print(f"- Science: {grades['science']}")

def top3(student_list):
    print("\n TOP 3 STUDENTS ")
    if len(student_list) < 1:
        print("Not enough students")
        return
    
    # Calculate averages
    students_with_average = []
    for student_data in student_list:
        grades = student_data['grades']
        student_average = (grades['spanish'] + grades['english'] + 
                          grades['social_studies'] + grades['science']) / 4
        
        students_with_average.append({
            'name': student_data['name'],
            'grade': student_data['grade'],
            'average': student_average
        })
    
    # Sort and take the top 3
    top_three_sorted = sorted(students_with_average, key=lambda student: student['average'], reverse=True)[:3]
    
    # Display results
    for position, top_student_data in enumerate(top_three_sorted, 1):
        print(f"\nTop #{position}: {top_student_data['name']}")
        print(f"Grade: {top_student_data['grade']}")
        print(f"Average: {top_student_data['average']:.1f}")

def overall_average(student_list):
    if not student_list:
        print("No students available to calculate")
        return
    
    total_sum_averages = 0
    for student_data in student_list:
        grades = student_data['grades']
        individual_average = (grades['spanish'] + grades['english'] + 
                             grades['social_studies'] + grades['science']) / 4
        total_sum_averages += individual_average
    
    overall_course_average = total_sum_averages / len(student_list)
    print(f"\nCourse Average: {overall_course_average:.2f}")