# Bishu and his Girlfriends

# load input data

# number of node
import sys
sys.setrecursionlimit(10000000)

n = int(input())

visited = [0] * (n + 1)
graph = [[] for i in range(n + 1)]
dist = [0] * (n + 1)

# it's tree, i.e. n -1 edges
for i in range(n - 1):
    u , v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# number of girls
q = int(input())
girls = []

for i in range(q):
    girl = int(input())
    girls.append(girl)


def dfs(node, distance):
    visited[node] = 1
    dist[node] = distance

    for child in graph[node]:
        if not visited[child]:
            #graph[child] = distance + 1

            dfs(child, distance + 1)


dfs(1, 0)

min_dis = 10000000
best_girl = 0
for girl in girls:
    if dist[girl] < min_dis:
        min_dis = dist[girl]
        best_girl = girl
    elif dist[girl] == min_dis and girl < best_girl:
        best_girl = girl

print(best_girl)

#Lakes in Berland
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
MAX = 51
visited = [[False] * MAX for _ in range(MAX)]
table = []
lakes = []


def DFS(sr, sc):
    s = [(sr, sc)]
    visited[sr][sc] = True

    isOcean = False
    temp = []

    while len(s):
        ur, uc = s.pop()
        temp.append((ur, uc))

        if ur == 0 or uc == 0 or ur == n - 1 or uc == m - 1:
            isOcean = True

        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]

            if r in range(n) and c in range(m) and table[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                s.append((r, c))

    if not isOcean:
        lakes.append(temp)


n, m, k = map(int, input().split())

for _ in range(n):
    table.append(list(input()))

for i in range(n):
    for j in range(m):
        if not visited[i][j] and table[i][j] == '.':
            DFS(i, j)

lakes.sort(key=lambda lake: len(lake))
sum_cell = 0

for i in range(len(lakes) - k):
    sum_cell += len(lakes[i])
    for r, c in lakes[i]:
        table[r][c] = '*'

print(sum_cell)

for i in range(n):
    print(''.join(table[i]))