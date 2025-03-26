class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    if head is None:
        return Node(data)
    if head.data >= data:
        data_node = Node(data)
        data_node.next = head
        return data_node
    curr_node = head
    while True:
        if curr_node.next is None:
            curr_node.next = Node(data)
            return head
        if curr_node.next.data > data:
            next_node = curr_node.next
            data_node = Node(data)
            data_node.next = next_node
            curr_node.next = data_node
            return head
        curr_node = curr_node.next
