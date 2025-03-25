class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    if head is None:
        return Node(data)
    nd = Node(data)
    nd.next = head
    return nd


def build_one_two_three():
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head