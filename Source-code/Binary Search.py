import bisect


def binarySearch(a, left, right, x):
    while left <= right:
        mid = (left + right) // 2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == '__main__':
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    result = binarySearch(a, 0, n - 1, x)
    print(result)


def binarySearchRecursion(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        if a[mid] > x:
            return binarySearchRecursion(a, left, mid - 1, x)
        return binarySearchRecursion(a, mid + 1, right, x)
    return -1


# Tim phan tu dau tien


def bsFirst(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if (mid == left or x > a[mid - 1]) and a[mid] == x:
            return mid
        elif x > a[mid]:
            return bsFirst(a, mid + 1, right, x)
        else:
            return bsFirst(a, left, mid - 1, x)
    return -1


# Tim phan tu cuoi cung


def bsLast(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if (mid == right or x < a[mid + 1]) and a[mid] == x:
            return mid
        elif x < a[mid]:
            return bsLast(a, left, mid - 1, x)
        else:
            return bsLast(a, mid + 1, right, x)
    return -1


#Ham tim can duoi: tra ve vi tri dau tien >= gia tri tim kiem trong doan [first,last)
def main():
    a = [1,1,2,2,2,3,4,5,7]
    n,x = 9,3
    lowerBound = bisect.bisect_left(a,x,0,n)
    print(lowerBound)

#Ham tim can tren: tra ve vi tri dau tien > gia tri tim kiem trong doan [first, last)

    upperBound = bisect.bisect_right(a,x,0,n)
    print(upperBound)