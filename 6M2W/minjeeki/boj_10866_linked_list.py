# 실버 4. 덱
# 이중 연결 리스트로 덱 구현
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push_front(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    def push_back(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def pop_front(self):
        if self.head is None:
            return -1
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        self.size -= 1
        return value
    
    def pop_back(self):
        if self.tail is None:
            return -1
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        self.size -= 1
        return value
    
    def get_front(self):
        return self.head.value if self.head else -1
    
    def get_back(self):
        return self.tail.value if self.tail else -1
    
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return 1 if self.size == 0 else 0

deque = Deque()

N = int(input())
for _ in range(N):
    line = input().split()
    if line[0] == "push_front":
        deque.push_front(int(line[1]))
    elif line[0] == "push_back":
        deque.push_back(int(line[1]))
    elif line[0] == "pop_front":
        print(deque.pop_front())
    elif line[0] == "pop_back":
        print(deque.pop_back())
    elif line[0] == "size":
        print(deque.get_size())
    elif line[0] == "empty":
        print(deque.is_empty())
    elif line[0] == "front":
        print(deque.get_front())
    elif line[0] == "back":
        print(deque.get_back())
