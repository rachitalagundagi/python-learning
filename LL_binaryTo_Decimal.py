class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1

    def print_ll(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.lenght += 1

    def binary_to_integer(self):
        num = 0
        temp = self.head
        while temp is not None:
            num = num *2 + temp.value
            temp= temp.next
        print(num)


myLL = LinkedList(1)
myLL.append(1)
myLL.append(0)
myLL.print_ll()
print("converting binary to integer: ")
myLL.binary_to_integer()