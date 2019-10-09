def create_student():
    name = input("Enter the student name: ")
    student_data = {"name" : name, "marks": []}
    return student_data

def add_marks(student, mark):
    student["marks"].append(mark)

def calculate_average_mark(student):
    if len(student["marks"]) > 0:
        return sum(student["marks"]) / len(student["marks"])
    else:
        return 0

student_data = create_student()
add_marks(student_data,8)
add_marks(student_data,4)
add_marks(student_data,6)

print(calculate_average_mark(student_data))