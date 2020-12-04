#Energy Exchange
# n, k = map(int, input().split())
# a = sorted(list(map(int, input().split())))
#
# left = 0
# right = a[-1]
# print(right)
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
def bsFirst(a, left, right, x):
    if left <= right:
        mid = (left+right)//2
        
# Function to find first occurrence of a given number
# in sorted list of integers
def findFirstOccurrence(A, x):
    # search space is A[left..right]
    (left, right) = (0, len(A) - 1)

    # initialize the result by -1
    result = -1

    # iterate till search space contains at-least one element
    while left <= right:

        # find the mid value in the search space and
        # compares it with key value
        mid = (left + right) // 2

        # if key is found, update the result and
        # go on searching towards left (lefter indices)
        if x == A[mid]:
            result = mid
            right = mid - 1

        # if key is less than the mid element, discard right half
        elif x < A[mid]:
            right = mid - 1

        # if key is more than the mid element, discard left half
        else:
            left = mid + 1

    # return the leftmost index or -1 if the element is not found
    return result


# if __name__ == '__main__':
#
#     A = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
#     key = 5
#
#     index = findFirstOccurrence(A, key)
#
#     if index != -1:
#         print("First occurrence of element", key, "is found at index", index)
#     else:
#         print("Element found not in the list")

n,q = map(int, input().split())

while n!= 0 and q!=0:

    a = []
    for _ in range(n):
        marble_num = int(input())
        a.append(marble_num)
    sorted(a)
    b = []
    for _ in range(q):
        query = int(input())
        b.append(query)
    for i in b:
        pos = findFirstOccurrence(a,i)
        if pos == -1:
            print(i,'not found')
        else:
            print(i,'found at',pos)
    n,q = map(int,input().split())
