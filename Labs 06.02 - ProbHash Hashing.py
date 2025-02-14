"""Labs 06.02 - ProbHash Hashing"""
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

class ProbHash:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size

    def hash(self, key):
        return key % self.size

    def rehash(self, hkey):
        return (hkey + 1) % self.size

    def insert_data(self, student):
        key = student.std_id
        index = self.hash(key)
        original_index = index
        while self.hash_table[index] is not None:
            if self.hash_table[index].std_id == key:
                print(f"Insert {key} at index {index}")
                return
            index = self.rehash(index)
            if index == original_index:
                print(f"The list is full. {key} could not be inserted.")
                return
        self.hash_table[index] = student
        print(f"Insert {key} at index {index}")

    def search_data(self, std_id):
        index = self.hash(std_id)
        original_index = index
        while self.hash_table[index] is not None:
            if self.hash_table[index].std_id == std_id:
                print(f"Found {std_id} at index {index}")
                return self.hash_table[index]
            index = self.rehash(index)
            if index == original_index:
                break
        print(f"{std_id} does not exist.")
        return None

def main():
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()
