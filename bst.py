from __future__ import annotations

class Node:
    def __init__(self, value):
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None

class BST:
    def __init__(self):
        self.root: Node | None = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        current_pos = self.root
        while True:
            if value < current_pos.value:
                if current_pos.left is None:
                    current_pos.left = Node(value)
                    return
                current_pos = current_pos.left
            else:
                if current_pos.right is None:
                    current_pos.right = Node(value)
                    return
                current_pos = current_pos.right

    def delete(self, value):
        parent = None
        current = self.root
        while current is not None and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right
        if current is None:
            return

        if current.left is not None and current.right is not None:
            smallest_parent = current
            smallest = current.right
            while smallest.left is not None:
                smallest_parent = smallest
                smallest = smallest.left
            current.value = smallest.value
            parent = smallest_parent
            current = smallest

        child = current.left if current.left is not None else current.right
        if parent is None:
            self.root = child
        elif parent.left is current:
            parent.left = child
        else:
            parent.right = child

    def find(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return current
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return None