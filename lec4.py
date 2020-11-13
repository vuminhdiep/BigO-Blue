# Transform the Expression
# def transform(expression):
#     s = []
#     for symbol in expression:
#         if symbol.isalpha():
#             print(symbol, end='')
#         elif symbol == ')':
#             print(s.pop(), end='')
#         elif symbol != '(':
#             s.append(symbol)
#     print()
#
#
# t = int(input())
# for i in range(t):
#     expression = input()
#     transform(expression)

#Ferry Loading III
import queue


class Car:
    def __init__(self, _id, _arriveTime):
        self.id = _id
        self.arriveTime = _arriveTime


Q = int(input())

for _ in range(Q):
    qSide = [[], []]
    qSide[0] = queue.Queue()
    qSide[1] = queue.Queue()
    res = [0] * 10005

    n, t, m = map(int, input().split())

    for i in range(m):
        arrived, atBank = input().split()

        if atBank == "left":
            qSide[0].put(Car(i, int(arrived)))
        else:
            qSide[1].put(Car(i, int(arrived)))

    curTime, curSide = 0, 0
    waiting = (not qSide[0].empty()) + (not qSide[1].empty())

    while waiting:
        if waiting == 1:
            nextTime = qSide[1].queue[0].arriveTime if qSide[0].empty() else qSide[0].queue[0].arriveTime
        else:
            nextTime = min(qSide[0].queue[0].arriveTime, qSide[1].queue[0].arriveTime)

        curTime = max(curTime, nextTime)
        carried = 0

        while not qSide[curSide].empty():
            car = qSide[curSide].queue[0]
            if car.arriveTime <= curTime and carried < n:
                res[car.id] = curTime + t
                carried += 1
                qSide[curSide].get()
            else:
                break

        curTime += t
        curSide = 1 - curSide
        waiting = (not qSide[0].empty()) + (not qSide[1].empty())

    for i in range(m):
        print(res[i])

    if _ < Q - 1:
        print()
#That is Your Queue
from collections import deque

tc = 1

while True:
    P, C = map(int, input().split())
    if P == 0 and C == 0:
        break

    q = deque()
    for i in range(1, min(P, C) + 1):
        q.append(i)

    print('Case {}:'.format(tc))
    tc += 1

    for _ in range(C):
        line = input().split()
        cmd = line[0]

        if cmd == 'N':
            print(q[0])
            q.append(q.popleft())
        else:
            x = int(line[1])
            n = len(q)
            q.append(x)
            for i in range(n):
                temp = q.popleft()
                if temp != x:
                    q.append(temp)