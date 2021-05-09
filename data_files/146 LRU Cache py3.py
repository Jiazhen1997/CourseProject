



class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None


class LRUCache:

    def __init__(self, capacity: int):
        
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity
        self.map = {}

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self._remove(key)
            self._appendleft(node)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(key)
        elif len(self.map) >= self.cap:
            node = self.tail.prev
            self._remove(node.key)

        node = Node(key, value)
        self._appendleft(node)

    def _appendleft(self, node: Node):
        self.map[node.key] = node  
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node

    def _remove(self, key: int):
        node = self.map[key]
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        del self.map[key]  





