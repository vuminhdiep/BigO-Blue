#Energy Exchange
# n, k = map(int, input().split())
# a = sorted(list(map(int, input().split())))
#
# left = 0
# right = a[-1]
#
# for i in range(100):
#     mid = (left + right) / 2.0
#
#     s1 = sum([x - mid for x in a if x >= mid]) * (100 - k) / 100.0
#     s2 = sum([mid - x for x in a if x < mid])
#
#     if s1 >= s2:
#         left = mid
#     else:
#         right = mid
#
# print(left)

#Where is the Marble
# def BinarySearch(a,x):
#     left = 0
#     right = len(a)-1
#     while left <= right:
#         mid = (left+right)//2
#         if a[mid] == x and mid == left or a[mid-1] < a[mid]:
#             return mid
#         elif a[mid] < x:
#             left = mid+1
#         else:
#             right=mid-1
#     return -1
# def main():
#     test = 1
#     while True:
#         n,q = map(int,input().split())
#         if n==0 and q==0:
#             break
#         a = []
#         for i in range(0,n):
#             x = int(input())
#             a.append(x)
#         sorted(a)
#         print("Case# ", test, ": ")
#         for i in range(0,q):
#             x = int(input())
#             index = BinarySearch(a,x)
#             if index==-1:
#                 print(x," not found")
#             else:
#                 print(x, " found at ",index+1)
#         test+=1
#
# if __name__ == '__main__':
#     main()

#Pizzamania


# def findPair(data,length,sum):
#     num_pair = 0
#     if length < 1:
#         return num_pair
#     behind = 0
#     ahead = length-1
#     while ahead > behind:
#         curSum = data[ahead] + data[behind]
#         if curSum == sum:
#             num_pair+=1
#             behind+=1
#             ahead-=1
#         elif curSum > sum:
#             ahead -=1
#         else:
#             behind +=1
#
#     return num_pair
#
# def main():
#     test = int(input())
#     while test > 0:
#         n,m = map(int,input().split())
#         arr = list(map(int, input().split()))
#         sorted(arr)
#         print(findPair(arr,n,m))
#         test -=1
#
#
# if __name__ == '__main__':
#     main()

#The Playboy Chimp

def binSearch(a, length, val):
    left, right = 0, length - 1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == val:
            return mid - 1, mid + 1
        if a[mid] < val:
            left = mid + 1
        else:
            right = mid - 1

    return right, left


def main():

    n = int(input())
    height = list(map(int,input().split()))
    sorted(height)

    chimps = []
    last = -1

    for x in height:
        if x != last:
            chimps.append(x)  # Keeps only the unique elements.
            last = x
    q = int(input())
    queries = list(map(int,input().split()))
    sorted(queries)

    sz = len(chimps)


    for q in queries:
        a, b = binSearch(chimps, sz, q)
        tallest = str(chimps[a]) if a >= 0 else 'X'
        shortest = str(chimps[b]) if b < sz else 'X'
        print(tallest,shortest)


if __name__ == '__main__':
    main()