class Node:
    def __init__(self, value = None, next_node =None):
        self.value = value
        self.next_node = next_node
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        return self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_to_tail(self, value):
        new_node = Node(value, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            set.tail = new_node
    def remove_head(self):
        if not self.head:
            return None
        if not self.head.get_next():
            head =self.head
            self.head = None
            self.tail = None

            return head.get_value()

value = self.head.get_value()
self.head = self.head.get_next()
return value