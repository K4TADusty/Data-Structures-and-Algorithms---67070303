"""Lab 01.05 - Student Class (Class)"""
def main():
    """No Class"""
    students = []
    for _ in range(3):
        name = input()
        gender = input()
        age = input()
        student_id = input()
        gpa = float(input())
        students.append([name, gender, age, student_id, gpa])

    search_id = input()
    student = next((s for s in students if s[3] == search_id), None)
    
    if student:
        title = "Mr" if student[1] == "Male" else "Miss"
        print(f"{title} {student[0]} ({student[2]}) ID: {student[3]} GPA {student[4]:.2f}")
    else:
        print("Student not found")
main()
