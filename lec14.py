# class Node:
#     def __init__(self):
#         self.countWord = 0
#         self.child = dict()
#
#
# def addWord(root, s):
#     temp = root
#     for ch in s:
#         if ch not in temp.child:
#             temp.child[ch] = Node()
#         temp = temp.child[ch]
#     temp.countWord += 1
#
#
# def findWord(root, s):
#     temp = root
#     for ch in s:
#         if ch not in temp.child:
#             return False
#         temp = temp.child[ch]
#     return temp.countWord > 0
#
#
# def isWord(node):
#     return node.countWord != 0
#
#
# def isEmpty(node):
#     return len(node.child) == 0
#
#
# def removeWord(root, s, level, len):
#     if root == None:
#         return False
#     if level == len:
#         if root.countWord > 0:
#             root.countWord -= 1
#             return True
#         return False
#     ch = s[level]
#     flag = removeWord(root.child[ch], s, level + 1, len)
#     if flag == True and isWord(root.child[ch]) == False and isEmpty(root.child[ch]) == True:
#         del root.child[ch]
#         root.child[ch] = None
#     return flag
#
#
# def printWord(root, s):
#     if isWord(root):
#         print(s)
#     for ch in root.child:
#         printWord(root.child[ch], s + ch)


class Node:
    def __init__(self, value):
        self.countWord = 0
        self.child = dict()
        self.weight = value


def addWord(root, s, val):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node(val)
        temp = temp.child[ch]
        if val > temp.weight:
            temp.weight = val
    temp.countWord += 1


def findWord(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            return False
        temp = temp.child[ch]
    return temp.weight


n, q = list(map(int, input().split()))

root = Node(0)

for _ in range(n):
    word, weight = input().split()
    addWord(root, word, int(weight))

results = []
for _ in range(q):
    rq = input()
    results.append(findWord(root, rq))

for item in results:
    if not item:
        print(-1)
    else:
        print(item)