"""Lab 04.01 - Create BSTNode"""
class BSTNode:
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None
def main():
    data = int(input())
    node = BSTNode(data)
    print(node.data)
    print(node.left)
    print(node.right)
main()
