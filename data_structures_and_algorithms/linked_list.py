class Node:
    def __init__(self, value, node=None):
        self.value = value
        self.next_node = node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
        else:
            self.head = new_node

    def include(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            else:
                current = current.next_node
        return False

    def __str__(self):
        string = ""
        current = self.head
        while current is not None:
            string = string + f"{{{current.value}}}->"
            current = current.next_node
        string = string + "NULL"
        return string





if __name__ == '__main__':
     list = LinkedList()
     print(list)
     list.insert(5)
     list.insert(6)
     list.insert(7)
     list.insert(10)
     print(list)
     print(list.head.value)
     print(list.include(10))
     print(list.include(15))