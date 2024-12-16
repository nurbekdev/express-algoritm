class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def addTwoNumbers(head1: Node, head2: Node) -> Node:
    carry = 0
    curr1, curr2 = head1, head2
    head = curr = Node(0)

    while curr1 or curr2:
        total = sum([
            curr1.val if curr1 else 0,
            curr2.val if curr2 else 0,
            carry
        ])
        digit = total % 10
        carry = total // 10
        curr.next = Node(digit)
        curr = curr.next

        if curr1:
            curr1 = curr1.next
        if curr2:
            curr2 = curr2.next

    if carry:
        curr.next = Node(carry)

    return head.next