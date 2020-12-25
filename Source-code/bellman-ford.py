INF = 10 ** 9
MAX = 105


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


dist = [INF for _ in range(MAX)]
path = [-1 for _ in range(MAX)]
graph = []

def BellmanFord(s):
    dist[s] = 0
    for i in range(1,n):
        for j in range(m):
            u = graph[j].source
            v = graph[j].target
            w = graph[j].weight
            if (dist[u] != INF) and (dist[u]+ w < dist[v]):
                dist[v] = dist[u] + w
                path[v] = u

    for i in range(m):
        u = graph[i].source
        v = graph[i].target
        w = graph[i].weight
        if (dist[u] != INF) and (dist[u] + w < dist[v]):
            return False
    return True

if __name__ == '__main__':
    n, m = map(int,input().split())
    for i in range(m):
        u,v,w = map(int,input().split())
        graph.append(Edge(u,v,w))
    s,t = 0,4
    res = BellmanFord(s)
    if not res:
        print("Graph contains negative weight cycle")
    else:
        print(dist[t])