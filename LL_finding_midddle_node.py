class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght= 1

    def print_ll(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def append(self,value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node

    def middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print(slow.value)


myLL = LinkedList(1)
myLL.append(2)
myLL.append(3)
myLL.append(4)
myLL.append(5)
# myLL.append(6)
myLL.print_ll()
print("middle element/node is: ")
myLL.middle_node()