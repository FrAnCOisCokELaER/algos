#Single Linked list
#A doubly linked list has O(1) insertion and deletion at both ends, so it is a natural choice for queues.
#A regular singly linked list only has efficient insertion and deletion at one end. However, a small modification—keeping a pointer to the last node in addition to the first one—will enable it to implement an efficient queue.

class Node:
    def __init__(self, next=None, data = None):
        self.next=None

#basic FIFO queue with O(1) push and pop
class sll:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        newnode = Node()
        newnode.data = data
        if self.head is None:
            self.head = newnode
            self.tail = self.head
        else:
            if self.tail:
                tail = self.tail
                tail.next = newnode
                self.tail = newnode
        return self.tail

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

if __name__ == "__main__":
    asll = sll()
    asll.push(10)
    asll.push(15)
    asll.push(22)
    print(asll)
    asll.pop()
    print(asll)