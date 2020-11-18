# Monk and Multiplication
import heapq

N = int(input())

arr = list(map(int, input().split()))

heap = []

for i in arr:

    heapq.heappush(heap, -i)

    if len(heap) < 3:
        print(-1)

        continue

    largest = heapq.heappop(heap)

    second_largest = heapq.heappop(heap)

    third_largest = heapq.heappop(heap)

    print(-1 * largest * second_largest * third_largest)

    heapq.heappush(heap, largest)

    heapq.heappush(heap, second_largest)

    heapq.heappush(heap, third_largest)


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
