"""Lab 01.05 - Student Class (Class)"""
class Student:
    def __init__(self, name, gender, age, student_id, gpa):
        self.name = name
        self.gender = gender
        self.age = age
        self.student_id = student_id
        self.gpa = gpa

    def __str__(self):
        title = "Mr" if self.gender == "Male" else "Miss"
        return f"{title} {self.name} ({self.age}) ID: {self.student_id} GPA {self.gpa:.2f}"

def main():
    students = []
    for _ in range(3):
        name = input()
        gender = input()
        age = input()
        student_id = input()
        gpa = float(input())
        students.append(Student(name, gender, age, student_id, gpa))

    search_id = input()
    student = next((s for s in students if s.student_id == search_id), None)
    
    if student:
        print(student)
    else:
        print("Student not found")
main()
