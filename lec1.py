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


# Arrays https://codeforces.com/problemset/problem/572/A

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

# Big Segment https://codeforces.com/problemset/problem/242/B
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
# Vitaly and Strings
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

# Passwords
# Theo cách nhập mật khẩu của Vanya, các mật khẩu có chiều dài nhỏ nhất sẽ được nhập trước, rồi đến các mật khẩu có chiều dài nhỏ thứ hai, cứ tiếp tục như vậy. Đến khi chiều dài bằng chiều dài mật khẩu đúng, thì trường hợp tốt sẽ nhập đúng ngay lần đầu tiên, trường hợp xấu sẽ nhập đúng sau khi đã nhập tất cả mật khẩu cùng chiều dài.
# Vậy với nn mật khẩu, ta sẽ đếm xem ứng với mỗi chiều dài thì có bao nhiêu chuỗi cùng chiều dài đó, lưu lại thông tin này.
# Sau đó, để tìm thời gian cho trường hợp tốt nhất, đi tính tổng số mật khẩu có chiều dài nhỏ hơn chiều dài mật khẩu đúng, đây cũng là thời gian dành để nhập các mật khẩu. Sau kk lần nhập sai thì bị chặn 5 giây, nên ta lấy tổng vừa tìm được chia cho kk ra được số lần bị chặn, rồi nhân cho 5, ta sẽ biết được tổng số thời gian bị chặn. Ta lấy tổng số mật khẩu tìm được trước đó cộng với tổng thời gian bị chặn sẽ biết được tổng thời gian nhập các mật khẩu sai có chiều dài nhỏ hơn chiều dài mật khẩu đúng.
# Thực hiện tương tự để tìm thời gian cho trường hợp xấu nhất, nhưng chỗ tính tổng số mật khẩu, ta cộng thêm số mật khẩu cùng chiều dài với mật khẩu đúng, nhớ trừ đi 1 (trừ mật khẩu đúng).
# Lấy kết quả ở cả hai trường hợp ta đã tính được cộng thêm 1 (thời gian nhập mật khẩu đúng) là ra đáp án cuối cùng.
# Độ phức tạp: O(n + length(s))O(n+length(s)) với nn là số lượng chuỗi nhập và length(s)length(s) là độ dài chuỗi ss là chuỗi mật khẩu đúng.

n, k = map(int, input().split())
password = []
for i in range(n):
    s = input()
    password.append(s)
res = input()
lower, upper = 0, 0

for i in range(n):
    lower += (len(password[i]) < len(res))
    upper += (len(password[i]) <= len(res))

print(lower + (lower // k) * 5 + 1, upper + ((upper - 1) // k) * 5)
