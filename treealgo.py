#binary search tree definition
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    #insert a node in binary search tree
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

    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()

    #left, central, right
    def inordertraversal(self, node):
        res = []
        if node:
            res = self.inordertraversal(node.left)
            res = res + [node.data]
            res = res + self.inordertraversal(node.right)
        return res

    #central, left, right
    def preordertraversal(self, node):
        res = []
        if node:
            res = [node.data]
            res = res + self.preordertraversal(node.left)
            res = res + self.preordertraversal(node.right)
        return res

    #left, right, central
    def postordertraversal(self, node):
        res = []
        if node:
            res = self.postordertraversal(node.left)
            res = res + self.postordertraversal(node.right)
            res = res + [node.data]
        return res

#depth first binary : !! not efficient for binary trees
def findbyvalue(node, value):
    if node:
        if node.data is value:
            res = node
            return res
        else:
            foundleft = findbyvalue(node.left, value)
            if foundleft:
                return foundleft
            foundright = findbyvalue(node.right,value)
            if foundright:
                return foundright

import collections
#the two follwing
#breadth first
def findbyvaluebreadth(head, value):
    def findinlist(nodequeue, value):
        while nodequeue :
            curr = nodequeue.pop()
            if curr.data is value:
                return curr
            else:
                nodequeue.append(curr.left)
                nodequeue.append(curr.right)
        return
    q = collections.deque()
    q.append(head)
    node = findinlist(q, value)
    return node

def findbyvaluebinary(head,value):
    if head:
        if value > head.data:
            return findbyvaluebinary(head.right,value)
        elif value < head.data:
            return findbyvaluebinary(head.left, value)
        else:
            return head

if __name__ == "__main__":
    node = Node(10)
    node.insert(15)
    node.insert(42)
    node.insert(41)
    node.insert(5)
    node.insert(6)
    node.insert(2)
    node.print()
    print(node.inordertraversal(node))
    print(node.postordertraversal(node))
    print(node.preordertraversal(node))
    found = findbyvalue(node, 42)
    print(found.data)
    foundbreadth = findbyvaluebreadth(node, 42)
    print(foundbreadth.data)
    foundoptim = findbyvaluebinary(node,6)
    print(foundoptim.data)