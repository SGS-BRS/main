class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_node(data):
    return Node(data)

def insert_at_beginning(head, data):
    new_node = create_node(data)
    new_node.next = head
    return new_node

def insert_at_end(head, data):
    new_node = create_node(data)
    if head is None:
        return new_node
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = new_node
    return head

def insert_after_node(prev_node, data):
    if prev_node is None:
        print("The previous node cannot be None")
        return
    new_node = create_node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

def delete_node(head, key):
    temp = head
    if temp is not None:
        if temp.data == key:
            head = temp.next
            temp = None
            return head
    while temp is not None:
        if temp.data == key:
            break
        prev = temp
        temp = temp.next
    if temp == None:
        return head
    prev.next = temp.next
    temp = None
    return head
