from node import Node

class Stack:
    def __init__(self, name=None):
        self.name = name
        self.limit = 1000
        self.size = 0
        self.head_node = None

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def has_space(self):
        return self.limit > self.size
    def is_empty(self):
        return self.size == 0
    
    def push(self, value):
        if self.has_space():
            new_node = Node(value)
            #making this new node as the nead node by first setting current head node as next of 
            new_node.set_next_node(self.head_node)
            self.head_node = new_node
            self.size += 1
        else:
            print("Stack is full")

    def pop(self):
        if not self.is_empty():
            node_to_remove =  self.head_node
            self.head_node = node_to_remove.get_next_node()
            return node_to_remove.get_value()
            self.size -= 1
        else:
            print("Stack is empty")

    def print_list(self):
        item_list = []
        current_node = self.head_node
        while current_node:
            item_list.append(current_node.get_value())
            current_node = current_node.get_next_node()
        item_list.reverse()
        return item_list
        print(f"{self.get_name()} Stacks {print_list}")

#Testing the Stack class        
# plates = Stack(5)
# plates.push("Plate1")
# plates.push("Plate2")
# plates.push("Plate3")
# plates.push("Plate4")
# plates.push("Plate5")

# print(plates.print_list())
# plates.push("plate6")

# print(plates.has_space())

            

