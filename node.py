class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    def get_value(self):
        return self.value
    def get_next_node(self):
        return self.next_node
    def set_next_node(self, new_node):
        self.next_node = new_node

#Testing the Node class
# a = Node("apple")
# b = Node("oranges", a)
# c = Node("Guava", b)

# b.set_next_node(a)
# c.set_next_node(b)

