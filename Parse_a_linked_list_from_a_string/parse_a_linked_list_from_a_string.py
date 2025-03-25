class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    values = s.split(' -> ')[:-1]
    if not values:
        return None
    head = Node(values[0], None)
    curr_node = head
    for i in values[1:]:
        next = Node(i, None)
        curr_node.next = next
        curr_node = next
    return head

linked_list_from_string("1 -> 2 -> 3 -> None")
