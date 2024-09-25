def divide(a,b):
    print(a/b)
divide(10,5)

def divide(a,b=1):
    print(a/b)
divide(5)

def divide(a=1,b=1):
    print(a/b)
divide()


def says_hello(name):
    print("hello " + name)

print("please enter your name")
name = input()
says_hello(name)

name = "deniz"
says_hello(name)


def sum(number1,number2):
    answer = number1 + number2

result = sum(3,5)
print(result)

def sum(number1,number2):
    answer = number1 + number2
    return answer

result1 = sum(3,5)
print(result1)

result2 = sum(number1=3,number2=5)
print(result2)


def greetings(first_name,last_name,use_auto_correction):
    if use_auto_correction == True:
        capitalized_first_name = first_name.capitalize()
        capitalized_last_name = last_name.capitalize()
        print("hello",capitalized_first_name,capitalized_last_name)
    else:
        print("hello",first_name,last_name)

greetings("irEm","ozdEmir",True)
greetings("irEm","ozdEmir",False)

def greetings(first_name,last_name,use_auto_correction = True):
    if use_auto_correction == True:
        capitalized_first_name = first_name.capitalize()
        capitalized_last_name = last_name.capitalize()
        print("hello",capitalized_first_name,capitalized_last_name)
    else:
        print("hello",first_name,last_name)

greetings("irEm","ozdEmir")


number1 = 13

def change_number1():
    number1 = 4

change_number1()
print(number1)

number2 = 11

def change_number2():
    global number2
    number2 = 4

change_number2()
print(number2)