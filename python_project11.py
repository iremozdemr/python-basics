#first class objects:
#functions are first class objects
#functions can be used as arguments
#functions can be passed as arguments
#a function is an instance of the object type
#you can store the function in a variable
#you can return the function from a function
#you can store functions in data structures such as hash tables lists

#treating the functions as objects:

def shout(text):
    return text.upper()

print(shout("hello"))

yell = shout

print(yell("hello"))
#shout isimli function çağırılmaz
#yell isimli function çağırılır
#iki function da aynı yere işaret eder

#passing the functions as arguments:

def function1(text):
    return text.upper()

def function2(text):
    return text.lower()

def my_function(function):
    print(function("hello"))

my_function(function1)
my_function(function2)

#returning functions from another function

def create_adder(x): 
    def adder(y): 
        return x+y 

    return adder 

a = create_adder(15)
b = a(10)

print(b)