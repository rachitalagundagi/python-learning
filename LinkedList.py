# creating a node
class Node:
    def __init__(self,value):
        self.value = value
        self.next= None

#creating LL
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1

# method to print ll
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# method to append node at end
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght += 1

myLL = LinkedList(1)
myLL.print_list()

myLL.append(2)
myLL.print_list()