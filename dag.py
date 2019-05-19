#Directed ayclic graph example filled with integer
class Node:
    def __init__(self, data):
        self.prev = list()
        self.next = list()
        self.data = data

class DAG:
    def __init__(self):
        self.nodes = list()

    #get a list of all path in a directed graph
    def allpaths(self):
        starters = list()
        for node in self.nodes:
            if not node.prev:
                starters.append(node)
        if not starters:
            print("no starting node has been found")
            return -1

        #analigous to anagramm generation
        def allpathsfromnode(startnode, path, acc):
            nexts = startnode.next
            if not nexts:
                acc.append(path + [startnode.data])
            else:
                for next in nexts:
                    allpathsfromnode(next, path+[startnode.data], acc)

        all = list()
        for starter in starters:
            anacc = list()
            allpathsfromnode(starter, list(), anacc)
            all.append(anacc)
        return all

if __name__ == "__main__":
    tree = DAG()
    newnode1 = Node(1)
    for n in range(0,3):
        newnode1.next.append(Node(n*3))
    for node in newnode1.next:
        for n in range(0, 4):
            node.next.append(Node(n*3 + 2))
    tree.nodes.append(newnode1)
    print(tree.allpaths())