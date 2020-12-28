# MUH and Important Things
# n = int(input())
# h = [int(i) for i in input().split()]
# s = sorted([(h[i], i) for i in range(n)])
# f = [s[i][1] for i in range(n)]
# swp = []
# print(s)
# print(f)
# for i in range(n-1):
#     if s[i][0] == s[i+1][0]:
#         swp.append((i,i+1))
#     if len(swp)==2:
#         print('YES')
#         print(' '.join(str(k+1) for k in f))
#         for i,j in swp:
#             f[i],f[j]=f[j],f[i]
#             print(' '.join(str(l+1) for l in f))
#         exit()
# print('NO')


# Fibsieve Fantabulous
# if we find this number sqrt and use ceil function so now we find sqrt is 4. so we find our column = sqrt.
# and now my work is how to way we find this row. so if we use row = number - (sqrt -1) * (sqrt - 1)  = 10 - (4 - 1) * (4 - 1) = 10 - 3*3 = 10 - 9 = 1.
# so we find out expected output is row = 1 and our column = 4.
# if our input is 25 so now we find our row and column in this number.
# our extra number = sqrt(25)* sqrt(25) - 25 = 5*5 - 25 = 0.  so our column = 5 and row = extra number + 1 = 0+1 = 1.
# so now we find our column number is 5 and our row number is 1.


# import math
# t = int(input())
# for i in range(t):
#     n = int(input())
#     sqt = math.ceil(math.sqrt(n))
#     exit_num = sqt*sqt-n
#     row = 0
#     col = 0
#     if exit_num < sqt:
#         row = exit_num+1
#         col = sqt
#     else:
#         row = sqt
#         col = n-(sqt-1)*(sqt-1)
#     if sqt%2 == 0:
#         row,col = col,row
#
#     res = "Case {num}: {r} {c}".format(num=i+1,r=row,c=col)
#     print(res)

# Uniquitous Religions
MAX = 20
parent = []
ranks = []

def makeSet():
    global parent, ranks
    parent = [i for i in range(MAX + 5)]
    ranks = [0 for i in range(MAX + 5)]

#Path Compression

def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]

#Union By Rank

def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] += 1
tc = 1
while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    for i in range(n):
        makeSet()
    ans = n
    for i in range(m):
        u, v = map(int, input().split())
        unionSet(u,v)
    print("Case", tc, ans)
    tc += 1

#Freckles
# import sys
# import heapq
# from math import sqrt
#
#
# def load_int():
#     return int(sys.stdin.readline())
#
#
# def load_floats():
#     line = sys.stdin.readline()
#     return list(map(float, line.split()))
#
#
# def load_case():
#     sys.stdin.readline()
#     nfreckles = load_int()
#
#     freckles = []
#     for n in range(nfreckles):
#         freckles.append(tuple(load_floats()))
#
#     return freckles
#
#
# def point_dist(v1, v2):
#     return sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2)
#
#
# def min_tree(points):
#     """Use Prim's min spanning tree algorithm, to build min
#     spannig tree"""
#     # Initialize spanning tree
#     vertices = [0, ]  # Spanning tree vertices
#     edges = []  # Spanning tree edges
#
#     # Initialize free vertices not in tree (distance, vertex, tree_vertex)
#     free = [(99999999999, i + 1, 0) for i, v in enumerate(points[1:])]
#
#     def update_free(vertex):
#         """Update distances from free vertices to tree after adding one
#         of the free vertices to the tree"""
#         coordv = points[vertex]
#         for i, f in enumerate(free):
#             dist, fvertex, _ = f
#             coordf = points[fvertex]
#             ndist = point_dist(coordf, coordv)
#             if ndist < dist:
#                 free[i] = (ndist, fvertex, vertex)
#
#         heapq.heapify(free)
#
#     update_free(0)  # Initialize for first vertex
#
#     # Iterate through free vertex
#     while free:
#         dist, fvertex, vertex = heapq.heappop(free)
#         vertices.append(fvertex)
#         edges.append((vertex, fvertex))
#
#         update_free(fvertex)
#
#     return vertices, edges
#
#
# if __name__ == '__main__':
#
#     ncases = load_int()
#
#     for c in range(ncases):
#         points = load_case()
#         vertices, edges = min_tree(points)
#
#         # The min length is the sum of the min spanning tree edges
#         length = sum([point_dist(points[s], points[e]) for s, e in edges])
#         print("{0:.2f}".format(length))
#
#         if c + 1 < ncases:
#             print('')


#Phone List
# class Node:
#     def __init__(self):
#         self.end_word = False
#         self.child = dict()
#
#
# def addWord(root, s):
#     temp = root
#     s_prefix_other = False
#     other_prefix_s = True
#
#     for ch in s:
#         if ch not in temp.child:
#             temp.child[ch] = Node()
#             other_prefix_s = False
#
#         temp = temp.child[ch]
#         if temp.end_word:
#             s_prefix_other = True
#
#     temp.end_word = True
#     return s_prefix_other or other_prefix_s
#
#
# t = int(input())
# for tc in range(t):
#     n = int(input())
#     root = Node()
#     is_inconsistent = False
#
#     for _ in range(n):
#         if not is_inconsistent:
#             is_inconsistent = addWord(root, input())
#         else:
#             input()
#
#     print('NO' if is_inconsistent else 'YES')