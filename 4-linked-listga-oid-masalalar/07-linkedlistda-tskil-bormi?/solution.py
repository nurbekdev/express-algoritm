class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def hasCycle(head: Node) -> bool:
    fast = slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True

    return False
