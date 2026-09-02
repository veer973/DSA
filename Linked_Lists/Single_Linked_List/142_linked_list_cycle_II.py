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
    def linked_list_cycle2(Self,head):
        current = self.head
        s = set()
        while current is not None:
            if current in s:
                return current
            s.add(current)
            current = current.next
        return None