# Fashion in Berland: https://codeforces.com/problemset/problem/691/A

# def check_jacket(v, n):
#     # 1-button jacket
#     if n == 1:
#         if v[0] == 1:
#             return True
#         else:
#             return False
#     count = 0
#     for i in range(n):
#         if v[i] == 0:
#             count += 1
#
#     if count == 1:
#         return True
#     else:
#         return False
#
#
# n = int(input())
# v = list(map(int, input().split()))
# if check_jacket(v, n):
#     print("YES")
# else:
#     print("NO")


# Night at the Museum https://codeforces.com/problemset/problem/731/A

# def main():
#     n = input()
#     s = map(ord, n)
#
#     res = 0
#     curr = 0
#
#     A = ord('a')
#     Z = ord('z')
#
#     for x in s:
#         if A <= x <= Z:
#             x -= A
#             res += min(abs(x - curr), 26 - abs(x - curr))
#             curr = x
#         else:
#             break
#
#     print(res)
#
#
# if __name__ == '__main__':
#     main()

# Bear and Game https://codeforces.com/problemset/problem/673/A

# n = int(input())
# v = list(map(int, input().split()))
#
# start = 0
# watch = 0
# for i in v:
#     if i - start <= 15:
#         watch = i
#         start = i
#     else:
#         break
#
# print(min(90, watch + 15))


#Arrays https://codeforces.com/problemset/problem/572/A

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

#Big Segment https://codeforces.com/problemset/problem/242/B
# n = int(input())
# m = []
# for i in range(n):
#     a, b = map(int, input().split())
#     m.append([a, b])
#
# min_val = min([x[0] for x in m]) #Get the smallest value possible in the segments
# max_val = max([x[1] for x in m]) #Get the biggest value possible in the segments
# seg = [min_val, max_val] #The segment with smallest and biggest value will cover all segments in between
# if seg in m:
#     print(m.index(seg) + 1)
# else:
#     print(-1)
#Vitaly and Strings
# s = input()
# t = input()
# remain = 1
# u = s
# for i in range(0,len(u),-1):
#     if u[i] != 'z':
#         u[i]+=1
#         remain = 0
#         break
#     else:
#         u[i] = 'a'
# if remain == 1:
#     u = 'a'+u
#
# if u != t and len(u) == len(t):
#     print(u)
# else:
#     print("No such string")