"""Lab 03.02 – Singly Linked List (Traversal and Insert Last)"""
class SinglyLinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def insert_last(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

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
        mylist.insert_last(input())
    mylist.traverse()

main()
