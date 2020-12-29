l = []
l.insert(2, 9)  # Chen gia tri 9 vao vi tri thu 2
l.pop(2)  # Xoa gia tri trong list o vi tri thu 2 va tra ve gia tri bi xoa
l.clear()  # Xoa toan bo cac phan tu
l.extend(2 * [
    0])  # De tang kich thuoc cua list, ta noi them list moi vao list hien tai => list l se co them 2 phan tu 0 o cuoi
l = l[0:2]  # slicing de giam kich thuoc array

# Cac ham co ban dung trong string
chr()
s = "Hello"
res = s.isalpha()  # Co phai la chu cai khong
s.isdigit()
s.islower()
s.isupper()
# In hoa in thuong ky tu ASCII
string = "algorithm"
c = chr(ord(string[2] - 32))
