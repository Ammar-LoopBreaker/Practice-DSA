# Question: Implement a singly linked list with append, prepend, delete, find and reverse.
# Example: 1,2,3 then prepend 0 -> 0 -> 1 -> 2 -> 3
"""Singly Linked List with common operations."""


class Node:
    def __init__(self, data):
        self.data, self.next = data, None


class SinglyLinkedList:
    """Supports append, prepend, delete, find, reverse and iteration."""

    def __init__(self):
        self.head = None

    def prepend(self, data) -> None:          # O(1)
        node = Node(data)
        node.next, self.head = self.head, node

    def append(self, data) -> None:           # O(n)
        node = Node(data)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def delete(self, data) -> bool:           # remove first match
        if not self.head:
            return False
        if self.head.data == data:            # deleting the head
            self.head = self.head.next
            return True
        cur = self.head
        while cur.next:
            if cur.next.data == data:         # bypass the matching node
                cur.next = cur.next.next
                return True
            cur = cur.next
        return False

    def find(self, data) -> bool:
        return any(x == data for x in self)

    def reverse(self) -> None:                # O(n) time, O(1) space
        prev, cur = None, self.head
        while cur:
            nxt = cur.next
            cur.next, prev, cur = prev, cur, nxt
        self.head = prev

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.data
            cur = cur.next

    def __repr__(self) -> str:
        return " -> ".join(map(str, self)) + " -> None"


if __name__ == "__main__":
    ll = SinglyLinkedList()
    for v in (1, 2, 3):
        ll.append(v)
    ll.prepend(0)
    print(ll)              # 0 -> 1 -> 2 -> 3 -> None
    ll.delete(2)
    ll.reverse()
    print(ll, ll.find(1))  # 3 -> 1 -> 0 -> None True
