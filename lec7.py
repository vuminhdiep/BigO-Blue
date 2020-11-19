# Monk and Multiplication
# import heapq
#
# N = int(input())
#
# arr = list(map(int, input().split()))
#
# heap = []
#
# for i in arr:
#
#     heapq.heappush(heap, -i)
#
#     if len(heap) < 3:
#         print(-1)
#
#         continue
#
#     largest = heapq.heappop(heap)
#
#     second_largest = heapq.heappop(heap)
#
#     third_largest = heapq.heappop(heap)
#
#     print(-1 * largest * second_largest * third_largest)
#
#     heapq.heappush(heap, largest)
#
#     heapq.heappush(heap, second_largest)
#
#     heapq.heappush(heap, third_largest)
#

def __init__(self):
    self.h = []


def minHeapify(self,i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < len(self.h) and self.h[left] < self.h[smallest]:
        smallest = left
    if right < len(self.h) and self.h[right] < self.h[smallest]:
        smallest = right
    if smallest != i:
        self.h[i], self.h[smallest] = self.h[smallest], self.h[i]
        minHeapify(smallest)


def buildHeap(n):
    for i in range(n // 2 - 1, -1, -1):
        minHeapify(i)


def top(self):
    return self.h[0]

#QHeap 1 Hackerrank
#
# import heapq
# n = int(input())
# heap = []
# for i in range(n):
#     Q = list(map(int, input().split()))
#     type = Q[0]
#     if type == 1:
#         heapq.heappush(heap, Q[1])
#     elif type == 2:
#         root = heap[0]
#         heap.remove(Q[1])
#         if root == Q[1]:
#             heapq.heapify(heap)
#     elif type == 3:
#         print(heap[0])
#
# import heapq
# heap = []
# N = int(input())
# di = dict()
# for i in range(N):
#     Q = input().split()
#     if Q[0] == '1':
#         Q = int(Q[1])
#         di[Q] = 0
#         heapq.heappush(heap, Q)
#     elif Q[0] == '2':
#         Q = int(Q[1])
#         di[Q] = 1
#     else:
#         while di[heap[0]] == 1:
#             heapq.heappop(heap)
#         print(heap[0])

#Roy and Trending Topics

import heapq
n = int(input())
ls = []
for _ in range(n):
    id, z, p, l, c, s = map(int, input().split())
    z_score = p * 50 + l * 5 + c * 10 + s * 20
    change = z_score - z
    ls.append([change, id, z_score])

data = heapq.nlargest(5, ls)

for i, j, k in data:
    print(j, k)