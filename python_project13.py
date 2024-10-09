#f string:
#% operatörüne göre daha hızlıdır
#str.format() methoduna göre daha hızlıdır

#yöntem 1:

def greet(name):
    return f"hello, {name}!"

def wrapper(func):
    def wrapped(*args,**kwargs):
        print("fonksiyon cagrilmadan önce")
        result = func(*args,**kwargs)
        print("fonksiyon cagrildiktan sonra")
        print(result)
        return result
    return wrapped

wrapped_greet = wrapper(greet)
wrapped_greet("alice")

#yöntem 2:

@wrapper
def greet(name):
    return f"hello, {name}!"

def wrapper(func):
    def wrapped(*args,**kwargs):
        print("fonksiyon cagrilmadan önce")
        result = func(*args,**kwargs)
        print("fonksiyon cagrildiktan sonra")
        print(result)
        return result
    return wrapped

greet("alice")