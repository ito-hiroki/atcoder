from collections import deque


class Node:
    def __init__(self, index):
        self.index = index
        self.nears = []
        self.parent = -1
        self.score = 0

    def __repr__(self):
        return f"(index:{self.index}, nears:{self.nears}, parent:{self.parent}, score:{self.score})"


N = int(input())
nodes = [Node(i) for i in range(N+1)]
for i in range(N-1):
    a, b = list(map(int, input().split()))
    nodes[a].nears.append(b)
    nodes[b].nears.append(a)

queue = deque([])

queue.append(nodes[1])
nodes[1].parent = 0

score = 0
while queue:
    node = queue.popleft()
    nears = node.nears
    for near in nears:
        if nodes[near].parent == -1:
            queue.append(nodes[near])
            nodes[near].parent = node.index
            nodes[near].score = node.score + 1
            if node.score + 1 > score:
                max_index = nodes[near].index
                score = node.score + 1

for i in range(len(nodes)):
    nodes[i].parent = -1
    nodes[i].score = 0
nodes[max_index].parent = 0
queue.append(nodes[max_index])

score = 0
while queue:
    node = queue.popleft()
    nears = node.nears
    for near in nears:
        if nodes[near].parent == -1:
            queue.append(nodes[near])
            nodes[near].parent = node.index
            nodes[near].score = node.score + 1
            if node.score + 1 > score:
                max_index = nodes[near].index
                score = node.score + 1

print(score + 1)
