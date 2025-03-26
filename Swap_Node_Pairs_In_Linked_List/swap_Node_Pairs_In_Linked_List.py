class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    prev_node = head
    curr_node = head.next
    head = curr_node
    while True:
        next_node = curr_node.next
        curr_node.next = prev_node
        if next_node is None or next_node.next is None:
            prev_node.next = next_node
            break
        prev_node.next = next_node.next
        prev_node = next_node
        curr_node = prev_node.next

    return head
