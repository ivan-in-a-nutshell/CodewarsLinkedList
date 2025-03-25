class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    if node is None:
        return "None"
    data = []
    curr_node = node
    next = node.next
    while True:
        data.append(str(curr_node.data))
        if curr_node.next is None:
            # data.append(str(curr_node.data))
            break
        curr_node = next
        next = next.next
    data.append('None')
    return ' -> '.join(data)
