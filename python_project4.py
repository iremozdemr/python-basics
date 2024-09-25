print("what is the temperature?")
celcius = int(input())

if celcius > 30:
    print("hot")
elif 30 >= celcius > 20:
    print("good")
elif 20 >= celcius > -273:
    print("cold")
else:
    print("wrong input!")

print()

print("do you have a drivers licence?")
drivers_licence = input()
print("how old are you?")
age = int(input())

if age > 17:
    if drivers_licence:
        print("you can drive car")
    else:
        "you need to go to a drivers licence course"
else:
    print("you need to get older")
