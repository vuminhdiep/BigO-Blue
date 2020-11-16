#Validate the maze
import queue

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
MAX = 21
visited = [[False] * MAX for _ in range(MAX)]
maze = [None] * MAX


class Cell:
    def __init__(self, _r, _c):
        self.r = _r
        self.c = _c


def isValid(r, c):
    return r in range(n) and c in range(m)


def BFS(s, f):
    q = queue.Queue()
    visited[s.r][s.c] = True
    q.put(s)

    while not q.empty():
        u = q.get()
        if u.r == f.r and u.c == f.c:
            return True

        for i in range(4):
            r = u.r + dr[i]
            c = u.c + dc[i]

            if isValid(r, c) and maze[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                q.put(Cell(r, c))

    return False


Q = int(input())

for _ in range(Q):
    n, m = map(int, input().split())

    for i in range(n):
        maze[i] = input()

    entrance = []

    for i in range(n):
        for j in range(m):
            visited[i][j] = False
            if maze[i][j] == '.' and (i == 0 or j == 0 or i == n - 1 or j == m - 1):
                entrance.append(Cell(i, j))

    if (len(entrance)) != 2:
        print("invalid")
    else:
        s = entrance[0]
        f = entrance[1]
        print("valid" if BFS(s, f) else "invalid")