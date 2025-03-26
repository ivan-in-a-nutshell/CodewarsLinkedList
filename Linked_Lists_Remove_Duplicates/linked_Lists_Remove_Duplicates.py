class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None or head.next is None:
        return head
    curr_node = head
    while curr_node.next is not None:
        if curr_node.data == curr_node.next.data:
            curr_node.next = curr_node.next.next
            continue
        curr_node = curr_node.next
    return head

a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c

remove_duplicates(a)
