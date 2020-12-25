# Khai bao class Node voi id la ten dinh, dist la chi phi.
# define operator __lt__ (less than) cho class, so sanh theo dist nho hon, dung trong PriorityQueue

import queue

MAX = 100
INF = int(1e9)


class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist <= other.dist


def Dijkstra(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    while not pq.empty():
        top = pq.get()
        u = top.id
        w = top.dist
        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.dist
                pq.put(Node(neighbor.id, dist[neighbor.id]))
                path[neighbor.id] = u


if __name__ == '__main__':
    n = int(input())
    s, t = 0, 4
    graph = [[] for i in range(n + 5)]
    dist = [INF for i in range(n + 5)]
    path = [-1 for i in range(n + 5)]
    for i in range(n):
        d = list(map(int, input().split()))
        for j in range(n):
            if d[j] > 0:
                graph[i].append(Node(j, d[j]))
        Dijkstra(s)
        ans = dist[t]
        print(ans)
