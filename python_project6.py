def says_hello(name):
    print("hello " + name)

print("please enter your name")
name = input()
says_hello(name)
says_hello("deniz")


def sum(number1,number2):
    answer = number1 + number2

result = sum(3,5)
print(result)


def sum(number1,number2):
    answer = number1 + number2
    return answer

result = sum(3,5)
print(result)


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