# Dung list de bieu dien stack
stack = [3, 2, 5, 7, 9, 12, 37]

# Xoa phan tu tren cung cua stack
value = stack.pop()

# Lay gia tri tren cung stack
val = stack[-1]

# Lay kich thuoc cua stack
n = len(stack)

# Hoan doi 2 stack voi nhau bang phep gan
s1 = [1, 2, 3]
s2 = [4, 5, 6]
s1, s2 = s2, s1

import queue

q = queue.Queue()
#Them phan tu vao queue
q.put(5)
q.put(7)
q.put(3)

#Xoa phan tu khoi queue va co the lay duoc gia tri ve
val = q.get()

#Lay phan tu dau queue
first = q.queue[0]

#Lay kich thuoc cua queue
length = q.qsize()

#Kiem tra queue rong
q.empty()

#Dung phep gan de hoan doi 2 queue
q1 = queue.Queue()
q1.put(1)
q1.put(2)
q1.put(3)

q2 = queue.Queue()
q2.put(4)
q2.put(5)
q2.put(6)

q1, q2 = q2, q1

