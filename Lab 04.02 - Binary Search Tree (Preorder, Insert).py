"""Lab 04.02 - Binary Search Tree (Preorder, Insert)"""
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BSTNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = BSTNode(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = BSTNode(data)
            else:
                self._insert(node.right, data)

    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, node):
        if node:
            print("->", node.data, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)

def main():
    my_bst = BST()
    n = int(input())
    for _ in range(n):
        my_bst.insert(int(input()))
    
    print("Preorder:", end=" ")
    my_bst.preorder()
main()
