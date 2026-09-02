class node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self,val):
        new_node = node(val)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def traversal(self):
        current = self.head
        while current is not None:
            print(current.val)
            current = current.next

    def create_loop(self, pos_start, pos_end):
        current = self.head
        start_loop_node = None
        end_loop_node = None
        count = 0

        while current:
            if count == pos_start:
                start_loop_node = current

            if count == pos_end:
                end_loop_node = current

            current = current.next
            count += 1

        if start_loop_node is None or end_loop_node is None:
            print("Invalid positions")
            return

        end_loop_node.next = start_loop_node
        print(f'loop have been succesfully create between {end_loop_node.val} and {start_loop_node.val}')
    
    def length_of_loop(self):
        d = {}
        current = self.head
        count = 0

        while current is not None:
            d[current] = count
            count += 1

            if current.next in d:
                return count - d[current.next]

            current = current.next

        return 0

SLL1 = Linkedlist()
n = int(input())
for i in range(n):
    SLL1.append(int(input()))
SLL1.create_loop(2, 8)

# Do NOT call traversal() after creating a loop.
# Once a loop is created, there is no node whose next is None.
# Therefore, current will never become None, and traversal()
# will run forever (infinite loop).

# SLL1.traversal()   # Don't call this
'''If still we wanted to travser the linked list with loop we can use this travser function.
def traversal(self):
    current = self.head
    visited = set()

    while current is not None:
        if current in visited:
            print(f"Loop detected at {current.val}")
            break

        visited.add(current)
        print(current.val)
        current = current.next
        '''
#SLL1.traversal()