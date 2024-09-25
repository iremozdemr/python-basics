#loops:
#-for loop
#-while loop

#to end the infinite loop press ctrl+c


volcano_name = "eyjafjallaj"
for i in volcano_name:
    print(i)


numbers = [1,2,3,4,5]
for i in numbers:
    print(i)


numbers = range(5,21)
for i in numbers:
    print(i)
#starts with 5, ends with 20


numbers = range(1,101)
for i in numbers:
    if i % 5 == 0:
        print(i)


celcius = 10
while celcius < 50:
    if celcius > 30:
        print("hot")
    elif 30 >= celcius > 20:
        print("good")
    elif 20 >= celcius > -273:
        print("cold")
    else:
        print("wrong input!")
    print("the current temperature is " + str(celcius))
    celcius += 5


import time
celcius = 10
while celcius < 50:
    if celcius > 30:
        print("hot")
    elif 30 >= celcius > 20:
        print("good")
    elif 20 >= celcius > -273:
        print("cold")
    else:
        print("wrong input!")
    print("the current temperature is " + str(celcius))
    celcius += 5
    time.sleep(1)


import random
while True:
    number = random.randint(0,10)
    print(number)
    if(number == 7):
        print("found!")
        break


names = ["max","felix","lucas",26,"sarah"]
for name in names:
    if(type(name) != str):
        print("this is not a name")
        break
    else:
        print(name)