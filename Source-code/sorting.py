v = [2, 3, 6, 1, 9, 10]

# Sap xep tang dan
v.sort(reverse=False)
v = sorted(v, reverse=False)

# Sap xep giam dan
v.sort(key=lambda x: -x)
v = sorted(v, key=lambda x: -x)

v.sort(reverse=True)
v = sorted(v, reverse=True)

# Sap xep mang con
v[1:4] = sorted(v[1:4])


# Khai bao cau truc phan so
class Fraction:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom


frac = []
frac.append(Fraction(5, 4))
frac.append(Fraction(7, 9))
frac.append(Fraction(1, 8))
frac.append(Fraction(9, 2))
frac.append(Fraction(12, 8))

#Sap xep mang cau truc tang dan
frac.sort(key=lambda fraction: fraction.num/fraction.denom)

#Sap xep cau truc sinh vien
class Student:
    def __init__(self, id=0, score=0):
        self.id = id
        self.score = score
    def __lt__(self, other):
        if (self.score > other.score) or (self.score == other.score and self.id < other.id):
            return True
        return False

if __name__ == '__main__':

    list_student = []

    list_student.append(Student(100, 8.5))
    list_student.append(Student(101, 7.5))
    list_student.append(Student(102, 8.5))
    list_student.append(Student(103, 10.0))
    list_student.append(Student(104, 10.0))
    list_student.append(Student(105, 4.5))

    #Mac dinh Python sap tang dan
    list_student.sort()

    #Sap diem giam dan ta dao nguoc chieu
    list_student.sort(key=lambda s: (-s.score, s.id))
    for student in list_student:
        print(student.id, student.score)

