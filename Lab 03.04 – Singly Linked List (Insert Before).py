"""Lab 03.04 – Singly Linked List (Insert Before)"""
class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = SinglyLinkedListNode(data)
        new_node.next = self.head
        self.head = new_node

    def insert_last(self, data):
        new_node = SinglyLinkedListNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_before(self, target, data):
        if not self.head:
            print("Cannot insert, " + target + " does not exist.")
            return
        if self.head.data == target:
            self.insert_front(data)
            return
        prev = None
        current = self.head
        while current and current.data != target:
            prev = current
            current = current.next
        if current:
            new_node = SinglyLinkedListNode(data)
            new_node.next = current
            prev.next = new_node
        else:
            print("Cannot insert, " + target + " does not exist.")

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        prev = None
        current = self.head
        while current and current.data != data:
            prev = current
            current = current.next
        if current:
            prev.next = current.next

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
    n = int(input())
    for _ in range(n):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            target, new_data = data.split(", ")
            mylist.insert_before(target, new_data)
        elif condition == "D":
            mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()
main()
