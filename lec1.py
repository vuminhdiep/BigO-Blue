#Fashion
def check_jacket(v, n):
    # 1-button jacket
    if n == 1:
        if v[0] == 1:
            return True
        else:
            return False
    count = 0
    for i in range(n):
        if v[i] == 0:
            count += 1

    if count == 1:
        return True
    else:
        return False


n = int(input())
v = list(map(int, input().split()))
if check_jacket(v, n):
    print("YES")
else:
    print("NO")


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
    print(str(res) + '\n')


if __name__ == '__main__':
    main()
