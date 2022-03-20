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
            new_node.next_node=current
            self.head = new_node
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

    def append(self, value):
        new_node = Node(value)
        if self.head:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
        else:
            self.head = new_node

    def insert_before(self, value, new_value):
        if self.head:
            new_node = Node(new_value)
            if self.head.value == value:
                new_node.next_node = self.head
                self.head = new_node
                return True
            else:
                current = self.head
                while current.next_node:
                    if current.next_node.value == value:
                        new_node.next_node = current.next_node
                        current.next_node = new_node
                        return True
                    current = current.next_node
        return False

    def insert_after(self, value, new_value):
        if self.head:
            new_node = Node(new_value)
            current = self.head
            while current.next_node:
                if current.value == value:
                    new_node.next_node = current.next_node
                    current.next_node = new_node
                    return True
                current = current.next_node
        return False


    def kth_from_end(self, k):
            list_length = 0
            current = self.head
            while current is not None:
                list_length += 1
                current = current.next_node
            if 0 <= k < list_length:
                k_node = self.head
                target_index = list_length - k
                index = 0
                while index < target_index-1:
                    index += 1
                    k_node = k_node.next_node
                return k_node
            else:
                raise IndexError


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
    list.insert_before(5, 3)
    list.insert_after(7, 9)
    list.insert_before(9, 8)
    print(list)
    print(list.kth_from_end(3).value)
