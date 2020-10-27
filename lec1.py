# Fashion
#
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


# Night at the Museum

def main():
    n = input()
    s = map(ord, n)

    res = 0
    curr = 0

    A = ord('a')
    Z = ord('z')

    for x in s:
        if A <= x <= Z:
            x -= A
            res += min(abs(x - curr), 26 - abs(x - curr))
            curr = x
        else:
            break

    print(res)


# if __name__ == '__main__':
#     main()

# Bear and Game

n = int(input())
v = list(map(int, input().split()))

start = 0
watch = 0
for i in v:
    if i - start <= 15:
        watch = i
        start = i
    else:
        break

print(min(90, watch + 15))

# Vitaly and Strings
str1 = input()
str2 = input()
