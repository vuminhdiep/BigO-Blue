# nA, nB = (map(int, input().split()))
# k, m = (map(int, input().split()))
#
# listA = list(map(int, input().split()))
# listB = list(map(int, input().split()))
#
# if listA[k-1] < listB[nB-m]: #if first k numbers in A < last m number in B
#     print("YES")
# else:
#     print("NO")

n = int(input())
m = []
for i in range(n):
    a, b = map(int, input().split())
    m.append([a, b])

min_val = min([x[0] for x in m]) #Get the smallest value possible in the segments
max_val = max([x[1] for x in m]) #Get the biggest value possible in the segments
seg = [min_val, max_val] #The segment with smallest and biggest value will cover all segments in between
if seg in m:
    print(m.index(seg) + 1)
else:
    print(-1)

