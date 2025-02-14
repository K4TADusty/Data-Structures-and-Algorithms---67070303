"""Lab 06.03 - Binary Search"""
import json

class Student:
    def __init__(self, std_id, name, gpa):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    def print_details(self):
        print(f"ID: {self.std_id}")
        print(f"Name: {self.name}")
        print(f"GPA: {self.gpa:.2f}")

def binary_search(data, name):
    low = 0
    high = len(data) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if data[mid].name == name:
            print(f"Found {name} at index {mid}")
            data[mid].print_details()
            print(f"Comparisons times: {comparisons}")
            return mid
        elif data[mid].name < name:
            low = mid + 1
        else:
            high = mid - 1

    print(f"{name} does not exists.")
    print(f"Comparisons times: {comparisons}")
    return -1

def main():
    json_data = input()
    target_name = input()

    student_list = json.loads(json_data)
    students = [Student(std["id"], std["name"], std["gpa"]) for std in student_list]

    binary_search(students, target_name)
main()
