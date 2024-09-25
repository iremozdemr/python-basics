students = ["john","mark","venessa","mariam"]

for student in students:
    print(student)
#çıktı:
#john
#mark
#venessa
#mariam

for index,student in enumerate(students):
    print(index,student)
#çıktı:
#0 john
#1 mark
#2 venessa
#3 mariam

for student,index in enumerate(students):
    print(index,student)
#çıktı:
#john 0
#mark 1
#venessa 2
#mariam 3

for student,index in enumerate(students):
    print(student,index)
#çıktı:
#0 john
#1 mark
#2 venessa
#3 mariam

for index,student in enumerate(students,1):
    print(index,student)
#çıktı:
#1 john
#2 mark
#3 venessa
#4 mariam