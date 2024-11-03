class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def reverse(head: Node) -> Node:
    prev = None
    curr = head

    while curr:
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_

    return prev