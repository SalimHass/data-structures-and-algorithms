from audioop import lin2adpcm
from warnings import catch_warnings


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


def zip_lists(link_list_a, link_list_b):
    link_list = LinkedList()
    if link_list_a is not None and link_list_b is None:
        link_list.head = link_list_a.head
        return link_list

    if link_list_b is not None and link_list_a is None:
        link_list.head = link_list_b.head
        return link_list
    current_a = link_list_a.head
    current_b = link_list_b.head
    while current_a or current_b:
        if current_a:
            link_list.append(current_a.value)
            current_a = current_a.next_node
        if current_b:
            link_list.append(current_b.value)
            current_b = current_b.next_node

    return link_list


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
    lista = LinkedList()
    lista.append(1)
    lista.append(3)
    lista.append(6)
    lista.append(8)
    lista.append(11)
    print(lista)
    listb = LinkedList()
    listb.append(5)
    listb.append(9)
    listb.append(10)
    print(listb)
    print(zip_lists(lista, listb))
  

    
    
  

