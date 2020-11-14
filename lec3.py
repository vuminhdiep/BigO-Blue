# Devu the Dumb Guy
# n, x = map(int, input().split())
# subjects = list(map(int, input().split()))
#
#
# def selfLearning(subjects, x):
#     subjects.sort()
#     min_time = 0
#     for subject in subjects:
#         min_time += subject * x
#         if x > 1:
#             x -= 1
#     return min_time
#
#
# res = selfLearning(subjects, x)
# print(res)

#Chores
# n, a, b = map(int, input().split())
# h = list(map(int, input().split()))
# h.sort()
# print(h[b]-h[b-1])

#Pasha and Tea
# n,w = map(int,input().split())
# a = sorted(list(map(int, input().split())))
# x = min(a[0],a[n]/2)
# print(min(w,x*n*3))

#Towers
n = int(input())
l = list(map(int, input().split()))
l.sort()
n_towers = 1
max_height = 1
cur_height = 1
for i in range(1,n):
    if l[i]==l[i-1]:
        cur_height+=1
        max_height = max(max_height, cur_height)
    else:
        n_towers+=1
        cur_height=1

print(max_height,n_towers)

