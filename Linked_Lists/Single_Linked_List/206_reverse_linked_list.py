class node:
    def __init__(self,val):
        self.val = val
        self.next = None

class single_linked_list:
    def __init__(self):
        self.head = None

    def append(self,val):
        new_node = node(val)
        if self.head == None:
            self.head = new_node
            #print("Linked List Is Empty")
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traversal(self):
        if self.head is None:
            print("List is Empty")
        else:
            current = self.head
            while current is not None:
                print(current.val)
                current = current.next
    
    def reverse(self):
        temp = self.head
        stack = []
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next
        while temp is not None:
            e = stack.pop()
            temp.val = e
            temp = temp.next
        return self.head.val
    
    def optimal_reverse(self):
        temp = self.head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev.val
SLL1 = single_linked_list()
n = int(input())
arr =[]
for i in range(n):
    SLL1.append(int(input()))
resuult = SLL1.reverse()
print(resuult)