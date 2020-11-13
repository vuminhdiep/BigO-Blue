# Bishu and his Girlfriend

n = int(input())
graph = []


def dfs(start):
    visited = [False] * n
    stack = []
    dist[start] = 0
    stack.append(start)
    while len(stack) != 0:
        u = stack.pop()
        for v in graph[u]:
            if not visited[v]:
                dist[v] = dist[u] + 1
                visited = True
                stack.append(v)


for i in range(0, n-1):
    u, v = input().split()
    u, v = int(u), int(v)
    graph[u].append(v)
    graph[v].append(u)

dist = [-1] * n
dfs(1)

q = int(input())
minDist = 1005
id = 0
for i in range(0,q):
    u = int(input())
    if minDist > dist[u] or minDist == dist[u] and id > u:
        minDist = dist[u]
        id = u


print(id)
