class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def find_middle(head):
    fast = slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow

def reverse(head):
    prev = None
    curr = head

    while curr:
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_

    return prev

def is_same(head1, head2):
    while head1 and head2:
        if head1.val != head2.val:
            return False

        head1 = head1.next
        head2 = head2.next
    return True

def isPalindrome(head: Node) -> bool:
    middle = find_middle(head)
    middle = reverse(middle)

    return is_same(head, middle)