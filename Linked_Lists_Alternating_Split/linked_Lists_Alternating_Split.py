class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise Exception("Not enough data")
    first = head
    curr_first = first
    second = head.next
    curr_second = second
    i = 0
    curr_node = head.next.next
    while curr_node is not None:
        if i % 2 == 0:
            curr_first.next = curr_node
            curr_first = curr_first.next
        else:
            curr_second.next = curr_node
            curr_second = curr_second.next
        i += 1
        curr_node = curr_node.next
    curr_first.next = None
    curr_second.next = None
    return Context(first, second)
