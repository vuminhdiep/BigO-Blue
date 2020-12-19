class Node:
    def __init__(self):
        self.key = 0
        self.left = None
        self.right = None


def createNode(x):
    newNode = Node()
    newNode.key = x
    return newNode


def insertNode(root, x):
    if root == None:
        return createNode(x)
    if x < root.key:
        root.left = insertNode((root.left), x)
    elif x > root.key:
        root.right = insertNode(root.right, x)
    return root


def createTree(a, n):
    root = None
    for i in range(n):
        root = insertNode(root, a[i])
    return root


def searchNode(root, x):
    if root == None or root.key == x:
        return root
    if root.key < x:
        return searchNode(root.right, x)
    return searchNode(root.left, x)


def deleteNode(root, x):
    if root == None:
        return root
    if x < root.key:
        root.left = deleteNode(root.left, x)
    elif x > root.key:
        root.right = deleteNode(root.right, x)
    else:
        if root.left == None:
            temp = root.right
            del root
            return temp
        elif root.right == None:
            temp = root.left
            del root
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root


def minValueNode(node):
    current = node
    while current.left != None:
        current = current.left
    return current


# Duyet Binary Search Tree

def traversalTree(root):
    if root != None:
        traversalTree(root.left)
        print(root.key, end=' ')
        traversalTree(root.right)


def size(root):
    if root == None:
        return 0
    return size(root.left) + 1 + size(root.right)


def deleteTree(root):
    if root == None:
        return
    deleteTree(root.left)
    deleteTree(root.right)
    del root


# Trong Python dung set hoac dict

# Khai bao va su dung
s = set()
d = dict()

a = [10, 20, 50, 70, 90]
s = set(a)

d[10] = 'abc'
d[20] = 'def'
d[10] = 'mpk'

# Them phan tu
s.add(60)
d[14] = 'abc'

# Xoa phan tu
s.remove(60)
print(d.pop(14))

# keyError
if s.remove(30, None) == None:
    print('Object not found')
else:
    print('deleted')

if d.pop(30, None) == None:
    print('Key not found')
else:
    print('deleted')

# Kiem tra gia tri co ton tai hay khong
if 20 in s:
    print("exists")
else:
    print("not exists")

if 20 in d:
    print("exists")
else:
    print("not exists")

a = [10, 20, 50, 70, 90]
s = set(a)
print(50 in s)  # Return True or False

print(d.get(14))  # Lay gia tri cua dict theo key
print(d.get(1))  # Return None

# Tra ve danh sach cac phan tu
for value in s:
    print(value)

for item in d.items():
    print(item)

for key in d.keys():
    print(key, end=', ')

for value in d.values():
    print(value, end=', ')

s1 = set([10, 50, 60, 70])
s2 = set([10, 20])

d1 = {10:'mpk',14:'abc',20:'def'}
d2 = {10: 'bigo',22: 'coding'}
s1.update(s2) #Them cac phan tu cua set nay vao set khac, neu nhu co key trung thi bo qua
d1.update(d2) #Them cac phan tu cua dict nay vao dict khac, neu nhu co key trung thi value cua key se duoc lay theo value trong dict thu 2

s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)
s2 = s1.copy()

d2 = d1.copy()

len(s)
s.clear()

len(d)
d.clear()