#binary search tree definition
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

#insert a node in binary search tree
def insert(head, data):
    if head.data:
        if data < head.data:
            if head.left is None:
                head.left = Node(data)
            else:
                insert(head.left, data)
        elif data > head.data:
            if head.right is None:
                head.right = Node(data)
            else:
                insert(head.right, data)
    else:
        head.data = data

#traversal algorithm for binary graphs
#left, central, right
def inordertraversal(node):
    res = []
    if node:
        res = inordertraversal(node.left)
        res = res + [node.data]
        res = res + inordertraversal(node.right)
    return res

#central, left, right
def preordertraversal(node):
    res = []
    if node:
        res = [node.data]
        res = res + preordertraversal(node.left)
        res = res + preordertraversal(node.right)
    return res

#left, right, central
def postordertraversal(node):
    res = []
    if node:
        res = postordertraversal(node.left)
        res = res + postordertraversal(node.right)
        res = res + [node.data]
    return res


#print in depth
def printtree(node):
    if node.left:
        printtree(node.left)
    print(node.data)
    if node.right:
        printtree(node.right)


def deletenode(head, node):
    print(node.data)
    if node.left and node.right:
    # find max in rigth subtree
        maxnode = findmax(node)
        print(maxnode)
        #replace value
        parent = findparent(node, maxnode)
        node.data = maxnode.data
        parent.right = None
    elif node.left:
        node.data = node.left.data
        node.left = None
    elif node.right:
        node.data = node.right.data
        node.right = None
    else: #no child just remove
        parent = findparent(head, node)
        if parent.left.data is node.data:
            parent.left = None
        else:
            parent.right = None

def findparent(head, node):
    if node.data > head.data:
        if head.right is node:
            return head
        else:
            return findparent(head.right, node)
    elif node.data < head.data:
        if head.left is node:
            return head
        else:
            return findparent(head.left,node)
    else:
        return

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

def findmax(node):
    if node.right:
        return findmax(node.right)
    else:
        return node

import collections
#the two following
#breadth first
def findbyvaluebreadth(head, value):
    def findinlist(nodequeue, value):
        while nodequeue:
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
    insert(node, 15)
    insert(node, 12)
    insert(node, 42)
    insert(node, 43)
    insert(node, 5)
    insert(node, 6)
    insert(node, 2)
    printtree(node)

    print(inordertraversal(node))
    print(preordertraversal(node))
    print(postordertraversal(node))

    toto = findbyvaluebinary(node,789)
    print('test ok ')