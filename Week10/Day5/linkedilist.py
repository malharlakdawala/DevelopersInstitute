class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, node=None):
        self.head = node

n1 = Node("Mon")
n2 = Node("Tue")
n1.next = n2
n2.next = Node("Wed")

node = n1
#print(node.data)
a=LinkedList(Node("Sun", Node("Mon", Node("Tue", Node("Wed", Node("Thurs"))))))
node = a.head
print(node.data)