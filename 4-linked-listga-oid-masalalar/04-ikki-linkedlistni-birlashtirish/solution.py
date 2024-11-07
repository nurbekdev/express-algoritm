class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def mergeTwoLists(head1: Node, head2: Node) -> Node:
    curr1, curr2 = head1, head2
    head = curr = Node(0)

    while curr1 and curr2:
        if curr1.val < curr2.val:
            curr.next = curr1
            curr1 = curr1.next
        else:
            curr.next = curr2
            curr2 = curr2.next
        curr = curr.next
    curr.next = curr1 or curr2

    return head.next