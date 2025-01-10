"""Lab 04.04 – Binary Search Tree (Min, Max)"""
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

    def is_empty(self):
        return self.root is None

    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, node):
        if node:
            print("->", node.data, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print("->", node.data, end=" ")
            self._inorder(node.right)

    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print("->", node.data, end=" ")

    def traverse(self):
        if self.is_empty():
            print("This is an empty binary search tree.")
        else:
            print("Preorder:", end=" ")
            self.preorder()
            print("Inorder:", end=" ")
            self.inorder()
            print("Postorder:", end=" ")
            self.postorder()

    def find_min(self):
        if self.is_empty():
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.data

    def find_max(self):
        if self.is_empty():
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.data

def main():
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()
    print("Max:", my_bst.find_max())
    print("Min:", my_bst.find_min())

main()
