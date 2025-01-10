"""Lab 04.06 – Binary Search Tree (Delete All Cases)"""
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

    def delete(self, data):
        self.root, deleted_node = self._delete(self.root, data)
        if deleted_node is None:
            print("Delete Error, " + str(data) + " is not found in Binary Search Tree.")
        return deleted_node

    def _delete(self, node, data):
        if node is None:
            return node, None
        if data < node.data:
            node.left, deleted_node = self._delete(node.left, data)
        elif data > node.data:
            node.right, deleted_node = self._delete(node.right, data)
        else:
            deleted_node = node
            if node.left is None:
                return node.right, deleted_node
            elif node.right is None:
                return node.left, deleted_node
            else:
                max_left = self._find_max(node.left)
                node.data = max_left.data
                node.left, _ = self._delete(node.left, max_left.data)
        return node, deleted_node

    def _find_max(self, node):
        current = node
        while current.right:
            current = current.right
        return current

def main():
    my_bst = BST()
    while True:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()

main()
