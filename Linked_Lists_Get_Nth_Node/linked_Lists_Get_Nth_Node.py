class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if not isinstance(node, Node):
        raise TypeError('Expected a Node')
    if index < 0:
        raise IndexError("Negative index")
    i = 0
    while True:
        if i == index:
            return node
        if node.next is None:
            raise IndexError("Index out of range")
        node = node.next
        i += 1
