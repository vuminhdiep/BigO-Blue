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

# Search Engine
# class Node:
#     def __init__(self, value):
#         self.countWord = 0
#         self.child = dict()
#         self.weight = value
#
#
# def addWord(root, s, val):
#     temp = root
#     for ch in s:
#         if ch not in temp.child:
#             temp.child[ch] = Node(val)
#         temp = temp.child[ch]
#         if val > temp.weight:
#             temp.weight = val
#     temp.countWord += 1
#
#
# def findWord(root, s):
#     temp = root
#     for ch in s:
#         if ch not in temp.child:
#             return False
#         temp = temp.child[ch]
#     return temp.weight
#
#
# n, q = list(map(int, input().split()))
#
# root = Node(0)
#
# for _ in range(n):
#     word, weight = input().split()
#     addWord(root, word, int(weight))
#
# results = []
# for _ in range(q):
#     rq = input()
#     results.append(findWord(root, rq))
#
# for item in results:
#     if not item:
#         print(-1)
#     else:
#         print(item)


# Contacts

# contacts_book = dict()
#
#
# def add(word):
#     temp = contacts_book
#     for ch in word:
#         if ch not in temp:
#             temp[ch] = {}
#             temp[ch]['count'] = 1
#         else:
#             temp[ch]['count'] += 1
#         temp = temp[ch]
#     temp[None] = None
#
#
# def find(word):
#     temp = contacts_book
#     for ch in word:
#         if ch not in temp:
#             return 0
#         temp = temp[ch]
#     return temp['count']
#
#
# n = int(input())
# for i in range(n):
#     q = input().strip().split(' ')
#     operation = q[0]
#     name = q[1]
#     if operation == 'add':
#         add(name)
#     else:
#         print(find(name))

# No Prefix Set

# def add(root, s):
#     temp = root
#     length = len(s)
#     for ch, char in enumerate(s):
#         if char in temp:
#             if temp[char]:
#                 if ch == length - 1:
#                     return False
#                 else:
#                     temp = temp[char]
#             else:
#                 return False
#         else:
#             temp[char] = dict()
#             temp = temp[char]
#
#     return True
#
#
# if __name__ == '__main__':
#     n = int(input())
#     trie = dict()
#
#     bad = False
#     for i in range(n):
#         new = input()
#         if not add(trie, new):
#             bad = True
#             break
#
#     if bad:
#         print("BAD SET")
#         print(new)
#     else:
#         print("GOOD SET")

# Consistency Checker


def add(root, s):
    temp = root
    length = len(s)
    for ch, char in enumerate(s):
        if char in temp:
            if temp[char]:
                if ch == length - 1:
                    return False
                else:
                    temp = temp[char]
            else:
                return False
        else:
            temp[char] = dict()
            temp = temp[char]

    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        trie = dict()
        consistency = False
        n = int(input())
        for j in range(n):
            new = input()
            if not add(trie, new):
                consistency = True
                break

        if consistency:
            print(f"Case {i+1}: NO")
        else:
            print(f"Case {i+1}: YES")

