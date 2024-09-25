#lambda:

def divide(a,b):
    return a/b

print(divide(10,2))

divide_lambda = lambda a,b : a/b
print(divide_lambda(10,2))

#map:

salaries = [1000,2000,3000,4000,5000]

my_list = list(map(lambda x : x + 100, salaries))

print(salaries)
print(my_list)

#filter

numbers = [1,2,3,4,5,6,7,8]

my_list = list(filter(lambda x : x % 2 == 0, numbers))

print(numbers)
print(my_list)

#reduce

from functools import reduce

ages = [1,2,3,4]

my_list = reduce(lambda a,b : a+b, ages)

print(ages)
print(my_list)