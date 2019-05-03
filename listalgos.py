
#https://www.tutorialspoint.com/python/python_recursion.htm

#append is modifying the list in place, + create a new list
#complexity ois O(n log(n))
#logarithm time to divide and linear time to merge n elements
def msort(tosort):
    #divide
    halfindex = (int) (len(tosort)/2)
    if halfindex == 0:
        return tosort
    else:
        #merge
        def merge(left, right):
            if not left:
                return right
            if not right:
                return left
            if left[0]<=right[0]:
                 return [left[0]] + merge(left[1:], right)
            else:
                return [right[0]] + merge(left, right[1:])
        return (merge(msort(tosort[0:halfindex]), msort(tosort[halfindex:])))


#complexity ois O(n log(n))
#logarithm time to divide and linear time to compare n elements
def qsort(tosort):
    halfindex = (int)(len(tosort) / 2)
    if halfindex == 0:
        return tosort
    else:
        def mergelists(left, right, pivot):
            if not left:
                return [pivot]+right
            if not right:
                return left+[pivot]
            return left+[pivot]+right

        pivotval = tosort[halfindex]
        tosort.pop(halfindex)
        left = list(filter(lambda x: x <= pivotval, tosort))
        right = list(filter(lambda x: x > pivotval, tosort))

        return mergelists(qsort(left), qsort(right), pivotval)

#a unique algorithm in n! worst case complexity
def unique(tosort):
    if not tosort:
        return list()
    return [tosort[0]] + unique(list(filter(lambda x: x != tosort[0], tosort)))

#using a set is reducing complexity to O(n)
def uniquebest(tosort):
    if not tosort:
        return list()
    res = set()
    for elt in tosort:
        res.add(elt)
    return list(res)

#divide an conquer binary search on sorted list
def bsearch(tosearch, idx0, idxn, val):
    if idxn < idx0:
        return None
    else:
        halfindex = idx0 + ((idxn - idx0) // 2)
        if tosearch[halfindex] > val:
            return bsearch(tosearch, idx0, halfindex-1, val)
        elif tosearch[halfindex] < val:
            return bsearch(tosearch, halfindex+1, idxn, val)
        else:
            return halfindex


#double linked list
class Node_:
    def __init__(self, next= None, prev=None, data=None):
        self.data = data
        self.prev = prev
        self.next = next


class dll:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data=data)
        node.next=self.head
        node.prev=None

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

if __name__ == "__main__":
    # test = [12,56,89,1,23,45,22,12]
    # #print(msort(test))
    # print(qsort(test))
    # print(uniquebest(test))
    # root = Node(27)
    # root.insert(14)
    # root.insert(35)
    # root.insert(10)
    # root.insert(19)
    # root.insert(31)
    # root.insert(42)
    # root.PrintTree()
    # print(root.inordertraversal(root))
    # list = [8, 11, 24, 56, 88, 131]
    # print(bsearch(list, 0, 5, 24))
    # print(bsearch(list, 0, 5, 51))
    queens(4)