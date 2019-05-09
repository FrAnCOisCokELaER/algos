#Single Linked list
#A doubly linked list has O(1) insertion and deletion at both ends, so it is a natural choice for queues.
#A regular singly linked list only has efficient insertion and deletion at one end. However, a small
# modification—keeping a pointer to the last node in addition to the first one—will enable it to implement an efficient queue.

class Node:
    def __init__(self, next=None, data = None):
        self.next = None
        self.data = None

#basic FIFO queue with O(1) push and pop
class fifo:
    def __init__(self):
        self.head = None
        self.last = None

    #add new node, at the end of fifo
    def push(self, data):
        newnode = Node()
        newnode.data = data
        if self.last:
            last = self.last
            last.next = newnode
        self.last = newnode

        if not self.head:
            self.head = newnode

    #LIFO
    def pop(self):
        if self.head:
            head = self.head
            self.head = self.head.next
            return head
        else:
            return None

    def __str__(self):
        def printloop(node):
            if node is not None:
                print(node.data)
                return printloop(node.next)
            else:
                return "end"
        return printloop(self.head)

class lifo:
    def __init__(self):
        self.head = None
    def push(self, data):
        newnode = Node(data)
        newnode.data=data
        if self.head:
            currhead = self.head
            newnode.next=currhead
        self.head = newnode
    def pop(self):
        currhead = self.head
        self.head = currhead.next
        return currhead

    def __str__(self):
        def printloop(node):
            if node:
                print(node.data)
                return printloop(node.next)
            else:
                return "End of the queue"
        return printloop(self.head)

if __name__ == "__main__":
    asll = fifo()
    asll.push(10)
    asll.push(15)
    asll.push(22)
    print(asll)
    asll.pop()
    print(asll)

    alifo = lifo()
    alifo.push(45)
    alifo.push(12)
    alifo.push(49)
    print(alifo)
    alifo.pop()
    print(alifo)