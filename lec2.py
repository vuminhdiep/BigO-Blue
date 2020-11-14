# Array
# n, k = map(int, input().split())
# a = [int(i) for i in input().split()]
# d = {}
# j = 1
# for x in a:
#     if len(d) == k:
#         break
#     d[x] = j
#     j += 1
#
# if len(d) == k:
#     print(min(d.values()), max(d.values()))
# else:
#     print("-1 -1")

<<<<<<< HEAD
# n, k = map(int, input().split())
# a = [int(i) for i in input().split()]
# f = [0]*n
# unique = 0
# i = 1
# # for i in range(1,n):
#     #read a[i]
# for j in range(1,n):
#     if f[a[j]]==0:
#         unique+=1
#     f[a[j]]+=1
#     while unique==k:
#         f[a[i]]-=1
#         if f[a[i]]==0:
#             print(i, j)
#             break
#         i+=1
# print("-1 -1")

#George and Round
=======
# George and Round
>>>>>>> d6aa37f9f9e97e478d41b7ef5a41b74caf9e83d7
# n, m = map(int, input().split())
# a = [int(i) for i in input().split()]
# b = [int(j) for j in input().split()]
# pointer_a = 0
# pointer_b = 0
# while pointer_a < n and pointer_b < m:
<<<<<<< HEAD
#     if a[pointer_a] <= b[pointer_b]: #Lack of number with complexity b
#         pointer_a+=1
#     pointer_b+=1
# print(n-pointer_a) #Print out the needed problems

#Books

# n,t=map(int,input().split())
# l=[int(k) for k in input().split()]
# a=j=0
# for i in range(n):
#     a+=l[i]
#     if a>t:
#         a-=l[j]
#         j+=1
# print(n-j)

#Sereja and Dima

n = int(input())
l = [int(k) for k in input().split()]
s = 0
d = 0
for i in range(n):
    draw_card = max(l[0],l[-1])
    if i%2==0:
        s+=draw_card
    else:
        d+=draw_card
    l.remove(draw_card)
print(s,d)

=======
#     if a[pointer_a] <= b[pointer_b]:  # Lack of number with complexity b
#         pointer_a += 1
#     pointer_b += 1
# print(n - pointer_a)  # Print out the needed problems

# Books
# n, t = map(int, input().split())
# l = [int(k) for k in input().split()]
# a = j = 0
# for i in range(n):
#     a += l[i]
#     if a > t:
#         a -= l[j]
#         j += 1
# print(n - j)

# Sereja and Dija
# n = int(input())
# l = [int(k) for k in input().split()]
# s = 0
# d = 0
# for i in range(n):
#     draw_card = max(l[0], l[-1])
#     if i % 2 == 0:
#         s += draw_card
#     else:
#         d += draw_card
#     l.remove(draw_card)
# print(s, d)

# Dress em in Vest
n, m, x, y = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(j) for j in input().split()]
l = []
i = 0
j = 0
while j < len(b) and i < len(a):
    if a[i] - x <= b[j] <= a[i] + y:
        l.append((i + 1, j + 1))  # Add people with fit vest starting from index 1
        j += 1
        i += 1
    elif b[j] > a[i] + y:
        i += 1
    elif b[j] < a[i] + x:
        j += 1
print(len(l)) #Number of maximum people
for k in l:
    print(k[0], k[1])
>>>>>>> d6aa37f9f9e97e478d41b7ef5a41b74caf9e83d7
