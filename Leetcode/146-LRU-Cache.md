# LRU Cache

> - Difficulty: Medium
> - Type: Linked List
> - [link](https://leetcode.com/problems/lru-cache/)

## Solution
- Time complexity: "get" and "put" O(1)
- Space complexity: O(n) - linked list of length n and hash map holding n items
- An LRU cache is built by combining two data structures: a doubly linked list and a hash map.
- [LRU Cache Implementation - Interview Cake](https://www.interviewcake.com/concept/java/lru-cache#:~:text=An%20LRU%20cache%20tracking%20n,(as%20opposed%20to%20one).)


```python
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key] # We store the key in our Node object in order to use the key to delete from the cache hashmap
```
