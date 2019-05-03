#binary search tree definition
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data <= self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data)
        if self.right:
            self.right.printtree()


    def inordertraversal(self, node):
        res = []
        if node:
            res = self.inordertraversal(node.left)
            res = res + [node.data]
            res = res + self.inordertraversal(node.right)
        return res


if __name__ == "__main__":
