    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next= before
            before = temp
            temp = after

my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.print_list()
print("after reversing")
my_linked_list.reverse()
my_linked_list.print_list()