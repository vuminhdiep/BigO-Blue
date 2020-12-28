l = []
l.insert(2, 9) #Chen gia tri 9 vao vi tri thu 2
l.pop(2) #Xoa gia tri trong list o vi tri thu 2 va tra ve gia tri bi xoa
l.clear() #Xoa toan bo cac phan tu
l.extend(2*[0]) #De tang kich thuoc cua list, ta noi them list moi vao list hien tai => list l se co them 2 phan tu 0 o cuoi
l = l[0:2] #slicing de giam kich thuoc array

#Cac ham co ban dung trong string
string0 = "hakunamatata"
string1 = "123"

string0 = string0[:3] + string1 + string0