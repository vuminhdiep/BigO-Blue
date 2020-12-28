import queue
import heapq


def minHeapify(i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < len(h) and h[left] < h[smallest]:
        smallest = left
    if right < len(h) and h[right] < h[smallest]:
        smallest = right
    if smallest != i:
        h[i], h[smallest] = h[smallest], h[i]
        minHeapify(smallest)


# Ham xau dung min-heap tu mang h[] cos n phan tu: thuc hien chuan hoa cay tu vi tri cuoi cung co node la
def buildHeap(n):
    for i in range(n // 2 - 1, -1, -1):
        minHeapify(i)


if __name__ == '__main__':
    h = [7, 12, 6, 10, 17, 15, 2, 4]
    buildHeap(len(h))
    print(h)


# Tim phan tu nho nhat min-heap
def top():
    return h[0]


# Them phan tu vao min-heap
def push(value):
    h.append(value)
    i = len(h) - 1
    while i != 0 and h[(i - 1) // 2] > h[i]:
        h[i], h[(i - 1) // 2] = h[(i - 1) // 2], h[i]
        i = (i - 1) // 2


# Xoa phan tu dau min-heap
def pop():
    length = len(h)
    if length == 0:
        return
    h[0] = h[length - 1]
    h.pop()
    minHeapify(0)


# Khai bao va su dung Max-heap
class PQEntry:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value


a = [7, 12, 6, 10, 17, 15, 2, 4]
pq = queue.PriorityQueue()
for x in a:
    pq.put(PQEntry(x))

value = pq.queue[0]  # Tra ve gia tri node goc cua PQ
print(value)

pq.put(3)  # Them mot phan tu vao PQ

val = pq.get()  # Xoa phan tu dau trong PQ
print(val)

# Xoa toan bo phan tu trong PQ
pq = queue.PriorityQueue()

a = [7, 12, 6, 10, 17, 15, 2, 4]
heap_q = []
for x in a:
    heapq.heappush(heap_q,PQEntry(x))

#Tao heap tu 1 list co san
heap_list = [7,12,6,10,17,15,2,4]
heapq.heapify(heap_list)
print(heap_list)
var = heap_list[0] #Tra ve phan tu dau tien trong list chua gia tri nho nhat doi voi min-heap hoac lon nhat doi voi max-heap
print(var)
heapq.heappush(heap_list,3) #Them 1 phan tu vao heap
heapq.heappop(heap_list) #Lay gia tri va xoa phan tu dau trong heap
print(len(heap_list))
heap_list.clear()