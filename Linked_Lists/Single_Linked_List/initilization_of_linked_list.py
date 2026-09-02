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
            print("Linked List Is Empty")
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traversal(self):
        if self.head is None:
            print("Single Linked List Is Empty")
        else:
            current = self.head
            while current is not None:
                print(current.val)
                current = current.next

    def insert_at_any_position(self , postion , val):
        count = 0
        prev_node = None
        new_node = node(val)
        if postion == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while count<postion and current is not None:
                prev_node = current
                current = current.next
                count +=1
            prev_node.next = new_node
            new_node.next = current
    
    def delete(self,val):
        temp = self.head
        if temp.next is not None:
            if temp.val == val:
                self.head = self.head.next
                temp.next = None
                del temp
                return 
            else:
                found = False
                prev_node = None
                while temp is not None:
                    if temp.val == val:
                        found = True
                        break
                    prev_node = temp
                    temp = temp.next
                if found:
                    prev_node.next = temp.next
                    temp.next = None
                    del temp
                    return 
                else:
                    print("Node Not Found")

SLL1 = single_linked_list()
SLL1.append(10)
SLL1.append(20)
SLL1.append(30)
SLL1.append(40)
SLL1.insert_at_any_position(2,25)
SLL1.delete(20)
SLL1.append(1)

#SLL1.traversal()

