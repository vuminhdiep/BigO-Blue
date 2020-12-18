#MST
import queue
INF = 1e9
class Node:
    def __init__(self,index,dist):
        self.index = index
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.weight
n, m = map(int,input().split())
graph = []
for i in range(m):
    u,v,w = map(int,input().split())
    u -= 1
    v -= 1
    graph[u].append(Node(v, w))
    graph[v].append(Node(u, w))

res = Prim(0)
print(res)