class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def getIntersectionNode(headA: Node, headB: Node) -> Node:
    if not headA or not headB:
        return None

    pointerA, pointerB = headA, headB

    while pointerA != pointerB:
        pointerA = pointerA.next if pointerA else headB
        pointerB = pointerB.next if pointerB else headA

    return pointerA
