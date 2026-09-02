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

    def linked_list_cycle(Self,head):
        current = self.head
        s = set()
        while current is not None:
            if current.next in s:
                print("True")
            s.add(current)
            current = current.next
        print("False")
    def linked_list_cycle_optimal(Self,head):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print("True")
            else:
                print("False")
        print("false")