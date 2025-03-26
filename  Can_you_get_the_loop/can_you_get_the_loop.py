def loop_size(node):
    slow = fast = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            current = slow
            count = 0
            while True:
                current = current.next
                count += 1
                if current == slow:
                    break
            return count
