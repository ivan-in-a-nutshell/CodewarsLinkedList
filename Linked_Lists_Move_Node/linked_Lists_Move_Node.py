class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest


def move_node(source, dest):
    if not source:
        raise TypeError('Source cannot be None')
    temp = source.next
    source.next = dest

    return Context(temp, source)
