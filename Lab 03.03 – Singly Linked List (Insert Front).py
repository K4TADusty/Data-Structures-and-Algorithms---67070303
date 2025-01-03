"""Lab 03.03 – Singly Linked List (Insert Front)"""
class SinglyLinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_last(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def traverse(self):
        if not self.head:
            print("This is an empty list.")
            return
        current = self.head
        while current:
            print(current.data, end=' -> ' if current.next else '')
            current = current.next
        print()

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        command, data = input().split(": ")
        if command == "F":
            mylist.insert_front(data)
        elif command == "L":
            mylist.insert_last(data)
    mylist.traverse()
main()
