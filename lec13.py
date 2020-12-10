#Distinct Count
# t = int(input())
# for i in range(t):
#     n, x = list(map(int, input().split()))
#     arr = input().split()
#     arr = set(arr)
#     if len(arr) == x:
#         print('Good')
#     elif len(arr) < x:
#         print('Bad')
#     elif len(arr) > x:
#         print('Average')

#Monk and his Friends
# t=int(input())
# for i in range(t):
#     n,m=list(map(int,input().split()))
#     arr=list(map(int,input().split()))
#     dic=set()
#     for i in range(n):
#         dic.add(arr[i])
#     for i in range(n,n+m):
#         if arr[i] in dic:
#             print("YES")
#         else:
#             print("NO")
#         dic.add(arr[i])

#Penguins
# n = int(input())
# penguins = {
#     "Emperor Penguin": 0,
#     "Macaroni Penguin": 0,
#     "Little Penguin": 0
# }
# for i in range(n):
#     x = input()
#     if x == "Emperor Penguin":
#         penguins["Emperor Penguin"] += 1
#     elif x == "Macaroni Penguin":
#         penguins["Macaroni Penguin"] += 1
#     elif x == "Little Penguin":
#         penguins["Little Penguin"] += 1
#
# max_penguin = max(penguins["Emperor Penguin"],penguins["Macaroni Penguin"],penguins["Little Penguin"])
#
# key_list = list(penguins.keys())
# val_list = list(penguins.values())
#
# position = val_list.index(max_penguin)
# print(key_list[position])

#Megacity
# n, s = map(int, input().split())
# d = {}
#
# for i in range(n):
#     x, y, k = map(int, input().split())
#     dist = (x ** 2 + y ** 2) ** (1 / 2)
#     if dist not in d:
#         d[dist] = k
#     else:
#         d[dist] += k
#
# lstKey = sorted(d)
# ans = None
# for ele in lstKey:
#     s += d[ele]
#     if s >= 1000000:
#         ans = ele
#         break
# if ans == None:
#     print(-1)
# else:
#     print("%.7f" % (ele))

#Minimum Loss
n = int(input())
l = list(map(int,input().split()))
m = list(l)
m.sort()
mx = 10 ** 10
for i in range(1,len(m)):
    if m[i] - m[i-1] < mx and l.index(m[i]) < l.index(m[i - 1]):
        mx = m[i] - m[i - 1]
print(mx)
