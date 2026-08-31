class Node:
    def __init__(self,data):
        self.data   =   data
        self.next   =   None

class LinkedList:
    def __init__(self):
        self.head   = None
    
    def insert_at_head(self,data):
        new_node        = Node(data)
        new_node.next   = self.head
        self.head       = new_node
    
    def reverse(self):
        prev    =   None
        current =   self.head

        while current:
            next_node       =   current.next
            current.next    =   prev
            prev            =   current
            current         =   next_node
        self.head   =   prev

    def printList(self):
        current =   self.head
        while current:
            print(current.data,end="->")
            current = current.next
        print("NULL")
    

ll = LinkedList()

for val in [30,20,10]:
    ll.insert_at_head(val)

ll.printList()
ll.reverse()
ll.printList()
