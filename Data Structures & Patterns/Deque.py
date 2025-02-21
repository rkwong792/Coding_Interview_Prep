from collections import deque

# 1️⃣ Creating an empty deque
dq = deque()
print("Empty deque:", dq)

# 2️⃣ Creating a deque with initial elements
dq = deque([1, 2, 3])
print("Initialized deque:", dq)

# 3️⃣ Adding elements to deque
dq.append(4)        # Add to right
dq.appendleft(0)    # Add to left
print("After append & appendleft:", dq)

# 4️⃣ Removing elements from deque
dq.pop()         # Removes from right
dq.popleft()     # Removes from left
print("After pop & popleft:", dq)

# 5️⃣ Using deque as a Queue (FIFO)
queue = deque()
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue before dequeuing:", queue)
print("Dequeue:", queue.popleft())  # First in, first out
print("Queue after dequeuing:", queue)

# 6️⃣ Using deque as a Stack (LIFO)
stack = deque()
stack.append("X")
stack.append("Y")
stack.append("Z")
print("Stack before popping:", stack)
print("Pop:", stack.pop())  # Last in, first out
print("Stack after popping:", stack)

# 7️⃣ Setting a maximum size (circular buffer behavior)
fixed_dq = deque(maxlen=3)
fixed_dq.append(1)
fixed_dq.append(2)
fixed_dq.append(3)
print("Fixed deque (before overflow):", fixed_dq)
fixed_dq.append(4)  # Oldest element (1) is removed
print("Fixed deque (after overflow):", fixed_dq)

# 8️⃣ Rotating a deque
dq = deque([1, 2, 3, 4, 5])
print("Deque before rotation:", dq)
dq.rotate(2)  # Rotate right by 2
print("Deque after rotating right by 2:", dq)
dq.rotate(-1)  # Rotate left by 1
print("Deque after rotating left by 1:", dq)

# 9️⃣ Extending a deque
dq = deque([1, 2, 3])
dq.extend([4, 5])  # Add to right
print("After extend:", dq)
dq.extendleft([0, -1])  # Add to left (note: reversed order)
print("After extendleft:", dq)

print("\n✅ All deque operations demonstrated successfully!")
