"""Lab 02.02 - Student Groups"""
import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ArrayStack:
    def __init__(self):
        self.size = 0
        self.top = None

    def push(self, input_data):
        new_node = Node(input_data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("Underflow: Cannot pop data from an empty list")
            return None
        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node.data

    def is_empty(self):
        return self.size == 0

    def get_stack_top(self):
        if self.is_empty():
            print("Underflow: Cannot get stack top from an empty list")
            return None
        return self.top.data

    def get_size(self):
        return self.size

    def print_stack(self):
        current = self.top
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

class GroupNode:
    def __init__(self):
        self.head = None
        self.tail = None
        self.next = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def print_group(self):
        current = self.head
        while current:
            print(current.data, end=", " if current.next else "")
            current = current.next

class GroupList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, group):
        if self.head is None:
            self.head = group
            self.tail = group
        else:
            self.tail.next = group
            self.tail = group

    def print_groups(self):
        current = self.head
        index = 1
        while current:
            print(f"Group {index}:", end=" ")
            current.print_group()
            print()
            current = current.next
            index += 1

def main():
    many_group = int(input())
    all_student = int(input())
    Temp = ArrayStack()
    for _ in range(all_student):
        Temp.push(input())

    groups = GroupList()

    for _ in range(many_group):
        groups.append(GroupNode())

    current_group = groups.head
    for i in range(all_student):
        if current_group is None:
            current_group = groups.head
        current_group.append(Temp.pop())
        current_group = current_group.next

    groups.print_groups()
main()
