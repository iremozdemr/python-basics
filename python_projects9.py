students = ["john","mark","venessa","mariam"]
departments = ["math","statistics","physics","astronomy"]
ages = [23,30,26,22]

new_list = list(zip(students,departments,ages))
print(new_list)

new_list = list(zip(departments,ages,students))
print(new_list)

students = ["john"]
departments = ["math","statistics","physics","astronomy"]
ages = [23,30,26,22,15]

new_list = list(zip(students,departments,ages))
print(new_list)

students = []
departments = ["math","statistics","physics","astronomy"]
ages = [23,30,26,22,15]

new_list = list(zip(students,departments,ages))
print(new_list)