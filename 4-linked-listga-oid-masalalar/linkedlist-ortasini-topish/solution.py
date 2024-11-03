class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def middleNode(head: Node) -> Node:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow
