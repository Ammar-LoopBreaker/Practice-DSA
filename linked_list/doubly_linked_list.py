# Question: Implement a doubly linked list with append, prepend, delete and traversal in both directions.
# Example: 1,2,3 then prepend 0, delete 2 -> [0,1,3] and [3,1,0]
"""Doubly Linked List with head and tail pointers."""


class Node:
    def __init__(self, data):
        self.data, self.prev, self.next = data, None, None


class DoublyLinkedList:
    """O(1) append/prepend; delete by value; traversal in both directions."""

    def __init__(self):
        self.head = self.tail = None

    def append(self, data) -> None:
        node = Node(data)
        if not self.tail:
            self.head = self.tail = node
        else:
            node.prev, self.tail.next = self.tail, node
            self.tail = node

    def prepend(self, data) -> None:
        node = Node(data)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next, self.head.prev = self.head, node
            self.head = node

    def delete(self, data) -> bool:
        cur = self.head
        while cur and cur.data != data:
            cur = cur.next
        if not cur:
            return False
        if cur.prev:                        # bypass cur on the left...
            cur.prev.next = cur.next
        else:
            self.head = cur.next
        if cur.next:                        # ...and on the right
            cur.next.prev = cur.prev
        else:
            self.tail = cur.prev
        return True

    def forward(self) -> list:
        out, cur = [], self.head
        while cur:
            out.append(cur.data)
            cur = cur.next
        return out

    def backward(self) -> list:
        out, cur = [], self.tail
        while cur:
            out.append(cur.data)
            cur = cur.prev
        return out


if __name__ == "__main__":
    dll = DoublyLinkedList()
    for v in (1, 2, 3):
        dll.append(v)
    dll.prepend(0)
    dll.delete(2)
    print(dll.forward(), dll.backward())  # [0, 1, 3] [3, 1, 0]
