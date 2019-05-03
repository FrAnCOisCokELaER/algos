# Double linked list implementation
# implement traversal,
# #insertion , deletion
# pro and cons , complexity
#Linked list
#A doubly linked list has O(1) insertion and deletion at both ends, so it is a natural choice for queues.
#A regular singly linked list only has efficient insertion and deletion at one end. However, a small modification—keeping a pointer to the last node in addition to the first one—will enable it to implement an efficient queue.

# double linked list O(1) push and removal
class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.data = data
        self.prev = prev
        self.next = next


class dll:
    def __init__(self):
        self.head = None

    def traverse(self):
        def printnode(node):
            if node is None:
                print('End of the dequeue')
            else:
                print(node.data)
                printnode(node.next)
        printnode(self.head)

    def getnode(self, index):
        def loop(currindex, node):
            if node is None or index < 0:
                print('Wrong index : node is not found')
                raise Exception("'Wrong index : node is not found'")
            else:
                if index is currindex:
                    return node
                else:
                    return loop(currindex +1, node.next)
        node = loop(0, self.head)
        return node

    def push(self, data):
        node = Node(data=data)
        node.next = self.head
        node.prev = None

        if self.head is not None:
            self.head.prev = node
        self.head = node

    def insertafter(self, prev_node, new_data):
        # 1. check if the given prev_node is NULL
        if prev_node is None:
            print("This node doesn't exist in DLL")
            return

        # 2. allocate node  & 3. put in the data
        new_node = Node(data=new_data)

        # 4. Make next of new node as next of prev_node
        new_node.next = prev_node.next

        # 5. Make the next of prev_node as new_node
        prev_node.next = new_node

        # 6. Make prev_node as previous of new_node
        new_node.prev = prev_node

        # 7. Change previous of new_node's next node */
        if new_node.next is not None:
            new_node.next.prev = new_node

    def removenode(self, nodetodel):

        tmpprev = nodetodel.prev
        tmpnext = nodetodel.next
        if tmpprev :
            tmpprev.next = tmpnext
        else:
            self.head = tmpnext
        tmpnext.prev = tmpprev
        print('Node is deleted from the linked list')
        return 0


if __name__ == "__main__":
    adll = dll()
    adll.push(data=12)
    adll.push(data=45)
    adll.push(data=76)
    adll.traverse()
    #anode = adll.getnode(2)
    # adll.insertafter(anode, 101)
    # adll.traverse()
    # adll.getnode(0)

    adll.removenode(adll.getnode(1))
    adll.traverse()
